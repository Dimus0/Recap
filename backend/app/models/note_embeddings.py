import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from app.db.session import Base

class NoteEmbedding(Base):
    __tablename__ = "note_embeddings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    note_id = Column(UUID(as_uuid=True), ForeignKey("notes.id", ondelete="CASCADE"), nullable=False)
    embedding_vector = Column(Vector(1536), nullable=False)  # розмірність під вашу модель ембедінгів
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    note = relationship("Note", back_populates="embeddings")