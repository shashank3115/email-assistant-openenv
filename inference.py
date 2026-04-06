import os
import requests
import json

# Use the direct API URL
API_BASE = os.getenv("API_BASE_URL", "https://hf.space").rstrip('/')
HF_TOKEN = os.getenv("HF_TOKEN")

def run():
    print(f"[START] task=easy_phish env=EmailSentinel model=baseline-agent")
    
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        # 1. Reset
        resp = requests.post(f"{API_BASE}/reset?task_id=easy_phish", headers=headers)
        
        if resp.status_code != 200:
            # This will tell us if it's a 401 (Unauthorized) or 404 (Not Found)
            raise Exception(f"HTTP {resp.status_code}: Check your Token or URL.")

        # 2. Step
        action_payload = {"call": "delete", "email_id": 1}
        step_resp = requests.post(f"{API_BASE}/step", json=action_payload, headers=headers)
        
        res = step_resp.json()
        reward = res.get('reward', 0.0)
        done = res.get('done', True)
        
        print(f"[STEP] step=1 action=delete reward={reward} done={str(done).lower()} error=null")
        print(f"[END] success={reward > 0.8} steps=1 rewards={reward}")
        
    except Exception as e:
        # Debugging output to find the root cause
        print(f"[STEP] step=1 action=none reward=0.0 done=true error={str(e)}")
        print(f"[END] success=false steps=0 rewards=0.0")

if __name__ == "__main__":
    run()
