import uuid
from sqlalchemy import UUID, Column, DateTime, Enum as SQLEnum, ForeignKey, String,Float,Date, Text, func
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base
from app.models.enums import NoteSourceEnum

class Note(Base):
    __tablename__ = "notes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    source = Column(SQLEnum(NoteSourceEnum), default=NoteSourceEnum.MANUAL, nullable=False)
    source_ref = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    user = relationship("Profile", back_populates="notes")
    embeddings = relationship("NoteEmbedding", back_populates="note", cascade="all, delete-orphan")