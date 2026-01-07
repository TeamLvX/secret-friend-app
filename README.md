# secret-friend-app

## Structure

```bash
src/
├── main.py                  # FastAPI app
│
├── api/                     # Capa HTTP (routers)
│   └── v1/
│       ├── users.py
│       └── health.py
│
├── services/                # Lógica de negocio
│   └── user_service.py
│
├── repositories/            # Acceso a datos
│   └── user_repository.py
│
├── models/                  # Modelos de dominio (simples)
│   └── user.py
│
├── schemas/                 # DTOs / Pydantic (request/response)
│   └── user_schema.py
│
├── shared/
│   ├── config.py
│   ├── responses.py
│   └── logging.py
│
└── dependencies.py          # DI ligera (FastAPI style)

```

## Workflow

```bash
Request
  ↓
Router (api)
  ↓
Service
  ↓
Repository


```
