# NASA

## FastAPI NASA Project

This project is a FastAPI-based application for managing users and fetching data from various NASA APIs, including NeoWs, Donki, and TLE.

## Project Structure

```
.
├── LICENSE
├── README.md
├── alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── 7ded8cafcd6a_.py
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── donki.py
│   │   ├── neows.py
│   │   ├── tle.py
│   │   └── users.py
│   └── schemas.py
├── requirements.txt
├── setup.cfg
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_1_database.py
    ├── test_2_schemas.py
    ├── test_3_models.py
    ├── test_4_users.py
    ├── test_5_dependencies.py
    ├── test_6_NASA.py
    └── test_7_crud.py
```

## API Endpoints

### Users
- `POST /users/` - Create User
- `GET /users/{user_id}` - Read User
- `PUT /users/{user_id}` - Update User
- `DELETE /users/{user_id}` - Delete User

### NeoWs
- `GET /neows/` - Get Neows

### Donki
- `GET /donki/` - Get Donki

### TLE
- `GET /tle/` - Search TLE By Name
- `GET /tle/{id}` - Get TLE By Id

## Configuration

This project requires a `.env` file to configure environment variables. Create a `.env` file in the root directory of the project with the following variables:

```
TOKEN=
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
TESTING={True or False}
```

## Installation and Setup

Follow these steps to set up and run the project:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/argunv/NASA_FastAPI.git
   cd NASA_FastAPI
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Ensure your PostgreSQL database is running and configured with the credentials specified in your `.env` file. Then, apply the database migrations:

   ```sh
   alembic upgrade head
   ```

5. **Run the application:**

   ```sh
   uvicorn app.main:app --reload
   ```

6. **Run tests:**

   - Edit `TESTING=True` at `.env` and create `test.db` using:
   ```sh
   python3 app/models.py
   ```
   ```sh
   pytest
   ```

## Project Components

- **Alembic**: Used for database migrations.
- **FastAPI**: The web framework used to build the application.
- **PostgreSQL**: The database used to store data.
- **Pytest**: Used for testing the application.

## API Routes

The project includes several routes for interacting with NASA data:

- **DONKI** (`donki.py`): Routes related to the NASA DONKI (Space Weather Database Of Notifications, Knowledge, Information) API.
- **NeoWs** (`neows.py`): Routes for NASA's Near Earth Object Web Service.
- **TLE** (`tle.py`): Routes for obtaining Two-Line Element Set data.
- **Users** (`users.py`): Routes for user management.

## Contributing

If you wish to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [httpx](https://www.python-httpx.org/)
