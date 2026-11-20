import httpx

from .config import settings

PLACES_URL = 'https://places.googleapis.com/v1/places:searchNearby'
GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
FIELDS = ','.join([
    'places.id', 'places.displayName', 'places.formattedAddress',
    'places.location', 'places.rating', 'places.userRatingCount',
    'places.priceLevel', 'places.types',
])

# print('FIELDS:',FIELDS)

# radius is in meters
def search_nearby(lat: float, lng: float, radius: float) -> list[dict]:
    body = {
        'includedTypes': ['restaurant'],
        'maxResultCount': 20,
        'locationRestriction': {
            'circle': {
                'center': {'latitude': lat, 'longitude': lng},
                'radius': radius,
            }
        },
    }
    headers = {
        'X-Goog-Api-Key': settings.google_maps_api_key,
        'X-Goog-FieldMask': FIELDS,
    }
    resp = httpx.post(PLACES_URL, json=body, headers=headers, timeout=20)

    # tester
    print(resp.text)


    resp.raise_for_status()
    return resp.json().get('places', [])



def geocode(address: str) -> tuple[float, float] | None:
    resp = httpx.get(
        GEOCODE_URL,
        params={'address': address, 'key': settings.google_maps_api_key},
        timeout=10,
    )
    data = resp.json()
    if data.get('status') != 'OK':
        return None
    loc = data['results'][0]['geometry']['location']
    return loc['lat'], loc['lng']