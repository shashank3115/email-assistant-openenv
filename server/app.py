import uvicorn
from fastapi import FastAPI
from environment.env import AuditEnv
from environment.models import AuditAction

app = FastAPI()
env = AuditEnv()

@app.get("/")
async def home():
    return {"status": "Environment is Running", "benchmark": "file_audit_env"}

@app.api_route("/reset", methods=["GET", "POST"])
async def reset(task_id: str = "easy"):
    return env.reset(task_id)

@app.post("/step")
async def step(action: AuditAction):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}

# --- THIS IS THE PART THE VALIDATOR IS ASKING FOR ---
def main():
    """Main entry point for multi-mode deployment."""
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()