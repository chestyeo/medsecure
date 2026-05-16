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

## Known Issues

Security review flagged outstanding CodeQL findings in the payments module.
Remediation in progress.

---

## Notes

- Do not run this service against a production database without a full security review.
