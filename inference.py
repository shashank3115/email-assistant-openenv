import os, requests

def run():
    url = "http://localhost:7860"
    print(f"[START] task=easy_phish env=EmailSentinel model=baseline-agent")
    
    # Reset
    init = requests.post(f"{url}/reset").json()
    
    # Step
    payload = {"call": "delete", "email_id": 1}
    res = requests.post(f"{url}/step", json=payload).json()
    
    reward = res['reward']
    print(f"[STEP] step=1 action=delete reward={reward} done=true error=null")
    print(f"[END] success={reward > 0.8} steps=1 rewards={reward}")

if __name__ == "__main__":
    run()
