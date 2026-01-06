# secret-friend-app

## Structure

```bash
src/
├── handlers/            # entry points (lambdas)
│   ├── create_user.py
│   ├── get_user.py
│   └── health.py
│
├── services/            # lógica de negocio
│   └── user_service.py
│
├── repositories/        # acceso a datos
│   └── user_repository.py
│
├── models/              # modelos simples
│   └── user.py
│
├── shared/
│   ├── response.py
│   ├── validation.py
│   └── config.py
│
└── settings.py          # app settings

```

## Workflow

```bash
handler → service → repository
```