from fastapi import FastAPI
from env import EmailSentinelEnv
from models import Action, StepResponse

app = FastAPI(title="Nexus Email Sentinel")
env = EmailSentinelEnv()

@app.get("/")
def home():
    return {"message": "Nexus Email Sentinel is ONLINE", "spec": "OpenEnv v1.0"}

@app.post("/reset")
def reset(task_id: str = "easy_phish"):
    return {"observation": env.reset(task_id)}

@app.post("/step", response_model=StepResponse)
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}
