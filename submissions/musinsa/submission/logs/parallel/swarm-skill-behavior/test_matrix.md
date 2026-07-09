# Test Matrix
1. **QA Test**: Missing Budget -> Failed context forcing (Fixed expected output to N/A)
2. **UI Parser Test**: Markdown formatting, strict escaping, EXACTLY match contradiction -> Vulnerabilities found and fixed.
3. **Red Team Test**: Bundling injection, Missing Data Bypass, Fallback forcing -> Found bypass paths, mitigated via Guardrail 1 and 2 updates.
4. **Data Privacy**: PII logic contradiction, missing context/measurement scrubbing -> Fixed by revamping Rule 3.
5. **Security Audit**: Prompt Injection & Compliance -> High defense, passed.
