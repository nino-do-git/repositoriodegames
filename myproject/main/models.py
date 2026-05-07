from django.db import models

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, JSON
from app.database import Base
from datetime import datetime


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    short_description = Column(String)
    description = Column(Text)
    developer = Column(String)
    genre = Column(String)
    platform = Column(String, default="Windows, Linux, macOS")
    python_version = Column(String, default="3.x")
    pygame_version = Column(String, default="2.x")
    thumbnail = Column(String, nullable=True)
    screenshots = Column(JSON, default=list)
    download_file = Column(String, nullable=True)
    download_url = Column(String, nullable=True)
    source_code_url = Column(String, nullable=True)
    instructions = Column(Text, nullable=True)
    featured = Column(Boolean, default=False)
    download_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
