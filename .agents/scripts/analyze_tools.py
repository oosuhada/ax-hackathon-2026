import json
from collections import defaultdict

paths = [
    "/Users/gabrieljang/Documents/AX Hackerton/submissions/samilpwc/submission/logs/transcript.jsonl",
    "/Users/gabrieljang/Documents/AX Hackerton/submissions/kakaopaysec/submission/logs/transcript.jsonl",
    "/Users/gabrieljang/Documents/AX Hackerton/submissions/musinsa/submission/logs/original_conversation_transcript.jsonl"
]

print("Detailed Tool Call Analysis:")
print("-----------------------------------")

for path in paths:
    team = path.split('/')[6]
    print(f"=== Analysis for {team} ===")
    
    total_steps = 0
    tools_used = defaultdict(int)
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
                        tools_used[name] += 1
                        args = call.get("args", {})
                        
                        if name in ["replace_file_content", "multi_replace_file_content", "write_to_file"]:
                            target_file = args.get("TargetFile", "").strip('"').split('/')[-1]
                            if target_file:
                                modifications[target_file] += 1
                        elif name == "run_command":
                            cmd = args.get("CommandLine", "").strip('"')
                            # simplify cmd to see repeated patterns
                            short_cmd = cmd.split(' ')[0] + " " + " ".join(cmd.split(' ')[1:3])
                            commands[cmd] += 1
    except FileNotFoundError:
        print(f"File not found: {path}\n")
        continue
    
    print(f"Total PLANNER_RESPONSE steps: {total_steps}")
    print("Tools used distribution:")
    for t, c in sorted(tools_used.items(), key=lambda x: x[1], reverse=True):
        print(f"  {t}: {c}")
        
    print("\nTop 5 modified files:")
    for file, count in sorted(modifications.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {file}: {count} times")
        
    print("\nTop 5 commands:")
    for cmd, count in sorted(commands.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {cmd[:60]}...: {count} times")
            
    print("\n")
