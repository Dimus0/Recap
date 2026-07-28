from enum import Enum

class RoleEnum(str, Enum):
    OWNER = "owner"
    MANAGER = "manager"
    MEMBER = "member"

class NoteSourceEnum(str, Enum):
    MANUAL = "manual"
    SLACK = "slack"
    TASK_TRACKER = "task_tracker"
    CALENDAR = "calendar"

class IntegrationProviderEnum(str, Enum):
    SLACK = "slack"
    LINEAR = "linear"
    JIRA = "jira"
    TRELLO = "trello"
    GOOGLE_CALENDAR = "google_calendar"