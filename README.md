#  AutoCode Review & Optimizer

An intelligent, agent-powered system designed to automatically analyze, review, and suggest optimizations for your Python source code. Built using **Streamlit** for the UI and **CrewAI** for the underlying multi-agent workflow.

##  Features

* **Automated Code Analysis:** Uses static analysis tools (like Pylint) to check for syntax errors, style violations, and potential bugs.
* **Intelligent Code Review:** AI agents assess code quality, adherence to best practices, and security risks.
* **Performance Optimization Suggestions:** Identifies inefficient code patterns (e.g., costly loops, redundant calculations) and proposes optimized alternatives.
* **Comprehensive Output Report:** Generates a structured report detailing original issues, optimized code snippets, and a summary of performance gains.
* **Streamlit User Interface:** Provides a simple, interactive web interface for uploading code and viewing results.

##  Installation

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
Install all required packages from the ``` requirements.txt ``` file (you will need to create this file containing ```streamlit```, ```crewai```, ```crewai_tools```, ```pydantic```, ```python-dotenv```, etc.).

### 4. Configure Environment Variables
Create a file named ```.env``` in the root directory and add your API key:
```bash
# Set the LLM model to use with CrewAI. This points to your local Ollama instance.
OPENAI_API_BASE=http:****
OPENAI_MODEL_NAME=codellama:7b
```
## Usage

### Running the Application
Ensure your virtual environment is active, and then run the Streamlit application:

```bash
streamlit run streamlit_app.py
```

## Workflow

**Upload**: In the Streamlit UI, upload the Python file (.py) you wish to review.

**Process**: Click the "Run Review and Optimization" button.

**Review**: The CrewAI agents will execute the workflow: read the file, run Pylint analysis, review the code, and propose optimizations.

**View Results**: The final comprehensive report will be displayed in the Streamlit interface.

