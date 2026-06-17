# Security Policy

## Supported Versions

This repository currently tracks security updates on the `main` branch.

## Reporting a Vulnerability

Please report security issues privately to the repository owner or maintainer. Do not open a public issue for vulnerabilities that expose credentials, authentication bypasses, database access, or sensitive operational data.

Include:

- A clear description of the issue.
- Steps to reproduce.
- Affected routes, files, or configuration.
- Suggested mitigation, if known.

## Authentication And Sessions

- Scanner passwords are stored using Django password hashers.
- Existing plaintext scanner passwords are hashed through a migration.
- QR workflow routes require a valid login session.
- Expired sessions are logged out and redirected to `/Login`.

## Security Checks

Before release, run:

```bash
python manage.py check --deploy
python -m pip_audit -r requirements.txt
python -m bandit -r Login QR QRSCANNER -x QRSCANNER/static,QR/migrations,Login/migrations -ll
```

## Sensitive Data

Never commit:

- `.env` files.
- Database dumps or local database files.
- Production credentials.
- Secret keys or production environment values.
- User data or operational cylinder records.

Production deployments must set `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, secure cookie flags, and HTTPS redirect/HSTS settings through environment variables.
