## Development

Install virtual environment and dependencies: 
```bash
python3 -m venv env
env/bin/pip install -r requirements.txt
env/bin/pip install -r requirements.tests.txt
```

Migrate database to initial state:
```bash
alembic upgrade head
```

## Tests
To run tests use `./run_tests.sh`
