# How to test it?

## Backend

```bash
cd backend
# and
pipenv shell
# and
pipenv install
# and
python manage.py runserver
```

## Backend Test

```bash
cd backend
# and
pytest
```

## Backend Coverage

```bash
cd backend
# and
pytest --cov
```

## Frontend

```bash
cd frontend
# and
yarn install
# and
yarn build
# and
yarn start
```

## Frontend Test

```bash
yarn cypress:run
```
