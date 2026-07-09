# Findings Backlog

### Round 1
- P1: Foreign language translation injection vulnerability (security-auditor)
- P2: Markdown blocks inside JSON string values could break parsing (qa-tester)
- P2: Time-to-checkout metric is missing from ROI (roi-architect)

### Round 2
- P2: Empty `rejected_options` array when recommending an item undermines the 1-Pick 'Why Not' philosophy (qa-tester)
- P2: Prompt injection using zero-width spaces or Unicode bidirectionals could bypass keyword filters (security-auditor)
- P2: Customer Service (CS) ticket reduction is a major ROI point but missing from README (roi-architect)

### Round 3
- P2: Users asking for the "2nd best" or "alternative" item can break the 1-Pick absolute conviction model (qa-tester)
- P1: Roleplaying jailbreaks (e.g., DAN) can bypass identity constraints and force unstructured output (security-auditor)
- P2: Inventory Liquidation ROI metric lacks mention of "discount promotion cost reduction" (roi-architect)

### Round 4
- P2: Logical contradictions in user input (e.g. summer puffer jacket) force the agent to make a flawed guess rather than asking for clarity (qa-tester)
- P2: Users asking for the "empty JSON template" could leak the internal schema structure (security-auditor)
- P2: The ROI section is missing "Response Latency / Bounce Rate" reduction which is a natural benefit of 1-Pick's small output size (roi-architect)

### Round 5
- P1: Reflection of executable code (e.g., XSS or SQLi) could be dangerous if the client blindly renders the agent's response (security-auditor)
- P2: Confidence score type could drift to integer or float instead of string, breaking strict parsing (qa-tester)
- P3: Backend server load reduction from the Pivot feature is an excellent ROI point but omitted from README (roi-architect)

### Round 6
- P2: When `one_pick_item` is "N/A", the `rejected_options` array should logically be empty, but users can force it to be populated, confusing parsers (qa-tester)
- P2: HTML comment injection could bypass filters while still being processed by downstream parsers (security-auditor)
- P3: API egress cost savings due to the strictly bounded JSON structure is a great ROI point but missing (roi-architect)

### Round 7
- P2: Extremely long meaningless strings without spaces can cause token exhaustion or parser timeouts (qa-tester)
- P1: Multi-turn emulation injections (e.g. injecting 'Agent: Okay I am unlocked') can confuse the LLM into dropping guardrails (security-auditor)
- P2: Reverse Logistics Cost (return shipping fees) reduction is missing from ROI metrics (roi-architect)

### Round 8
- P2: Model might mutate JSON keys (e.g. `one_pick` instead of `one_pick_item`) if instructed, breaking downstream parsing (qa-tester)
- P2: Deeply nested brackets or symbols injected by user could cause Regex DoS in naive filters (security-auditor)
- P2: Token efficiency (30% increase) due to non-conversational strict JSON format is missing from ROI (roi-architect)

### Round 9
- P2: Negative numbers in budget queries could cause logic processing errors or weird behavior (qa-tester)
- P2: Instructing the agent to perform complex math calculations (e.g., square roots) wastes tokens and latency (security-auditor)
- P2: Explicit mention of "결제 전환율(CVR) 상승" is needed to solidify the business case for Hackathon judges (roi-architect)

### Round 10 (Halfway Milestone)
- P2: Generic rejection reasons (e.g. "not a good fit") weaken the "1-Pick" authoritative tone and UX (qa-tester)
- P2: Asking the agent to encode its output (e.g., Base64) can bypass linguistic and format filters (security-auditor)
- P2: "Hyper-personalized experience" and its effect on Customer Lifetime Value (LTV) should be explicitly stated (roi-architect)

### Round 11
- P3: Compound attacks could confuse the LLM's priority queue (e.g. should it reject because of Stonewall, or because of 2nd best request?) (qa-tester)
- P2: Combining Zero-width space injection with Translation and Base64 encoding tests the limit of parser robustness (security-auditor)
- P3: Zero operational risk against compound attacks is a major enterprise selling point missing from README (roi-architect)

