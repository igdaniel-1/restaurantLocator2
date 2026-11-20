# Restaurant Locator v2

## New and improved locator
New locator testing the new Google Places API instead of Maps. Evaluating location proximity runtime latency.

This is an improved version of my [v1](https://github.com/igdaniel-1/simpleSearchBar-GoogleMapsAPI) (Docker X NodeJS + Google Maps API.)

## Execution instructions
Navigate to /backend 

```cd backend```

Launch the Python VM

```.\.venv\Scripts\Activate.ps1```

(First Run Only) Download:
FastAPI, SQLAlchemy, GeoAlchemy2, httpx, pydantic-settings

```pip install fastapi 'uvicorn[standard]' sqlalchemy 'psycopg[binary]' geoalchemy2 httpx pydantic-settings```

## Test Google Places API
Change the region by updating the lat/long coordinates. Change the search radius by updating the final integer (measured in meters), or leave empty to use the default radius. Default radius is set to 2000 meters if not specified.

This site can be useful for converting addresses into Lat/Long [coordinates](https://www.latlong.net/).


### Test Cases
Lower Manhattan: ```python -m app.import_restaurants 40.7127 -74.0059 --radius 2000```

Midtown Manhattan: ```python -m app.import_restaurants 40.7547 -73.9853 --radius 1000```

Downtown Brooklyn: ```python -m app.import_restaurants 40.6980 -73.9871 --radius 2000```

Fort Greene Park: ```python -m app.import_restaurants 40.6897 -73.9734 --radius 500```

