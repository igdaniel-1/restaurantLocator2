# Restaurant Locator v2

## New and improved locator
New locator testing the new Google Places API instead of Maps. Evaluating location proximity runtime latency.

## Execution instructions
Navigate to /backend 

```cd backend```

Launch the Python VM

```.\.venv\Scripts\Activate.ps1```

(First Run Only) Download:
FastAPI, SQLAlchemy, GeoAlchemy2, httpx, pydantic-settings

```pip install fastapi 'uvicorn[standard]' sqlalchemy 'psycopg[binary]'```
```pip install 'psycopg[binary]' geoalchemy2 httpx pydantic-settings```
