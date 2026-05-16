import sqlite3
import os
from flask import Flask, g, current_app


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db(app):
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id      INTEGER PRIMARY KEY,
                amount  REAL    NOT NULL,
                status  TEXT    NOT NULL,
                patient_id INTEGER NOT NULL
            )
        ''')
        db.execute("INSERT OR IGNORE INTO payments VALUES (1, 150.00, 'completed', 1001)")
        db.execute("INSERT OR IGNORE INTO payments VALUES (2, 200.00, 'pending',   1002)")
        db.commit()


def create_app(config=None):
    app = Flask(__name__)
    app.config['DATABASE'] = os.path.join(app.instance_path, 'medsecure.db')

    if config:
        app.config.update(config)

    os.makedirs(app.instance_path, exist_ok=True)
    app.teardown_appcontext(close_db)

    from app.routes.payments import payments_bp
    app.register_blueprint(payments_bp)

    init_db(app)

    return app
