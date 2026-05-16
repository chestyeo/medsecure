# medsecure

## What This Is

A minimal intentionally vulnerable Flask application used as the target repository for the Security Remediation Agent demo.

This repo simulates a real client codebase. Devin operates directly on this repo — investigating vulnerabilities, generating fixes, and opening PRs — without any changes to the existing workflow.

---

## Project Structure

```
medsecure/
├── app/
│   ├── __init__.py
│   └── routes/
│       └── payments.py         ← contains SQL injection vulnerability
├── tests/
│   └── test_payments.py        ← basic test suite Devin will run
├── CODEOWNERS                  ← ownership file Devin reads for context
├── requirements.txt
└── README.md                   ← this file
```

---

## The Vulnerability

**File:** `app/routes/payments.py`
**Line:** ~20
**Rule:** `py/sql-injection`
**Severity:** high

```python
# VULNERABLE — do not use in production
def get_payment(payment_id):
    query = "SELECT * FROM payments WHERE id = '" + payment_id + "'"
    return db.execute(query)
```

The payment ID is passed directly into a SQL query via string concatenation. An attacker can manipulate the query to access or destroy data.

---

## What Devin Will Do

When tasked by the remediation agent, Devin will:

1. Read this repo and locate the vulnerable file
2. Understand the surrounding code context
3. Generate a minimal fix using parameterised queries
4. Run the test suite to validate the fix
5. Open a PR with a full vulnerability summary and audit metadata

Devin will NOT:
- Refactor unrelated code
- Rename variables
- Modify any files outside the fix scope

---

## How to Run Locally

```bash
pip install -r requirements.txt
python -m flask run
```

## How to Run Tests

```bash
pytest tests/
```

Tests must pass before and after Devin's fix.

---

## CODEOWNERS

```
# payments module owned by backend security team
app/routes/payments.py @medsecure/backend-security
```

Devin reads this to determine ownership and include the right reviewers on the PR.

---

## Requirements

```
flask==2.3.0
pytest==7.4.0
```

Keep dependencies minimal. This repo exists only to demonstrate Devin's remediation capability on a realistic but simple codebase.

---

## Notes

- This repo is intentionally minimal — one vulnerability, one test file, one CODEOWNERS entry
- Do not add additional vulnerabilities or complexity
- The vulnerability is real and exploitable — do not deploy this application