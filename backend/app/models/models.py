from app.db.session import Base

# 2. Імпортуємо ВСІ ваші моделі з окремих файлів
from app.models.profiles import Profile
from app.models.teams import Team, TeamMembers
from app.models.notes import Note
from app.models.summaries import Summary
from app.models.team_digests import TeamDigest
from app.models.integrations import Integration
from app.models.note_embeddings import NoteEmbedding

# 3. (Опціонально) Оголошуємо __all__, щоб явно вказати, що саме експортує цей модуль
__all__ = [
    "Base",
    "Profile",
    "Team",
    "TeamMembers",
    "Note",
    "Summary",
    "TeamDigest",
    "Integration",
    "NoteEmbedding",
]