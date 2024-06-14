# NASA

## FastAPI NASA Project

This project is a FastAPI-based application for managing users and fetching data from various NASA APIs, including NeoWs, Donki, and TLE.

### Project Structure

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
│   ├── schemas.py
│   └── test.db
├── requirements.txt
├── setup.cfg
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_donki.py
    ├── test_neows.py
    ├── test_tle.py
    └── test_users.py
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

## Testing

1. To run tests:
    ```bash
    pytest
    ```

2. To ensure a clean state, tests automatically clear the database after each run.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [httpx](https://www.python-httpx.org/)
