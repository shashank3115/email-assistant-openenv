from env.environment import EmailEnv

env = EmailEnv()

print("[START]")

state = env.reset()
done = False

while not done:
    print("[STEP] State:", state)

    # simple logic
    if "free" in state.lower():
        action = "spam"
    else:
        action = "important"

    state, reward, done, _ = env.step(action)

    print("[STEP] Action:", action, "Reward:", reward)

print("[END]")