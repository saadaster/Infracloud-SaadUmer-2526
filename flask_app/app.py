from flask import Flask, jsonify, request

app = Flask(__name__)

# Onze "database" (simpele lijst voor dit voorbeeld)
users = [
    {"id": 1, "name": "Alice", "role": "Admin"},
    {"id": 2, "name": "Bob", "role": "User"}
]

@app.route('/users', methods=['GET'])
def get_users():
    """Geeft alle gebruikers terug"""
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Zoekt een specifieke gebruiker op basis van ID"""
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    # We draaien de service op poort 5001
    app.run(port=5001, debug=True)