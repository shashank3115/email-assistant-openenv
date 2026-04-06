from models import Action, Observation

class EmailSentinelEnv:
    def __init__(self):
        self.tasks = {
            "easy_phish": {
                "goal": "Identify and delete the phishing email.",
                "emails": [
                    {"id": 1, "sender": "security@bank.co", "body": "Click here to reset pass", "label": "spam"},
                    {"id": 2, "sender": "mom@home.com", "body": "Dinner at 5?", "label": "inbox"}
                ],
                "target_id": 1, "correct_action": "delete"
            },
            "hard_temporal": {
                "goal": "What time is the meeting finally set for? Respond with the time.",
                "emails": [
                    {"id": 10, "sender": "boss@co.com", "body": "Meeting at 2pm."},
                    {"id": 11, "sender": "boss@co.com", "body": "Wait, let's do 4pm instead."},
                    {"id": 12, "sender": "boss@co.com", "body": "Actually, 3pm works best for all."}
                ],
                "target_id": 12, "correct_payload": "3pm"
            }
        }
        self.reset()

    def reset(self, task_id="easy_phish"):
        self.active_task = self.tasks.get(task_id, self.tasks["easy_phish"])
        self.done = False
        return Observation(
            inbox=self.active_task["emails"],
            last_action_status="Initialized",
            current_task_goal=self.active_task["goal"]
        )

    def step(self, action: Action):
        reward = 0.0
        # Winning Logic: Partial Rewards
        if action.email_id == self.active_task["target_id"]:
            reward += 0.4 # Reward for identifying the correct email
            
            if "correct_action" in self.active_task and action.call == self.active_task["correct_action"]:
                reward += 0.6
            elif "correct_payload" in self.active_task and self.active_task["correct_payload"] in action.payload:
                reward += 0.6
        
        self.done = True
        obs = Observation(inbox=[], last_action_status="Success", current_task_goal="Finished")
        return obs, round(reward, 2), self.done, {"final_score": reward}
