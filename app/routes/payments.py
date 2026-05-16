from flask import Blueprint, jsonify
from app import get_db

payments_bp = Blueprint('payments', __name__)


@payments_bp.route('/payments/<payment_id>')
def get_payment(payment_id):
    db = get_db()

    query = "SELECT * FROM payments WHERE id = ?"
    result = db.execute(query, (payment_id,)).fetchone()

    if result is None:
        return jsonify({'error': 'Payment not found'}), 404

    return jsonify({
        'id': result['id'],
        'amount': result['amount'],
        'status': result['status'],
        'patient_id': result['patient_id'],
    })
