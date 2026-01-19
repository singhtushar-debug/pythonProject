## Simple FastApi CRUD app

A learning project that includes CRUD(Create , Read , Update , Delete) APIs built with **FastAPi** and managed with **uv**.

## Tech Stack
   * **FastAPI**: Asynchronous web framework.
   * **Pydantic**: Data validation.
   * **uv**: Modern Python package manager.

## Requirements
   * **Python 3.11+**.
   * **uv**: If not installed,run: `pip install uv`.

## Installation & Setup
  * **Clone the repository**:

     **Run:**  `git clone https://github.com/singhtushar-debug/pythonProject.git `

     **Run:**  `cd pythonPorject`

  * **Sync dependencies:**

    **Run:** `python -m uv sync`

  * **How to run:**

    **Run:**  `python -m uv run uvicorn main:app --reload`

    **The server will start at:** `http://127.0.0.1:8000`


## API documentation
Once the server is running,you can access the interactive documentation to test the CRUD endpoints:

  * **Swagger UI**: `http://127.0.0.1:8000/docs`


        


