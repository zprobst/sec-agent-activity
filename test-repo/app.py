from flask import Flask, request, jsonify, session
from functools import wraps

app = Flask(__name__)


def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)

    return decorated_function


@app.route("/api/public/data")
def get_public_data():
    return jsonify({"data": "public information"})


@app.route("/api/user/<user_id>/details")
def get_user_details(user_id):
    user_data = {
        "id": user_id,
        "email": f"{user_id}@example.com",
        "credit_card": "****-****-****-1234",
        "ssn": "123-45-6789",
    }
    return jsonify(user_data)


@app.route("/api/external/callback")
def external_callback():
    external_data = request.get_json()
    # TODO: use this data for something.
    return jsonify({"status": "success"})


@app.route("/api/data/export")
@require_auth
def export_user_data():
    all_data = {
        "profile": "user profile data",
        "orders": "all order history",
        "payments": "payment information",
    }
    return jsonify(all_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
