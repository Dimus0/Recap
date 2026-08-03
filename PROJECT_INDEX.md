# 📋 PROJECT INDEX & CONTEXT (Recap Project)

> **Призначення:** Цей файл зберігає повний індекс, структуру, статус та історію змін проекту **Recap**. Всі наступні сесії та промпти мають спочатку читати цей файл для швидкого розуміння архітектури та економії токенів, а після виконання завдань — оновлювати його (зміст, статус та Журнал змін з датою).

---

## 📌 Основна інформація
- **Назва проекту:** Recap (Recap for Teams)
- **Суть проекту:** AI B2B SaaS платформа для автоматичного збору нотаток, генерування індивідуальних тижневих підсумків (Summaries) та командних дайджестів (Team Digests).
- **Останнє оновлення:** `2026-08-03`

---

## 📑 Зміст (Table of Contents)
1. [Загальний стан та архітектура](#1-загальний-стан-та-архітектура)
2. [Карта файлів та директорій](#2-карта-файлів-та-директорій)
3. [Моделі даних (Database Models)](#3-моделі-даних-database-models)
4. [API Ендпоінти (Endpoints Status)](#4-api-ендпоінти-endpoints-status)
5. [Правила для Агента (Workflow & Token Saving)](#5-правила-для-агента-workflow--token-saving)
6. [Журнал змін (Changelog)](#6-журнал-змін-changelog)

---

## 1. 🏗 Загальний стан та архітектура

### Технологічний стек:
- **Backend:** Python 3.12+, FastAPI, Uvicorn, Pydantic v2, Pydantic-Settings
- **ORM / Database:** SQLAlchemy 2.0 (Async + `asyncpg`), PostgreSQL 16 (`pgvector/pgvector:pg16` у Docker), Alembic для міграцій
- **Auth & Security:** `fastapi-users`, `passlib[bcrypt]`, `pwdlib`, `python-jose`
- **AI & Vectors:** OpenAI API, `pgvector` (векторні ембедінги розмінності 1536)
- **Frontend:** React + Tailwind CSS (директорія `frontend/`, підготовка)
- **Запуск:** `docker-compose.yml` (БД PostgreSQL + pgvector), `uv run python main.py` або `uvicorn app.app:app --reload`

---

## 2. 📁 Карта файлів та директорій

```
recap-project/
├── .agents/
│   └── AGENTS.md                  # Системні інструкції агента для автоматичного використання PROJECT_INDEX.md
├── backend/
│   ├── .env                       # Конфігурація середовища backend (DATABASE_URL тощо)
│   ├── alembic.ini                # Налаштування Alembic
│   ├── alembic/                   # Міграції бази даних
│   │   ├── env.py                 # Асинхронний env.py для Alembic з підключеним Base
│   │   └── versions/
│   │       ├── 67fe673d8e3c_create_all_tables.py
│   │       └── adbbc2e35262_add_pgvector_extension_and_note_.py
│   └── app/
│       ├── __init__.py
│       ├── app.py                 # Головна точка входу FastAPI додатка (CORS, lifespan, OpenAPI)
│       ├── api/
│       │   └── v1/
│       │       └── endpoints/
│       │           ├── auth.py     # Endpoints аутентифікації (в розробці)
│       │           ├── notes.py    # Endpoints нотаток (в розробці)
│       │           ├── summaries.py # Endpoints підсумків (в розробці)
│       │           └── teams.py    # Endpoints команд (в розробці)
│       ├── core/
│       │   ├── config.py          # Pydantic Settings (DATABASE_URL, async_database_url)
│       │   └── security.py        # Безпека та хешування
│       ├── db/
│       │   └── session.py         # Async SQLAlchemy engine, async_sessionmaker, Base, get_async_session
│       ├── models/                # SQLAlchemy моделі даних
│       │   ├── enums.py           # Enum (RoleEnum, NoteSourceEnum, IntegrationProviderEnum)
│       │   ├── integrations.py    # Модель Integration
│       │   ├── models.py          # Головний імпорт та __all__ для всіх моделей
│       │   ├── note_embeddings.py # Модель NoteEmbedding (pgvector Vector(1536))
│       │   ├── notes.py           # Модель Note
│       │   ├── profiles.py        # Модель Profile (користувач)
│       │   ├── summaries.py       # Модель Summary (тижневі підсумки)
│       │   ├── team_digests.py    # Модель TeamDigest (дайджести команди)
│       │   └── teams.py           # Моделі Team, TeamMembers
│       ├── routers/               # Додаткові роутери (в розробці)
│       ├── schemas/               # Pydantic схеми (в розробці)
│       ├── services/              # Бізнес-логіка (в розробці)
│       └── tests/                 # Тести (в розробці)
├── deployments/                   # Конфігурації деплою
├── frontend/                      # React/Vite фронтенд (в розробці)
├── supabase/                      # Supabase migrations (структура підготовлена)
├── docker-compose.yml             # PostgreSQL 16 з розширенням pgvector (порт 5432)
├── HINT.txt                       # Шпаргалка з командами запуску та роботи з БД
├── main.py                        # Кореневий скрипт запуску Uvicorn сервера
├── pyproject.toml                 # Залежності проекту (uv / pip)
├── README.md                      # Документація проекту Recap
└── PROJECT_INDEX.md               # Даний індексний файл проекту
```

---

## 3. 🗄 Моделі даних (Database Models)

1. **Profile (`profiles`)** — профіль користувача (`id`, `firstname`, `lastname`, `avatar_url`, `timezone`, `created_at`). Зв'язки: `notes`, `summaries`, `integrations`, `teams`, `team_memberships`.
2. **Team (`teams`)** — команда (`id`, `name`, `owner_id`, `created_at`).
3. **TeamMembers (`team_members`)** — члени команди (`team_id`, `user_id`, `role`: `owner`|`manager`|`member`, `joined_at`).
4. **Note (`notes`)** — нотатка (`id`, `user_id`, `content`, `source`: `manual`|`slack`|`task_tracker`|`calendar`, `source_ref`, `created_at`).
5. **NoteEmbedding (`note_embeddings`)** — векторні ембедінги нотатки (`id`, `note_id`, `embedding_vector`: `Vector(1536)`, `created_at`).
6. **Summary (`summaries`)** — тижневий підсумок (`id`, `user_id`, `period_start`, `period_end`, `highlight`, `decision`, `blockers`, `next_steps`, `raw_llm_output`: `JSONB`, `is_public`, `public_slug`).
7. **TeamDigest (`team_digests`)** — дайджест команди (`id`, `team_id`, `period_start`, `period_end`, `content`: `JSONB`).
8. **Integration (`integrations`)** — інтеграції зовні (`id`, `profile_id`, `provider`: `slack`|`linear`|`jira`|`trello`|`google_calendar`, `access_token`, `refresh_token`, `meta_data`: `JSONB`).

---

## 4. 🌐 API Ендпоінти (Endpoints Status)

- [ ] `POST /api/v1/auth/*` — Аутентифікація (в розробці, заглушка `auth.py`)
- [ ] `GET/POST /api/v1/notes/*` — Нотатки (в розробці, заглушка `notes.py`)
- [ ] `GET/POST /api/v1/summaries/*` — Підсумки (в розробці, заглушка `summaries.py`)
- [ ] `GET/POST /api/v1/teams/*` — Команди (в розробці, заглушка `teams.py`)

---

## 5. 🤖 Правила для Агента (Workflow & Token Saving)

При отриманні будь-якого нового промпту від користувача:
1. **Крок 1: Ознайомлення з контекстом**
   - Відкрити та прочитати `PROJECT_INDEX.md`.
   - Використати карту файлів та опис моделей для швидкої орієнтації **без повторного сканування всього репозиторію**.
2. **Крок 2: Точкова робота**
   - Відкрити лише потрібні файли для редагування/створення.
   - Виконати поставлене завдання.
3. **Крок 3: Оновлення індексу**
   - Після внесення змін оновити `PROJECT_INDEX.md`:
     - Оновити карту файлів (якщо додано/видалено/перейменовано файли).
     - Оновити статус ендпоінтів/компонентів.
     - Записати нову зміну в розділ **6. Журнал змін (Changelog)** з поточною датою та стислим описом зробленого.

---

## 6. 📝 Журнал змін (Changelog)

| Дата (YYYY-MM-DD) | Змінені файли / Компоненти | Опис змін |
| :--- | :--- | :--- |
| **2026-08-03** | `PROJECT_INDEX.md`, `.agents/AGENTS.md`, `README.md` | Створено індексний файл проекту `PROJECT_INDEX.md` для економії токенів, налаштовано правила для агента в `.agents/AGENTS.md`, виправлено кодування `README.md` на UTF-8. |
