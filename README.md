# 📧 Email Assistant OpenEnv Environment

## 🚀 Overview

**Email Assistant OpenEnv** is a real-world simulation environment designed to train and evaluate AI agents on **email triage tasks** — a critical workflow in modern digital communication.

This environment models how humans:

* classify emails (spam vs important)
* prioritize tasks
* make quick decisions under limited context

Unlike toy environments, this project focuses on **practical, real-world usability**, making it suitable for evaluating intelligent agents in productivity systems.

---

## 🎯 Motivation

Email overload is a real problem in both personal and professional settings. Efficiently handling emails requires:

* understanding intent
* identifying urgency
* filtering noise (spam)

This environment provides a **structured benchmark** for training AI agents to perform these tasks, bridging the gap between research and real-world applications.

---

## 🧠 Environment Design

The environment follows the **OpenEnv specification**, implementing:

* `reset()` → initializes a new episode
* `step(action)` → processes an action and returns result
* `state()` → returns current environment state

Each episode consists of a sequence of emails that the agent must process.

---

## 📥 Observation Space

The agent receives:

```json
{
  "email": "string",
  "step_count": "int"
}
```

* `email`: current email content
* `step_count`: current step in episode

---

## ⚡ Action Space

The agent can take one of the following actions:

* `"spam"` → mark email as spam
* `"important"` → mark email as important
* `"reply"` → generate a response (advanced extension)

---

## 🎯 Tasks (Easy → Medium → Hard)

### 🟢 Task 1 — Easy: Spam Detection

* Identify obvious spam emails
* Example: *"Win a free iPhone!!!"*
* Expected output: `"spam"`

---

### 🟡 Task 2 — Medium: Priority Classification

* Classify emails based on urgency
* Example: *"Submit report by EOD"*
* Expected output: `"important"`

---

### 🔴 Task 3 — Hard: Contextual Understanding

* Interpret nuanced or ambiguous emails
* Example: *"Client escalation — urgent response needed"*
* Requires reasoning and prioritization

---

## 🧪 Reward Function

The environment uses a **graded reward system**:

| Condition                      | Reward  |
| ------------------------------ | ------- |
| Correct classification         | 1.0     |
| Partially correct / acceptable | 0.3–0.5 |
| Incorrect classification       | 0.0     |

### 💡 Key Features:

* Provides **dense feedback** (not just binary)
* Encourages progressive improvement
* Penalizes incorrect decisions

---

## 🧪 Grading System

Each task includes a **deterministic grader**:

* Outputs score in **range [0.0, 1.0]**
* Fully reproducible
* Ensures fair evaluation across agents

---

## 🤖 Baseline Agent

A simple rule-based agent is provided via `inference.py`.

### Behavior:

* Detects keywords like `"free"` → marks as spam
* Otherwise → marks as important

This serves as a **baseline benchmark** for evaluation.

---

## 📊 Example Output Logs

```
[START] task=email env=openenv model=baseline
[STEP] step=1 action=important reward=1.00 done=false error=null
[STEP] step=2 action=spam reward=1.00 done=false error=null
[STEP] step=3 action=important reward=1.00 done=true error=null
[END] success=true steps=3 rewards=1.00,1.00,1.00
```

---

## 🐳 Setup & Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/email-assistant-openenv
cd email-assistant-openenv
```

---

### 2. Run with Docker

```bash
docker build -t email-env .
docker run email-env
```

---

### 3. Run Locally

```bash
pip install pydantic
python inference.py
```

---

## ☁️ Deployment

This environment is deployed using:

👉 Hugging Face Spaces

* Fully containerized
* Supports OpenEnv validation
* Responds to `/reset` and `/step` endpoints

---

## 📈 Baseline Performance

| Task   | Score |
| ------ | ----- |
| Easy   | 1.0   |
| Medium | 1.0   |
| Hard   | 0.8   |

---

## 🏗️ Project Structure

```
.
├── env/
│   ├── environment.py
│   ├── models.py
│   ├── tasks.py
│   ├── grader.py
│
├── inference.py
├── openenv.yaml
├── Dockerfile
├── README.md
```

---

## 💡 Design Highlights

* ✅ Real-world applicability (email triage)
* ✅ Clean environment abstraction
* ✅ Deterministic grading system
* ✅ Dense reward shaping
* ✅ Lightweight and reproducible

---

## 🚀 Future Improvements

* Multi-label classification (priority levels)
* Response generation using LLMs
* Threaded email conversations
* User-specific personalization

---

## 👨‍💻 Team

* Shashank Padmasale (Team Lead)
* Team Members

---

## 🏁 Conclusion

This project demonstrates how **OpenEnv can be used to model real-world workflows**, enabling the development of intelligent agents that go beyond toy problems and into practical applications.

---
