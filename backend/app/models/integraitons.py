import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, Enum as SQLEnum, String,Float,Date, func
from sqlalchemy.orm import relationship
from app.db.session import Base
from sqlalchemy.dialects.postgresql import JSONB
from app.models.enums import IntegrationProviderEnum


class Integration(Base):
    __tablename__ = "integrations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    profile_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)
    provider = Column(SQLEnum(IntegrationProviderEnum), nullable=False)
    access_token = Column(String, nullable=False)  # Should be encrypted before storage
    refresh_token = Column(String, nullable=True)  # Should be encrypted before storage
    meta_data = Column(JSONB, nullable=True)  
    
    connected_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    profile = relationship("Profile", backref="integrations")