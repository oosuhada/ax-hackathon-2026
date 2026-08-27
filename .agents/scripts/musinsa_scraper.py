import os
import json
import time
import requests
from bs4 import BeautifulSoup
from google import genai
from google.genai import types

client = genai.Client(vertexai=True, project="flai-oosuhada-20260506", location="us-central1")

# 설정
NUM_TARGET_ITEMS = 5000
BATCH_SIZE = 50
OUTPUT_FILE = "../musinsa/musinsa_submission/src/data/Dummy_Product_Data.json"

def scrape_musinsa_base_data(limit=100):
    """무신사에서 기초 데이터(상품명, 가격 등) 크롤링 (차단 대비 샘플 데이터 폴백 포함)"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    items = []
    try:
        url = "https://www.musinsa.com/ranking/best"
        res = requests.get(url, headers=headers, timeout=5)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            goods_list = soup.select('.li_box')
            for goods in goods_list[:limit]:
                title_el = goods.select_one('.list_info a')
                price_el = goods.select_one('.price')
                brand_el = goods.select_one('.item_title')
                if title_el and price_el:
                    title = title_el.get('title', title_el.text).strip()
                    price = price_el.text.strip().replace('원', '').replace(',', '').strip()
                    brand = brand_el.text.strip() if brand_el else "Musinsa Standard"
                    items.append({"title": title, "price": price, "brand": brand})
    except Exception as e:
        print(f"Crawling error: {e}")
    
    # 부족한 분량을 위한 절차적 데이터 생성
    categories = ["오버핏 셔츠", "와이드 데님 팬츠", "바람막이 자켓", "캐시미어 니트", "크롭 티셔츠", "플리츠 스커트", "레더 자켓"]
    brands = ["커버낫", "디스이즈네버댓", "무신사 스탠다드", "라퍼지스토어", "아디다스", "나이키", "인사일런스", "드로우핏"]
    
    import random
    while len(items) < limit:
        brand = random.choice(brands)
        cat = random.choice(categories)
        items.append({
            "title": f"[{brand}] 24SS {cat} (블랙/그레이/화이트)",
            "price": str(random.randint(20000, 150000)),
            "brand": brand
        })
    return items

def enrich_with_llm(base_batch):
    """LLM을 호출하여 TPO, 핏, 반품 리스크 등 깊은 추론 생성"""
    prompt = f"""
다음은 패션 상품 데이터입니다. 패션 MD 관점에서 깊게 추론하여 JSON 배열 포맷으로 반환하세요.

입력 데이터:
{json.dumps(base_batch, ensure_ascii=False, indent=2)}

각 항목을 아래 필드를 포함한 JSON 형식으로 변환하세요:
- "item_id": "item_" + 무작위 4자리
- "name": 원본 title
- "price": 원본 price (숫자)
- "category": 카테고리 (예: "outer", "top", "bottom")
- "tpo_tags": 어울리는 TPO 3~4개 (예: ["소개팅", "하객룩", "캠퍼스"])
- "fit_cover_type": 커버해주는 체형 (예: "하체비만", "어깨좁음")
- "return_risk_note": 소재/핏 때문에 발생할 반품 리스크 (예: "니트 보풀 클레임 주의")
- "inventory_status": "in_stock" 또는 "low_stock"
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a fashion MD. Output ONLY JSON array. Do not wrap in ```json",
                temperature=0.7,
                max_output_tokens=4000,
            )
        )
        content = response.text.strip()
        if content.startswith('```json'): content = content[7:-3].strip()
        if content.startswith('```'): content = content[3:-3].strip()
        return json.loads(content)
    except Exception as e:
        print(f"LLM API Error: {e}")
        return []

def main():
    print("=== 무신사 대규모 LLM 추론 데이터 파이프라인 시작 ===")
    
    final_data = {
        "_metadata": {
            "source": "LLM Enrichment + Web Crawling",
            "count": NUM_TARGET_ITEMS,
            "version": "v2.0_llm_reasoned"
        },
        "items": []
    }
    
    essential_items = [
        {"item_id": "item_019", "name": "데님 오버핏 자켓", "price": 89000, "category": "outer", "tpo_tags": ["소개팅", "캠퍼스", "데일리"], "fit_cover_type": "어깨좁음", "return_risk_note": "소매 기장이 길어 반품 위험", "inventory_status": "in_stock"},
        {"item_id": "item_042", "name": "와이드 슬랙스", "price": 45000, "category": "bottom", "tpo_tags": ["오피스", "하객룩"], "fit_cover_type": "하체비만", "return_risk_note": "허리 사이즈 미스 주의", "inventory_status": "low_stock"},
        {"item_id": "item_088", "name": "캐시미어 블렌드 니트", "price": 62000, "category": "top", "tpo_tags": ["소개팅", "데이트"], "fit_cover_type": "마른체형", "return_risk_note": "피부 민감 고객 반품 위험", "inventory_status": "in_stock"}
    ]
    final_data["items"].extend(essential_items)
    
    generated_count = len(essential_items)
    base_data_pool = scrape_musinsa_base_data(limit=1000)
    
    print(f"목표 데이터 생성 개수: {NUM_TARGET_ITEMS}개")
    
    while generated_count < NUM_TARGET_ITEMS:
        import random
        batch = random.sample(base_data_pool, min(BATCH_SIZE, NUM_TARGET_ITEMS - generated_count))
        print(f"[{generated_count}/{NUM_TARGET_ITEMS}] LLM에 {len(batch)}개 추론 요청 중...")
        
        enriched_batch = enrich_with_llm(batch)
        if enriched_batch:
            for i, item in enumerate(enriched_batch):
                item['item_id'] = f"item_{generated_count + i + 1:04d}"
            final_data["items"].extend(enriched_batch)
            generated_count += len(enriched_batch)
        else:
            time.sleep(2)
            continue
            
        time.sleep(1)

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
    print(f"완료! {OUTPUT_FILE} 저장 성공.")

if __name__ == "__main__":
    main()
