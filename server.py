from fastapi import FastAPI
from env.environment import EmailEnv
from env.models import Action

app = FastAPI()
env = EmailEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": {
            "email": obs.email,
            "step_count": obs.step_count
        }
    }

@app.post("/step")
def step(action: dict):
    act = Action(**action)
    obs, reward, done, _ = env.step(act)

    return {
        "observation": {
            "email": obs.email if obs else None,
            "step_count": obs.step_count if obs else None
        } if obs else None,
        "reward": reward,
        "done": done,
        "info": {}
    }