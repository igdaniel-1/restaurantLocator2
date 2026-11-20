import argparse

from geoalchemy2 import WKTElement
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import insert

from .db import SessionLocal, init_db
from .google import search_nearby
from .models import Restaurant


def main() -> None:
    parser = argparse.ArgumentParser(description='Import restaurants around a lat/lng')
    parser.add_argument('lat', type=float)
    parser.add_argument('lng', type=float)
    # radius is in meters
    parser.add_argument('--radius', type=float, default=2000)
    args = parser.parse_args()

    init_db()
    places = search_nearby(args.lat, args.lng, args.radius)

    with SessionLocal() as db:
        for p in places:
            lat = p['location']['latitude']
            lng = p['location']['longitude']
            row = {
                'place_id': p['id'],
                'name': p['displayName']['text'],
                'address': p.get('formattedAddress', ''),
                'latitude': lat,
                'longitude': lng,
                'location': WKTElement(f'POINT({lng} {lat})', srid=4326),
                'rating': p.get('rating'),
                'rating_count': p.get('userRatingCount'),
                'price_level': p.get('priceLevel', ''),
                'cuisine_types': p.get('types', []),
                'last_synced': func.now(),
            }
            stmt = insert(Restaurant).values(**row)
            stmt = stmt.on_conflict_do_update(
                index_elements=['place_id'],
                set_={k: v for k, v in row.items() if k != 'place_id'},
            )
            db.execute(stmt)
        db.commit()

    print(f'Imported {len(places)} restaurants')


if __name__ == '__main__':
    main()