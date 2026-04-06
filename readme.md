---
title: Nexus Email Sentinel
emoji: 🛡️
sdk: docker
app_port: 7860
pinned: true
---

# 🛡️ Nexus Email Sentinel: Advanced OpenEnv Benchmark

**Nexus Email Sentinel** is a high-fidelity OpenEnv environment designed to benchmark LLM agents on **Temporal Reasoning** and **Information Conflict Resolution** within a simulated professional email workflow.

Unlike static benchmarks, Nexus requires agents to cross-reference multiple threads to identify the most current "ground truth" in rapidly changing scenarios.

---

## 🎯 The Challenge: Temporal Reasoning
In real-world business, information is fluid. A meeting time might change three times in ten minutes. 
*   **The Problem:** Most agents latch onto the *first* piece of information they see.
*   **Our Solution:** Nexus provides "Hard" tasks where the agent must ignore outdated instructions and identify the final state of a thread to succeed.

---

## 🚀 Environment Specifications


| Feature | Specification |
| :--- | :--- |
| **Framework** | OpenEnv v1.0 |
| **Tasks** | 3 (Easy, Medium, Hard) |
| **State Space** | Pydantic-validated JSON |
| **Action Space** | Categorize, Draft, Delete |
| **Grading** | Deterministic with Partial Rewards |

---

## 🛠️ Tasks & Grading Logic

### 1. Phish Detection (Easy)
*   **Goal:** Identify a "Security" email that is actually a phishing attempt.
*   **Win Condition:** Correct `email_id` + `delete` action.

### 2. Thread Consolidation (Medium)
*   **Goal:** Summarize a thread with three participants.
*   **Win Condition:** Inclusion of specific keywords from all participants.

### 3. The "Moving Target" (Hard)
*   **Goal:** Extract the *final* agreed-upon time from a 5-email chain where plans change in every message.
*   **Win Condition:** Exact string match of the final timestamp.

---

## 🔧 Installation & Validation

### Local Development
```bash
# Clone the repository
git clone https://huggingface.co
cd email-assistant-openenv

# Install dependencies
pip install -r requirements.txt

# Run the OpenEnv server
uvicorn app:app --host 0.0.0.0 --port 7860

# Running the Baseline
python inference.py

```
### 📊 Evaluation Format
Nexus outputs logs in the strict OpenEnv format for seamless integration with leaderboards:
[START] task=<name> env=Nexus model=<model>
[STEP] step=<n> action=<cmd> reward=<0.0-1.0> done=<bool>
[END] success=<bool> steps=<n> rewards=<list>


### ⚖️ License
This environment is released under the MIT License for the Meta PyTorch OpenEnv Hackathon 2026.