# 🚀 AutoCode Review & Optimizer

An intelligent, agent-powered system designed to automatically analyze, review, and suggest optimizations for your Python source code. Built using **Streamlit** for the UI and **CrewAI** for the underlying multi-agent workflow.

## ✨ Features

* **Automated Code Analysis:** Uses static analysis tools (like Pylint) to check for syntax errors, style violations, and potential bugs.
* **Intelligent Code Review:** AI agents assess code quality, adherence to best practices, and security risks.
* **Performance Optimization Suggestions:** Identifies inefficient code patterns (e.g., costly loops, redundant calculations) and proposes optimized alternatives.
* **Comprehensive Output Report:** Generates a structured report detailing original issues, optimized code snippets, and a summary of performance gains.
* **Streamlit User Interface:** Provides a simple, interactive web interface for uploading code and viewing results.

## 🛠️ Installation

### Prerequisites

* Python 3.8+
* A valid **OpenAI API Key** (or another large language model API key supported by CrewAI).

### 1. Clone the repository

```bash
git clone <repository-link-here>
cd AutoCode_Review_Optimizer
```

### 2. Set up the Virtual Environment (Recommended)

```bash
python -m venv venv
# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```
### 3. Install Dependencies
Install all required packages from the ```bash requirements.txt ``` file (you will need to create this file containing streamlit, crewai, crewai_tools, pydantic, python-dotenv, etc.).
