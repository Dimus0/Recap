import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, String,Float,Date, func
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    avatar_url = Column(String, nullable=True)
    timezone = Column(String, default="UTC", nullable=True)
    created_at = Column(DateTime(timezone=True),nullable=False,server_default=func.now())

    notes = relationship("Note", back_populates="user", cascade="all, delete-orphan")
    summaries = relationship("Summary", back_populates="user", cascade="all, delete-orphan")
    integrations = relationship("Integration", back_populates="profile", cascade="all, delete-orphan")
    teams = relationship("Team", back_populates="owner", cascade="all, delete-orphan")
    team_memberships = relationship("TeamMembers", back_populates="user", cascade="all, delete-orphan")
   