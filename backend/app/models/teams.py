import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey,Enum as SQLEnum, String,func
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.models.enums import RoleEnum

class Team(Base):
    __tablename__ = "teams"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    owner = relationship("Profile", back_populates="teams")
    digests = relationship("TeamDigest", back_populates="team", cascade="all, delete-orphan")
    members = relationship("TeamMembers", back_populates="team", cascade="all, delete-orphan")

class TeamMembers(Base):
    __tablename__ = "team_members"

    team_id = Column(UUID(as_uuid=True), ForeignKey("teams.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    role = Column(SQLEnum(RoleEnum), default=RoleEnum.MEMBER, nullable=False)
    joined_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    team = relationship("Team", back_populates="members")
    user = relationship("Profile", back_populates="team_memberships")