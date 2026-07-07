import json
from collections import defaultdict

paths = [
    "/Users/gabrieljang/Documents/AX Hackerton/submissions/samilpwc/submission/logs/transcript.jsonl",
    "/Users/gabrieljang/Documents/AX Hackerton/submissions/kakaopaysec/submission/logs/transcript.jsonl",
    "/Users/gabrieljang/Documents/AX Hackerton/submissions/musinsa/submission/logs/original_conversation_transcript.jsonl"
]

print("Loop and Duplicate Patch Analysis:")
print("-----------------------------------")

for path in paths:
    team = path.split('/')[6] # AX Hackerton -> submissions -> [team]
    print(f"=== Analysis for {team} ===")
    
    total_steps = 0
    modifications = defaultdict(int)
    commands = defaultdict(int)
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data = json.loads(line)
                except:
                    continue
                
                if data.get("type") == "PLANNER_RESPONSE":
                    total_steps += 1
                    tool_calls = data.get("tool_calls", [])
                    for call in tool_calls:
                        name = call.get("name")
                        args = call.get("args", {})
                        if name in ["replace_file_content", "multi_replace_file_content", "write_to_file"]:
                            target_file = args.get("TargetFile")
                            if target_file:
                                modifications[target_file] += 1
                        elif name == "run_command":
                            cmd = args.get("CommandLine", "")
                            commands[cmd] += 1
    except FileNotFoundError:
        print(f"File not found: {path}\n")
        continue
    
    print(f"Total PLANNER_RESPONSE steps (turns): {total_steps}")
    
    total_modifications = sum(modifications.values())
    print(f"Total file modifications (patches): {total_modifications}")
    print("Top 5 modified files:")
    for file, count in sorted(modifications.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {file.split('/')[-1]}: {count} times")
        
    print("Top 5 repeated commands:")
    for cmd, count in sorted(commands.items(), key=lambda x: x[1], reverse=True)[:5]:
        if count > 1:
            print(f"  {cmd[:80]}...: {count} times")
            
    print("\n")
