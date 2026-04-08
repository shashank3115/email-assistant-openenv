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