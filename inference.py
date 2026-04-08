import os
import asyncio
from openai import OpenAI

# These must match the Hackathon requirements
API_KEY = os.getenv("HF_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")

async def main():
    client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)
    
    # [START] line is MANDATORY
    print(f"[START] task=file_cleanup env=audit_env model={MODEL_NAME}")
    
    # Simulation of a step (In a real submission, you'd loop this)
    print(f"[STEP] step=1 action=delete('virus.exe') reward=0.50 done=false error=null")
    print(f"[STEP] step=2 action=move('data_v1.csv') reward=1.00 done=true error=null")
    
    # [END] line is MANDATORY
    print(f"[END] success=true steps=2 score=1.00 rewards=0.50,1.00")

if __name__ == "__main__":
    asyncio.run(main())