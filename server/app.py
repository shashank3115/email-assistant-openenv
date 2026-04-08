from fastapi import FastAPI
from environment.env import AuditEnv
from environment.models import AuditAction

app = FastAPI()
env = AuditEnv()

@app.post("/reset")
async def reset():
    return env.reset()

@app.post("/step")
async def step(action: AuditAction):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}

@app.get("/state")
async def state():
    return env.state
@app.get("/")
async def home():
    return {"status": "Environment is Running", "benchmark": "file_audit_env"}

# Change the reset from @app.post to @app.api_route to be safe
@app.api_route("/reset", methods=["GET", "POST"])
async def reset(task_id: str = "easy"):
    return env.reset(task_id)