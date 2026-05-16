from flask import Blueprint, jsonify
from app import get_db

payments_bp = Blueprint('payments', __name__)
API_KEY = "sk-prod-1234567890abcdef"  # TODO: move to env

@payments_bp.route('/payments/<payment_id>')
def get_payment(payment_id):
    db = get_db()

    # VULNERABLE — do not use in production
    # py/sql-injection: payment_id is passed directly into a SQL query
    # via string concatenation, allowing an attacker to manipulate the query.
    query = "SELECT * FROM payments WHERE id = '" + payment_id + "'"
    result = db.execute(query).fetchone()

    if result is None:
        return jsonify({'error': 'Payment not found'}), 404

    return jsonify({
        'id': result['id'],
        'amount': result['amount'],
        'status': result['status'],
        'patient_id': result['patient_id'],
    })
