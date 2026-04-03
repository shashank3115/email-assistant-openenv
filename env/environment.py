from env.models import Observation, Action, Reward

class EmailEnv:
    def __init__(self):
        self.emails = [
            "Meeting at 5pm",
            "Win money now!!!",
            "Submit assignment"
        ]
        self.index = 0

    def reset(self):
        self.index = 0
        return Observation(email=self.emails[self.index], step_count=0)

    def step(self, action: Action):
        correct = ["important", "spam", "important"]

        reward = 1.0 if action.label == correct[self.index] else 0.3

        self.index += 1
        done = self.index >= len(self.emails)

        obs = None if done else Observation(
            email=self.emails[self.index],
            step_count=self.index
        )

        return obs, reward, done, {}

    def state(self):
        return self.emails[self.index]