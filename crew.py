import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai.process import Process
from tools import FileReadTool, PylintAnalysisTool, OptimizationKnowledgeTool

load_dotenv()

# --- Initialize Tools ---
file_reader = FileReadTool()
pylint_analyzer = PylintAnalysisTool()
knowledge_tool = OptimizationKnowledgeTool()

# --- Define Agents ---
class CodeReviewAgents:
    def code_analyst(self):
        return Agent(
            role='The Code Analyst',
            goal="Read the entire code file and generate a detailed report from Pylint static analysis.",
            backstory="You are a meticulous senior software engineer specializing in diagnostics and linting. Your job is to objectively scan the code and provide raw data on its current state.",
            verbose=True,
            allow_delegation=False,
            tools=[file_reader, pylint_analyzer],
            llm_model=os.getenv("OPENAI_MODEL_NAME")
        )

    def optimization_engineer(self):
        return Agent(
            role='The Optimization Engineer',
            goal="Suggest specific, actionable improvements for code performance, security, and best practices based on the Analyst's report.",
            backstory="You are a performance optimization expert. You take raw diagnostic data and turn it into clear, well-explained solutions and refactoring suggestions.",
            verbose=True,
            allow_delegation=True,
            tools=[knowledge_tool],
            llm_model=os.getenv("OPENAI_MODEL_NAME")
        )

    def technical_writer(self):
        return Agent(
            role='The Technical Writer',
            goal="Compile all analysis and suggestions into a final, professional, well-structured Markdown report for the user.",
            backstory="You are a technical editor who ensures all complex technical details are presented clearly and concisely in a final deliverable.",
            verbose=True,
            allow_delegation=False,
            llm_model=os.getenv("OPENAI_MODEL_NAME")
        )

# --- Define Tasks and Crew ---
class CodeReviewTasks:
    def analyze_code(self, agent: Agent, file_path: str):
        return Task(
            description=f"1. Use the File Reader Tool to read the contents of '{file_path}'. 2. Use the Pylint Static Analysis Tool to run a full linting check on the file. 3. Summarize the initial findings and the Pylint report.",
            agent=agent,
            expected_output="A summary of the code's purpose and the full, raw Pylint output."
        )

    def optimize_suggestions(self, agent: Agent, file_path: str):
        return Task(
            description=f"Using the Code Analyst's report and the Optimization Knowledge Tool, generate a list of 5-10 specific, prioritized code improvements for '{file_path}'. Suggestions must cover performance, security, and Python best practices. For each suggestion, cite the relevant best practice from the tool if available.",
            agent=agent,
            expected_output="A markdown-formatted list of actionable optimization suggestions with explanations."
        )

    def generate_report(self, agent: Agent, file_path: str):
        return Task(
            description="Take the *entire* process output (Code Analyst's summary and Pylint report, and the Optimization Engineer's suggestions) and compile them into a single, cohesive, professional Markdown document. The final report MUST include the following sections: '1. Project Overview', '2. Static Analysis Summary (from Pylint)', '3. Detailed Optimization Suggestions', and '4. Next Steps & Summary'.",
            agent=agent,
            context=[self.analyze_code, self.optimize_suggestions],
            expected_output="A single, detailed, professional Markdown report.",
            # This task's output is the final answer
            is_final_task=True
        )

# --- Main Execution Function ---
def run_crew(file_path: str):
    agents = CodeReviewAgents()
    tasks = CodeReviewTasks()

    # Define Agents
    analyst = agents.code_analyst()
    engineer = agents.optimization_engineer()
    writer = agents.technical_writer()

    # Define Tasks
    analyze_task = tasks.analyze_code(analyst, file_path)
    optimize_task = tasks.optimize_suggestions(engineer, file_path)
    report_task = tasks.generate_report(writer, file_path)

    # Instantiate the Crew
    project_crew = Crew(
        agents=[analyst, engineer, writer],
        tasks=[analyze_task, optimize_task, report_task],
        process=Process.sequential,  # Agents work in a defined sequence
        verbose=2, # Show detailed progress
    )

    # Kickoff the process
    result = project_crew.kickoff()
    return result