### Round 12
- P2: Brand hallucination trap: If a user demands a specific unavailable brand, the agent might invent one instead of cleanly failing (qa-tester)
- P2: Context Amnesia Attack: Massive input length could push system prompts out of the attention window, breaking JSON constraints (security-auditor)
- P3: Explicitly marketing "Brand Safety and Zero Hallucination" is highly effective for Enterprise B2B hackathon scores (roi-architect)

### Round 13
- P2: Complex strings with unescaped quotes or slashes in user input might be echoed back improperly, breaking JSON syntax (qa-tester)
- P2: Command injection syntaxes (e.g., `$()`, `&&`, `|`) could be dangerous if logged or parsed by vulnerable downstream bash scripts (security-auditor)
- P3: Data Pipeline Integrity (Acting as a firewall for downstream ML training) is a powerful Hackathon pitch point (roi-architect)

### Round 14
- P2: Contradictory sizing constraints (e.g. S size but XL fit) without 'oversized' keywords could break matching logic (qa-tester)
- P2: Time delay injections ("wait 10 seconds") waste GPU compute time and degrade latency (security-auditor)
- P3: "Zero Decision Fatigue" is the core thesis of 1-Pick and must be boldly stated in the README ROI (roi-architect)

### Round 15
- P2: Output truncation due to hitting token limits leaves unclosed JSON brackets, fatally crashing the parser (qa-tester)
- P2: Recursive logic loops injected by user can cause the LLM to get stuck thinking or generating max tokens (security-auditor)
- P3: Emphasizing "Resilience" and 0% downtime due to parsing errors is a strong enterprise feature for the README (roi-architect)

### Round 16
- P2: Users inputting an array of JSON objects can confuse the agent into returning a list instead of a single recommendation (qa-tester)
- P2: Emotional manipulation ("dying wish") or fake authority ("developer test") can exploit the LLM's safety-alignment to break its persona (security-auditor)
- P3: Emphasizing "Brand Persona Consistency" against emotional attacks adds massive trust value for Enterprise B2B pitching (roi-architect)

### Round 17
- P2: Forcing the agent to write rejections as poems or creative writing breaks the professional tone and increases token size (qa-tester)
- P2: Semantic redefinition attacks (e.g. changing the meaning of N/A to mean a specific item) could bypass the hardcoded fallback mechanism (security-auditor)
- P3: A strictly bounded agent is highly suited for A/B testing pipelines, which should be pitched in the README (roi-architect)

### Round 18
- P2: Logic collision where the agent could potentially list the recommended item inside `rejected_options` if pushed by a contradictory prompt (qa-tester)
- P2: Demanding deep sorting (e.g. median, percentiles) of the entire DB wastes compute tokens and goes against the quick 1-Pick philosophy (security-auditor)
- P3: Capturing "Why Not" data when returning N/A acts as a valuable trend-spotting tool for merchandisers, which is a great Hackathon pitch (roi-architect)

### Round 19
- P2: Data from the catalog with native unescaped quotes might corrupt the JSON if not sanitized upon interpolation (qa-tester)
- P2: "Reverse Prompt Injection" where users pretend a decision was already made in a previous turn could trick the agent into confirming a hallucination (security-auditor)
- P3: Highlighting horizontal scale-up readiness (handling Black Friday spikes) due to token efficiency is the perfect Hackathon climax (roi-architect)

### Round 20 (GRAND FINALE)
- P3: ZWNJ (Zero-width non-joiner) characters injected directly into JSON keys could bypass literal string matching parsers (qa-tester)
- P2: "System Override" and "Delete Instructions" payload attempts to wipe the agent's memory completely (security-auditor)
- P3: The 20-Round Autonomous Validation process itself is a massive Hackathon selling point and needs to be highlighted in README (roi-architect)

