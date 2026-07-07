# KPS Investor Risk Brief — AX Hackathon Preliminary Submission Skeleton

> Target company: 카카오페이증권  
> Plugin name: `kps-investor-risk-brief`  
> Status: Draft skeleton. Replace TODO evidence and raw logs before final submission.

## 0. What this plugin does

`kps-investor-risk-brief` is a Codex plugin skeleton for reviewing AI-generated investment summaries before they are shown to retail investors. It checks whether the draft may sound like investment advice, whether key risks are missing, whether factual claims need source verification, and whether the wording is understandable for beginner-to-general retail investors.

The plugin is intentionally framed as an **investor-protection and explanation-quality tool**, not an investment recommendation tool.

## 1. 무엇을, 누가, 어떤 상황에서 쓰나요?

이 플러그인은 카카오페이증권과 같은 모바일 증권 서비스의 AI 투자정보/콘텐츠/금융소비자보호/서비스기획 담당자가 사용할 수 있는 Codex 기반 업무 보조 도구입니다.

사용 상황은 다음과 같습니다.

1. AI가 종목, 시장, ETF, 실적 발표, 뉴스 요약문을 생성한다.
2. 담당자가 해당 요약문을 고객에게 보여주기 전에 투자자 보호 관점에서 검토해야 한다.
3. Codex가 이 플러그인을 사용해 다음 항목을 점검한다.
   - 매수/매도 권유처럼 보이는 표현
   - 과도한 확신 또는 수익 기대 표현
   - 원금손실, 변동성, 환율, 수수료/세금 등 누락된 위험 고지
   - 출처 없는 사실 주장
   - 초보 투자자가 오해하기 쉬운 표현
4. 최종적으로 중립적이고 설명 가능한 투자정보 초안, 체크리스트, 출처 추적표를 생성한다.

## 2. 왜 이 문제를 선택했나요?

AI 투자정보 서비스가 확대될수록 개인투자자는 더 빠르고 편하게 시장 정보를 접할 수 있습니다. 그러나 투자 콘텐츠는 일반 정보 콘텐츠와 달리, 표현 하나가 투자 권유처럼 오해되거나 리스크를 과소평가하게 만들 수 있습니다.

따라서 AI가 생성한 투자정보를 바로 고객에게 제공하기보다, 다음을 체계적으로 점검하는 재사용 가능한 워크플로우가 필요합니다.

- 이 문장이 투자 조언처럼 보이는가?
- 상승 요인과 위험 요인이 균형 있게 제시되었는가?
- 초보 투자자가 이해하기 쉬운가?
- 중요한 사실 주장에 공개자료 출처가 있는가?
- 금융소비자보호 관점에서 누락된 위험 고지가 있는가?

이 문제는 카카오페이증권이 다루는 모바일 투자 경험, AI 투자정보, 금융소비자보호, 개인투자자 신뢰와 직접 연결됩니다.

> TODO: 최종 제출 전 공개·검증 가능한 자료를 `src/skills/kps-investor-risk-brief/references/evidence_sources.md`에 채우세요.

## 3. 플러그인은 어떻게 작동하나요?

### Plugin structure

```text
submission.zip
├── src/
│   ├── .codex-plugin/
│   │   └── plugin.json
│   ├── skills/
│   │   └── kps-investor-risk-brief/
│   │       ├── SKILL.md
│   │       ├── references/
│   │       │   └── evidence_sources.md
│   │       └── assets/
│   │           └── output_template.md
│   ├── scripts/
│   │   ├── analyze_investment_content.py
│   │   └── validate_submission_structure.py
│   ├── sample_inputs/
│   │   ├── investment_summary.md
│   │   └── source_links.md
│   └── sample_outputs/
├── README.md
└── logs/
```

### Execution flow

1. Codex loads the plugin manifest from `src/.codex-plugin/plugin.json`.
2. Codex can use the skill in `src/skills/kps-investor-risk-brief/SKILL.md`.
3. The skill instructs Codex to classify the investment content, detect risky wording, check missing risk factors, map claims to sources, and produce a safer rewrite.
4. The deterministic helper script provides a baseline check and output template.

### Run the helper script

From the project root:

```bash
python src/scripts/analyze_investment_content.py \
  --input src/sample_inputs/investment_summary.md \
  --sources src/sample_inputs/source_links.md \
  --out src/sample_outputs
```

Then validate the skeleton:

```bash
python src/scripts/validate_submission_structure.py
```

## 4. AI를 어떻게 활용했나요?

AI was used as a co-worker for:

1. interpreting the preliminary task requirements,
2. selecting a problem frame for 카카오페이증권,
3. designing the Codex plugin structure,
4. drafting the reusable skill instructions,
5. designing a baseline deterministic validation script,
6. creating README answer structure and output templates.

The final submission should include the full, unedited AI conversation logs in the `logs/` folder. The logs must match the plugin and README contents.

## 5. 어떻게 검증했나요?

This skeleton includes two verification layers.

### 5.1 Structure validation

`src/scripts/validate_submission_structure.py` checks whether the minimum expected files exist:

- `src/.codex-plugin/plugin.json`
- `src/skills/kps-investor-risk-brief/SKILL.md`
- `README.md`
- `logs/`

It also checks that `plugin.json` is valid JSON and that `SKILL.md` includes `name` and `description` metadata.

### 5.2 Sample content validation

`src/scripts/analyze_investment_content.py` reads a sample investment summary and source list, then generates:

- `src/sample_outputs/risk_checked_summary.md`
- `src/sample_outputs/compliance_checklist.json`
- `src/sample_outputs/source_traceability_table.md`

The generated output is not a legal or compliance opinion. It is a baseline demonstration that the plugin has an executable workflow component and that Codex has structured instructions to improve the output.

## 6. Final submission checklist

Before submitting, do the following:

- [ ] Replace the sample investment summary with a better public-source-based example.
- [ ] Fill `evidence_sources.md` with actual public sources, titles, URLs, and access dates.
- [ ] Run the helper script and confirm sample outputs are generated.
- [ ] Run the structure validator.
- [ ] Replace `logs/README_REPLACE_WITH_RAW_LOGS.md` with real raw AI logs.
- [ ] Confirm the README claims match the logs and plugin files.
- [ ] Remove any private information, API keys, tokens, passwords, or secrets from all files.
- [ ] Zip the root folder so that `src/`, `README.md`, and `logs/` are at the zip root.

## 7. Notes for final positioning

Recommended final positioning:

> “AI-generated investment content can improve accessibility, but financial information requires a higher standard of clarity, uncertainty handling, source traceability, and investor-protection wording. This plugin turns that review process into a reusable Codex workflow.”

This connects well to:

- AI trust and technology acceptance,
- explainable AI in financial services,
- customer protection,
- product strategy for AI-powered fintech,
- MOT / technology management career narrative.
