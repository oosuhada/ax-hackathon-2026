import json
import time
import sys

CMD_FILE = "/Users/gabriel/Documents/ax-hackathon-2026/logs/_mailbox/samilpwc/cmd_from_opus.json"
RES_FILE = "/Users/gabriel/Documents/ax-hackathon-2026/logs/_mailbox/samilpwc/result_from_gemini.json"

def get_cmd_id(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data.get("cmd_id", -1)
    except:
        return -1

if __name__ == "__main__":
    print("Starting mailbox poller...")
    initial_cmd = get_cmd_id(CMD_FILE)
    
    while True:
        current_cmd = get_cmd_id(CMD_FILE)
        
        # Trigger if cmd_from_opus.json has a new cmd_id that is different from our last known res_id
        # We also check if it changed from what it was when we started polling.
        res_id = get_cmd_id(RES_FILE)
        
        if current_cmd != res_id and current_cmd != -1:
            print(f"NEW COMMAND DETECTED! cmd_id: {current_cmd}. Exiting to wake up agent.")
            sys.exit(0)
            
        time.sleep(5)
