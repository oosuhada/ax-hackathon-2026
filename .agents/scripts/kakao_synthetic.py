import os
import json
import random
import time
from google import genai
from google.genai import types

# 설정
NUM_TARGET_ITEMS = 5000
BATCH_SIZE = 50
OUTPUT_FILE = "../kakaopaysec/kakaopaysec_submission/src/data/Dummy_Peer_Data.json"

client = genai.Client(vertexai=True, project="flai-oosuhada-20260506", location="us-central1")

# 다양한 LLM 추론을 유도하기 위한 페르소나/조건 Seed
PERSONA_SEEDS = [
    "20대 공격적 투자자 (가상화폐, 밈주식 선호)",
    "30대 직장인 (우량주 중심 장기투자, 배당주 선호)",
    "40대 보수적 투자자 (채권, ETF, 자산방어 선호)",
    "50대 은퇴준비자 (월배당, 리스크 최소화)",
    "테마주 단타 스윙 투자자 (변동성 선호, 높은 컷로스)",
    "ESG 및 기술주 선호 30대 (나스닥 빅테크 집중)",
    "안전 자산 선호 (금, 달러 ETF 위주)",
    "배당률 8% 이상 고배당 추구 투자자",
    "성장주 위주의 영끌 투자자 (레버리지 잦음)",
    "미국 배당성장주 중심의 현금흐름 창출 투자자"
]

def generate_peer_batch(seed_persona, batch_size):
    prompt = f"""
다음 페르소나/투자 성향을 바탕으로 가상의 증권사 투자자 세그먼트(Peer Group) 데이터를 {batch_size}개 생성해주세요.
단순 무작위가 아닌, 각 페르소나에 맞는 매우 그럴듯한(Plausible) 수치와 설명(Reasoning)이 포함되어야 합니다.

[페르소나 조건]: {seed_persona}

출력 형식 (반드시 JSON 배열로 반환):
각 항목은 다음 필드를 가져야 합니다.
- "group_id": "pg_" + 무작위 4자리 영숫자
- "group_name": 페르소나를 묘사하는 그룹명 (예: "30대 우량주 장기투자 그룹")
- "description": 이 그룹의 특성에 대한 심층 설명
- "peer_hold_ratio_percent": 또래 중 이 종목(또는 유사 종목)을 보유/홀딩하는 비율 (퍼센트 숫자, 페르소나에 맞게 추론)
- "average_loss_cut_percent": 이 그룹의 평균 손절 라인 (-숫자)
- "fomo_trigger_keywords": 이 그룹이 가장 반응할 만한 FOMO 방어 키워드 배열 (예: ["장기복리", "시장수익률 벤치마크", "배당컷"])
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a senior financial analyst and behavioral economics expert. Output strictly a JSON array without markdown blocks.",
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
    print("=== 카카오페이증권 대규모 LLM 추론(Peer Group) 파이프라인 시작 ===")
    
    final_data = {
        "_metadata": {
            "source": "LLM Iterative Persona Generation",
            "count": NUM_TARGET_ITEMS,
            "version": "v2.0_llm_reasoned"
        },
        "peer_groups": []
    }
    
    # 데모용 Fallback (기존 정합성 유지)
    fallback_item = {
        "group_id": "pg_fallback",
        "group_name": "전체 평균",
        "description": "데이터가 부족할 때 사용되는 전체 시장 평균 그룹",
        "peer_hold_ratio_percent": 65.0,
        "average_loss_cut_percent": -15.0,
        "fomo_trigger_keywords": ["시장 평균", "안정성", "자산 배분"]
    }
    final_data["peer_groups"].append(fallback_item)
    
    generated_count = 1 # fallback 포함
    import random
    
    while generated_count < NUM_TARGET_ITEMS:
        seed = random.choice(PERSONA_SEEDS)
        request_size = min(BATCH_SIZE, NUM_TARGET_ITEMS - generated_count)
        print(f"[{generated_count}/{NUM_TARGET_ITEMS}] Seed: {seed} ({request_size}개 추론 요청 중...)")
        
        enriched_batch = generate_peer_batch(seed, request_size)
        if enriched_batch:
            # ID 보정
            for i, item in enumerate(enriched_batch):
                item['group_id'] = f"pg_{generated_count + i:05d}"
            final_data["peer_groups"].extend(enriched_batch)
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
