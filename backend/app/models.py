from datetime import datetime

from geoalchemy2 import Geography
from sqlalchemy import DateTime, Float, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .db import Base


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id: Mapped[int] = mapped_column(primary_key=True)
    place_id: Mapped[str] = mapped_column(String(255), unique=True)
    name: Mapped[str] = mapped_column(String(255))
    address: Mapped[str] = mapped_column(String(500))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    location = mapped_column(Geography(geometry_type='POINT', srid=4326))  # spatially indexed
    rating: Mapped[float | None]
    rating_count: Mapped[int | None]
    price_level: Mapped[str] = mapped_column(String(50), default='')
    cuisine_types: Mapped[list] = mapped_column(JSONB, default=list)
    last_synced: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
)