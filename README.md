# LangGraph Agent Pipeline with Streamlit and Google Gemini

This project demonstrates a simple autonomous agentic workflow built using LangGraph, powered by Google Gemini, and presented with a user-friendly interface using Streamlit. The agent follows a basic Plan -> Execute -> Reflect loop to tackle user queries.

## Features

* **Web User Interface:** Interactive web application built with Streamlit.
* **Agentic Workflow:** Implements a Plan, Execute, and Reflect cycle using LangGraph.
* **Google Gemini Integration:** Leverages the Gemini Pro model for planning, task execution simulation, and reflection.
* **Dynamic Planning:** The agent generates a step-by-step plan based on the user's query.
* **Simulated Execution:** Tasks are "executed" by prompting the LLM, simulating tool use or information gathering.
* **Reflection and Revision:** The agent reflects on the executed tasks and their results, potentially revising the plan if needed.
* **Session Management:** Uses Streamlit's session state to persist inputs and API key.
* **API Key Handling:** Supports loading the Google API key from an environment variable (`.env` file) or via a text input in the UI.

## Prerequisites

* Python 3.7 or higher
* A Google Cloud account with access to the Gemini API. You can get an API key from the [Google AI Studio](https://aistudio.google.com/app/apikey).

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/PunVas/ATGTask1.git
    cd <repo_dir>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**
    * On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    * On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```

4.  **Install dependencies:**
    Create a `requirements.txt` file in the root directory of the project with the following content:
    ```
    streamlit>=1.20
    google-generativeai>=0.3
    langgraph>=0.0.30
    python-dotenv>=1.0
    ```
    Then, install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

You need to provide your Google Gemini API Key. You can do this in one of two ways:

1.  **Using a `.env` file (Recommended):**
    * Create a file named `.env` in the root directory of the project.
    * Add the following line to the `.env` file, replacing `YOUR_API_KEY_HERE` with your actual API key:
        ```env
        GOOGLE_API_KEY=YOUR_API_KEY_HERE
        ```
    * The application will automatically load the key from this file when it starts.

2.  **Using the Streamlit UI:**
    * If no `.env` file is found or the `GOOGLE_API_KEY` variable is not set, the Streamlit application will display a text input field where you can paste your API key.

## How to Run

1.  Make sure your virtual environment is activated.
2.  Navigate to the project directory in your terminal.
3.  Run the Streamlit application (assuming your main script is named `app.py`):
    ```bash
    streamlit run app.py
    ```
4.  Your web browser should open automatically to the Streamlit app. If not, open your browser and go to `http://localhost:8501`.

## How it Works

The application uses LangGraph to orchestrate the following state machine:

1.  **Plan:** Takes the user's query and uses Gemini to break it down into a list of sequential tasks.
2.  **Execute:** Takes the next task from the plan and uses Gemini to simulate performing that task, generating a "result".
3.  **Reflect:** Reviews the results of the executed tasks and the remaining plan. Uses Gemini to decide if the plan needs modification based on progress and results. It can output "DONE" if the goal seems achieved or propose a revised list of remaining tasks.
4.  **Conditional Decision:** Based on the Reflection output (is it "DONE"?) and the number of reflection loops completed (has it reached the max?), the graph decides whether to loop back to the **Execute** step (if the plan was revised or tasks remain) or end the process.

This loop continues until the reflection indicates the task is "DONE" or the maximum number of reflection cycles is reached. Streamlit provides the interactive front-end to input the query and display the pipeline's progress and final output.

## Contributing

Feel free to fork the repository and contribute!

## License

This project is licensed under the MIT License - see the `LICENSE` file (create this file separately if you wish to include one) for details.

## Attribution

* Built with [LangChain/LangGraph](https://github.com/langchain-ai/langgraph)
* Powered by [Google Gemini API](https://ai.google.dev/models/gemini)
* Frontend using [Streamlit](https://streamlit.io/)
* Environment variables handled by [python-dotenv](https://github.com/theskumar/python-dotenv)

---
