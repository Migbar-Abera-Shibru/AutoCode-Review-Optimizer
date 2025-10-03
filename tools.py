import os
import subprocess
from crewai_tools import BaseTool
from pydantic import BaseModel, Field

# --- Tool 1: Reads a Code File ---
class FileReadTool(BaseTool):
    """A tool to safely read the content of a local file."""
    name: str = "File Reader Tool"
    description: str = "Useful for reading the content of a specified code file (e.g., 'main.py')."
    
    def _run(self, file_path: str) -> str:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            return f"Successfully read file content:\n```python\n{content}\n```"
        except FileNotFoundError:
            return f"Error: File not found at path {file_path}"
        except Exception as e:
            return f"Error reading file: {e}"

# --- Tool 2: Runs Pylint for Static Analysis ---
class PylintAnalysisTool(BaseTool):
    """A tool that executes Pylint for deep static code analysis."""
    name: str = "Pylint Static Analysis Tool"
    description: str = "Runs Pylint on a Python file to check for coding standards, errors, and complexity. The output is a detailed report."
    
    def _run(self, file_path: str) -> str:
        # Pylint is installed via requirements.txt
        try:
            # Run pylint as a subprocess and capture the output
            result = subprocess.run(
                ['pylint', file_path],
                capture_output=True,
                text=True,
                check=False # Do not raise error if linting issues are found
            )
            
            if result.stdout:
                return f"Pylint Analysis Complete. Results:\n{result.stdout}"
            else:
                return "Pylint ran, but returned no stdout. Check the file or pylint installation."
        except FileNotFoundError:
            return "Error: Pylint command not found. Ensure Pylint is installed."
        except Exception as e:
            return f"An unexpected error occurred during Pylint execution: {e}"

# --- Tool 3: Simulates Searching Best Practices (Free, Pre-canned knowledge) ---
class OptimizationKnowledgeTool(BaseTool):
    """A tool to query for known Python best practices and optimization techniques."""
    name: str = "Optimization Knowledgebase Tool"
    description: str = "Use this tool to look up specific best practices for Python coding, security, or performance, instead of using web search."
    
    def _run(self, query: str) -> str:
        # Simulate a free knowledge base lookup (in a real project, this would be a RAG or API call)
        knowledge_base = {
            "performance": "Optimization Tip: Use built-in functions (e.g., list comprehensions) instead of manual loops. Avoid unnecessary object creation. Profile before optimizing.",
            "security": "Security Tip: Never use the 'subprocess' module with unsanitized user input. Always use 'f-strings' safely, but prefer '.format()' for logging. Sanitize all inputs.",
            "type hinting": "Best Practice: Always use type hints (e.g., `def func(a: int) -> list[str]:`) for clarity and better static analysis. This improves maintainability.",
            "readability": "Best Practice: Follow PEP 8 standards. Keep functions short and focused. Use meaningful variable names."
        }
        
        # Simple keyword matching for demonstration
        for key, value in knowledge_base.items():
            if key in query.lower():
                return f"Found knowledge on '{key}': {value}"
        
        return "No specific knowledge found for this query, use general optimization knowledge."