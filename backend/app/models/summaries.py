import uuid
from sqlalchemy import UUID, Boolean, Column, DateTime, ForeignKey, String,Date, Text, UniqueConstraint, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.db.session import Base

class Summary(Base):
    __tablename__ = "summaries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)
    period_start = Column(Date, nullable=False)
    period_end = Column(Date, nullable=False)
    highlight = Column(Text, nullable=True)
    decision = Column(Text, nullable=True)
    blockers = Column(Text, nullable=True)
    next_steps = Column(Text, nullable=True)
    raw_llm_output = Column(JSONB, nullable=True) # JSONB

    is_public = Column(Boolean, nullable=False, default=False)
    public_slug = Column(String, nullable=True, unique=True)

    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("Profile", back_populates="summaries")

    __table_args__ = (
        UniqueConstraint("user_id", "period_start", "period_end", name="uq_user_summary_period"),
    )

    