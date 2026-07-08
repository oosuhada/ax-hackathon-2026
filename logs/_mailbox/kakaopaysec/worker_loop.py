import time
import json
import os
import sys
import threading
import datetime

PROJECT_ROOT = "/Users/oosu/Documents/ax-hackathon-2026"
MAILBOX_DIR = f"{PROJECT_ROOT}/logs/_mailbox/kakaopaysec"
CMD_FILE = f"{MAILBOX_DIR}/cmd_from_opus.json"
HEARTBEAT_FILE = f"{MAILBOX_DIR}/heartbeat_gemini.txt"

seen_cmd_ids = set()
heartbeat_active = False

def heartbeat_thread():
    while True:
        if heartbeat_active:
            try:
                now_str = datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat()
                with open(HEARTBEAT_FILE, 'w') as f:
                    f.write(now_str)
            except Exception:
                pass
        time.sleep(30)

t = threading.Thread(target=heartbeat_thread, daemon=True)
t.start()

print("Ready and watching for commands...", flush=True)

while True:
    if os.path.exists(CMD_FILE):
        try:
            with open(CMD_FILE, 'r') as f:
                content = f.read()
                if content.strip():
                    data = json.loads(content)
                    cmd_id = data.get("cmd_id")
                    
                    if cmd_id and cmd_id not in seen_cmd_ids:
                        print(f"NEW_COMMAND_DETECTED: {json.dumps(data)}", flush=True)
                        seen_cmd_ids.add(cmd_id)
                        
                        action = data.get("action")
                        if action == "end_all":
                            print("Received end_all. Exiting.", flush=True)
                            sys.exit(0)
                        
                        heartbeat_active = True
                        
                        # Wait for agent to process
                        line = sys.stdin.readline()
                        
                        heartbeat_active = False
                        
                        if not line or line.strip() == "EXIT":
                            break
        except Exception as e:
            pass
    time.sleep(5)
