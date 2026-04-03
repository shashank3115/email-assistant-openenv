class EmailEnv:
    def __init__(self):
        self.emails = [
            "Meeting at 5pm",
            "Win a free iPhone!!!",
            "Project deadline tomorrow"
        ]
        self.index = 0

    def reset(self):
        self.index = 0
        return self.emails[self.index]

    def step(self, action):
        correct = ["important", "spam", "important"]

        reward = 1.0 if action == correct[self.index] else 0.0

        self.index += 1
        done = self.index >= len(self.emails)

        next_state = None if done else self.emails[self.index]

        return next_state, reward, done, {}

    def state(self):
        return self.emails[self.index]