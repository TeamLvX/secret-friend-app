# secret-friend-app

## Structure

src/
├── handlers/            # entry points (lambdas)
│   ├── create_user.py
│   ├── get_user.py
│   └── health.py
│
├── services/            # bussines logic
│   └── user_service.py
│
├── repositories/        # data access
│   └── user_repository.py
│
├── models/              # models
│   └── user.py
│
├── shared/
│   ├── response.py
│   ├── validation.py
│   └── config.py
│
└── settings.py          # App settings

## Workflow

handler → service → repository