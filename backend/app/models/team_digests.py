import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, Date, UniqueConstraint, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.db.session import Base

class TeamDigest(Base):
    __tablename__ = "team_digests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    team_id = Column(UUID(as_uuid=True), ForeignKey("teams.id", ondelete="CASCADE"), nullable=False)
    period_start = Column(Date, nullable=False)
    period_end = Column(Date, nullable=False)
    content = Column(JSONB, nullable=True) # JSONB
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    team = relationship("Team", back_populates="digests")

    __table_args__ = (
        UniqueConstraint("team_id", "period_start", "period_end", name="uq_team_digest_period"),
    )