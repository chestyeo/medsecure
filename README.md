# medsecure

Intentionally vulnerable Flask application used as the target repository for the Security Remediation Agent demo.

> **Warning:** This app contains a real, exploitable SQL injection vulnerability. Do not deploy it.

## Run

```bash
pip install -r requirements.txt
python -m flask run
```

## Test

```bash
pytest tests/
```
