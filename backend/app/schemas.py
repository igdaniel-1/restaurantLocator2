from pydantic import BaseModel


class Origin(BaseModel):
    lat: float
    lng: float


class NearbyRestaurant(BaseModel):
    id: int
    name: str
    address: str
    rating: float | None
    rating_count: int | None
    price_level: str
    lat: float
    lng: float
    distance_m: int


class NearbyResponse(BaseModel):
    origin: Origin
    results: list[NearbyRestaurant]