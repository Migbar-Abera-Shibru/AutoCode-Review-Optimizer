import streamlit as st
import os
import tempfile
from crew import run_crew

st.set_page_config(layout="wide", page_title="AutoCode Review & Optimizer")

def main():
    st.title("💡 AutoCode Review & Optimizer")
    st.subheader("Multi-Agent System for Code Quality and Performance")

    st.warning("Prerequisite: Ensure your local **Ollama** server is running and the `codellama:7b` model is downloaded.")
    
    st.markdown("""
    This system mimics a team of senior engineers to analyze, optimize, and document your Python codebase.
    
    * **The Code Analyst** scans the file and runs Pylint.
    * **The Optimization Engineer** suggests improvements and best practices.
    * **The Technical Writer** compiles the final, professional report.
    """)

    uploaded_file = st.file_uploader("Upload a Python file (`.py`) for review:", type="py")

    if uploaded_file is not None:
        # 1. Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_file_path = tmp_file.name
        
        st.success(f"File '{uploaded_file.name}' successfully uploaded and ready for analysis.")
        st.code(uploaded_file.getvalue().decode("utf-8"), language="python", label="Uploaded Code Preview")

        # 2. Run the Crew when the button is clicked
        if st.button("Start AutoCode Review"):
            with st.spinner("Reviewing in progress... The agent team is collaborating..."):
                try:
                    # Run the multi-agent system
                    final_report = run_crew(temp_file_path)
                    
                    st.header("✅ Final Code Review Report")
                    # Display the final report in a beautiful Markdown format
                    st.markdown(final_report)
                    
                except Exception as e:
                    st.error(f"An error occurred during the Crew execution. Double-check your Ollama setup and `.env` file.")
                    st.exception(e)
                finally:
                    # 3. Clean up the temporary file
                    os.unlink(temp_file_path)

if __name__ == "__main__":
    # Ensure environment variables are loaded for CrewAI
    from dotenv import load_dotenv
    load_dotenv()
    
    # Run the main Streamlit function
    main()