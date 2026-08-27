import os
import json
import random
import time
from google import genai
from google.genai import types

# 설정
NUM_TARGET_ITEMS = 5000
BATCH_SIZE = 50
OUTPUT_SOP_FILE = "../samilpwc/samilpwc_submission/src/data/Dummy_SOP_Snippets.json"
OUTPUT_BIZ_FILE = "../samilpwc/samilpwc_submission/src/data/Dummy_Business_Data.json"

client = genai.Client(vertexai=True, project="flai-oosuhada-20260506", location="us-central1")

# SOP 생성을 위한 다양한 기업 규제/감사 테마
SOP_SEEDS = [
    "재무 회계 및 자금 횡령 방지 가이드라인",
    "IT 인프라 및 망분리 보안 규제",
    "인사(HR) 채용 비리 방지 및 성과급 지급 규정",
    "마케팅 비용 집행 및 법인카드 사용 지침",
    "ESG 경영 및 탄소 배출량 허위 보고(그린워싱) 방지",
    "하도급 업체 갑질 방지 및 공정거래법 준수",
    "해외 지사 파견 인력의 자금 운용 규칙",
    "개인정보보호법(GDPR 등) 대응 고객 데이터 폐기 규정",
    "사내 성희롱 및 직장내 괴롭힘 징계 절차",
    "임원진 스톡옵션 행사 및 내부자 거래 방지 가이드"
]

def generate_sop_batch(seed_theme, batch_size):
    prompt = f"""
다음 테마를 기반으로 글로벌 컨설팅 펌 수준의 매우 정교하고 현실적인 기업 내부 규정(SOP) 조항을 {batch_size}개 생성해주세요.

[테마]: {seed_theme}

출력 형식 (반드시 JSON 배열로 반환):
각 항목은 다음 필드를 가져야 합니다.
- "sop_id": "SOP-" + 무작위 4자리 숫자
- "category": 테마에 맞는 대분류 (예: "Finance", "HR", "IT", "Compliance")
- "title": 조항의 제목
- "rule_text": 조항의 상세 텍스트 (어기면 안되는 구체적인 행동 규칙, 한도, 권한 등 명시)
- "penalty_level": 위반 시 징계 수준 (예: "Warning", "Minor", "Major", "Dismissal")
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a Chief Compliance Officer. Output strictly a JSON array without markdown blocks.",
                temperature=0.8,
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
    print("=== 삼일PwC 대규모 LLM 추론(SOP) 파이프라인 시작 ===")
    
    final_sop_data = {
        "_metadata": {
            "source": "LLM Corporate Compliance Generator",
            "count": NUM_TARGET_ITEMS,
            "version": "v2.0_llm_reasoned"
        },
        "sops": []
    }
    
    generated_count = 0
    import random
    
    while generated_count < NUM_TARGET_ITEMS:
        seed = random.choice(SOP_SEEDS)
        request_size = min(BATCH_SIZE, NUM_TARGET_ITEMS - generated_count)
        print(f"[{generated_count}/{NUM_TARGET_ITEMS}] Seed: {seed[:15]}... ({request_size}개 추론 요청 중...)")
        
        enriched_batch = generate_sop_batch(seed, request_size)
        if enriched_batch:
            # ID 보정
            for i, item in enumerate(enriched_batch):
                item['sop_id'] = f"SOP-{generated_count + i + 1:04d}"
            final_sop_data["sops"].extend(enriched_batch)
            generated_count += len(enriched_batch)
        else:
            time.sleep(2)
            continue
            
        time.sleep(1)

    os.makedirs(os.path.dirname(OUTPUT_SOP_FILE), exist_ok=True)
    with open(OUTPUT_SOP_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_sop_data, f, ensure_ascii=False, indent=2)
    print(f"SOP 완료! {OUTPUT_SOP_FILE} 저장 성공.")
    
    # 비즈니스 데이터(Business Units)는 절차적 합성이 더 유리하지만, 일관성을 위해 일부 절차적 + 랜덤 배정
    print("Business Data 생성 중...")
    biz_data = {"business_unit_metrics": []}
    for i in range(NUM_TARGET_ITEMS):
        headcount = random.randint(30, 2000) # K-anonymity 통과를 위해 30 이상
        revenue = random.randint(1000000, 50000000)
        cost = int(revenue * random.uniform(0.5, 1.2)) # 간혹 적자(1.2) 발생
        
        biz_data["business_unit_metrics"].append({
            "unit_name": f"Unit_{i:04d}",
            "headcount": headcount,
            "q_revenue_usd": revenue,
            "q_cost_usd": cost,
            "risk_score": random.randint(1, 100)
        })
        
    with open(OUTPUT_BIZ_FILE, 'w', encoding='utf-8') as f:
        json.dump(biz_data, f, ensure_ascii=False, indent=2)
    print(f"Business Data 완료! {OUTPUT_BIZ_FILE} 저장 성공.")

if __name__ == "__main__":
    main()
