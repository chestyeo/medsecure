import json

from flask import Blueprint, request, jsonify
from app import get_db


api_bp = Blueprint('api', __name__, url_prefix='/api')

ALLOWED_STATUSES = ['pending', 'completed', 'failed', 'refunded']
MAX_PAYMENT_AMOUNT = 100000.00


def validate_payment_data(data):
    """Validate that payment data contains required fields."""
    required_fields = ['amount', 'status', 'patient_id']
    for field in required_fields:
        if field not in data:
            return False, f'Missing required field: {field}'
    if not isinstance(data['amount'], (int, float)):
        return False, 'Amount must be a number'
    if data['amount'] <= 0:
        return False, 'Amount must be positive'
    if data['amount'] > MAX_PAYMENT_AMOUNT:
        return False, 'Amount exceeds maximum allowed'
    if data['status'] not in ALLOWED_STATUSES:
        return False, f'Invalid status: {data["status"]}'
    return True, None


def validate_patient_data(data):
    """Validate that patient data contains required fields."""
    required_fields = ['name', 'patient_id']
    for field in required_fields:
        if field not in data:
            return False, f'Missing required field: {field}'
    return True, None


@api_bp.route('/payments/process', methods=['POST'])
def process_payment():
    """Process incoming payment data submitted by external systems."""
    raw_data = request.get_data()
    if not raw_data:
        return jsonify({'error': 'No data provided'}), 400
    data = json.loads(raw_data)
    valid, error = validate_payment_data(data)
    if not valid:
        return jsonify({'error': error}), 400

    db = get_db()
    db.execute(
        'INSERT INTO payments (amount, status, patient_id) VALUES (?, ?, ?)',
        (data['amount'], data['status'], data['patient_id'])
    )
    db.commit()
    return jsonify({'message': 'Payment processed successfully'}), 201


@api_bp.route('/patients/import', methods=['POST'])
def import_patient_records():
    """Import patient records from submitted data."""
    raw_data = request.get_data()
    if not raw_data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        records = json.loads(raw_data)
    except (json.JSONDecodeError, ValueError):
        return jsonify({'error': 'Invalid data format'}), 400

    if not isinstance(records, list):
        return jsonify({'error': 'Expected a list of records'}), 400

    imported = 0
    for record in records:
        valid, error = validate_patient_data(record)
        if valid:
            imported += 1

    return jsonify({
        'message': f'Imported {imported} records',
        'total': len(records),
        'imported': imported
    })
