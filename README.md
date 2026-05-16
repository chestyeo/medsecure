# medsecure
A Flask application for processing and retrieving patient payment records.

---

## Project Structure

```
medsecure/
├── app/
│   ├── __init__.py
│   └── routes/
│       └── payments.py
├── findings/
│   └── codeql.sarif.json
├── tests/
│   └── test_payments.py
├── CODEOWNERS
├── requirements.txt
└── README.md
```

---

## How to Run Locally

```bash
cp .env.example .env
pip install -r requirements.txt
python -m flask run
```

## How to Run Tests

```bash
pytest tests/
```

---

## CODEOWNERS

```
# payments module owned by backend security team
app/routes/payments.py @medsecure/backend-security
```

---

## Requirements

```
flask==2.3.0
werkzeug==2.3.7
pytest==7.4.0
```

---

## Security

CodeQL scans run on every push and output findings to `findings/codeql.sarif.json`.
Outstanding findings are triaged and remediated via the security remediation agent.

| Finding | Severity | Status |
|---|---|---|
| SQL injection in `payments.py` | High | Outstanding |
| Hardcoded API key in `payments.py` | High | Outstanding |

---

## Notes

- Do not run this service against a production database without a full security review.
- `findings/codeql.sarif.json` is the source of truth for outstanding security findings.
