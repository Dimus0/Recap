import uuid
from sqlalchemy import FLOAT, UUID, Column, DateTime, ForeignKey, String,Float,Date, func, ARRAY
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base
from pgvector.sqlalchemy import Vector


class NoteEmbedding(Base):
    __tablename__ = "note_embeddings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    note_id = Column(UUID(as_uuid=True), ForeignKey("notes.id", ondelete="CASCADE"), nullable=False)
    embedding_vector = Column(ARRAY(FLOAT), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    note = relationship("Note", back_populates="embeddings")