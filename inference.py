from env.environment import EmailEnv
from env.models import Action

env = EmailEnv()

print("[START] task=email env=openenv model=baseline")

obs = env.reset()
done = False
step = 0
rewards = []

while not done:
    step += 1

    email = obs.email

    if "free" in email.lower():
        action = "spam"
    else:
        action = "important"

    obs, reward, done, _ = env.step(Action(label=action))

    rewards.append(reward)

    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

print(f"[END] success=true steps={step} rewards={','.join([f'{r:.2f}' for r in rewards])}")