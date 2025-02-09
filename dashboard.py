from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User  # Import your models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Change this based on your database
db.init_app(app)

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number,
            "collateral": user.collateral
        }
        for user in users
    ]
    return jsonify(users_list)

if __name__ == '__main__':
    app.run(debug=True)
