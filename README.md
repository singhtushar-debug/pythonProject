## Simple FastApi CRUD app

A learning project that includes CRUD(Create , Read , Update , Delete) APIs built with **FastAPi** and managed with **uv**.

## Tech Stack
   * **FastAPI**: Asynchronous web framework.
   * **Pydantic**: Data validation.
   * **uv**: Modern Python package manager.
   * **PostgreSQL**: A relational database.

## Requirements
   * **Python 3.14+**.
   * **uv**: If not installed,run: `pip install uv`.

## Installation & Setup
  * **Clone the repository**:

     **Run:**  `git clone https://github.com/singhtushar-debug/pythonProject.git `

     **Run:**  `cd pythonProject`

  * **Sync dependencies:**

    **Run:** `python -m uv sync`

  * **How to run:**

    **Run:**  `python -m uv run uvicorn main:app --reload`

    **The server will start at:** `http://127.0.0.1:8000`

## Database setup
This project requires a **PostgreSQL** instance.
### 1. Local Installation
   Before running the application, you need to have a **PostgreSQL** instance ready.
   * **Step 1**: Install PostgreSQL from the [official website](https://www.postgresql.org/download/).
   * **Step 2**: Open your terminal and create a new database :
         ```
            CREATE DATABASE product_inventory;
         ```

### 2. Setup .env file
Create a `.env` file in the root directory :
```
   DATABASE_URL = postgresql+asyncpg://<username>:<password>@localhost:5432/<databasename>
```

## API documentation
Once the server is running,you can access the interactive documentation to test the CRUD endpoints:

  * **Swagger UI**: `http://127.0.0.1:8000/docs`


        


