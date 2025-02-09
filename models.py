# models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin  # Import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(80))
    middle_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    city = db.Column(db.String(80))
    district = db.Column(db.String(80))
    province = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    demat_id = db.Column(db.String(80), unique=True)
    collateral = db.Column(db.Float, default=0.0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def create_dummy_user(cls):
        """Create a dummy user with random credentials"""
        from random import randint, choice
        first_names = ['Dummy', 'Test', 'Mock', 'Sim']
        last_names = ['User', 'Trader', 'Account', 'Bot']

        dummy_user = User(
            username=f"dummy_{randint(1000, 9999)}",
            first_name=choice(first_names),
            last_name=choice(last_names),
            email=f"dummy{randint(1000, 9999)}@example.com",
            is_admin=False,
            demat_id=f"DMY{randint(100000, 999999)}",
            collateral=100000  # Default collateral
        )
        dummy_user.set_password('dummy_password')
        return dummy_user


class MarketData(db.Model):
    __tablename__ = 'market_data'
    csv_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contract_id = db.Column(db.BigInteger)  # Use BigInteger for larger numbers
    contract_type = db.Column(db.String(80))
    stock_symbol = db.Column(db.String(80))
    buyer_member_id = db.Column(db.String(80))
    seller_member_id = db.Column(db.String(80))
    contract_quantity = db.Column(db.Float)
    contract_rate = db.Column(db.Float)
    contract_amount = db.Column(db.Float)
    business_date = db.Column(db.String(80))
    trade_book_id = db.Column(db.String(80))
    stock_id = db.Column(db.String(80))
    buyer_broker_name = db.Column(db.String(80))
    seller_broker_name = db.Column(db.String(80))
    trade_time = db.Column(db.String(80))
    security_name = db.Column(db.String(80))


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    symbol = db.Column(db.String(10))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    is_buy = db.Column(db.Boolean)
    # pending, matched, cancelled
    status = db.Column(db.String(20), default='pending')
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class MatchedOrder(db.Model):
    __tablename__ = 'matched_orders'
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    symbol = db.Column(db.String(10))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    trading_company = db.Column(
        db.String(100), default="Order Matching FYP Private Limited")


class Holding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    symbol = db.Column(db.String(10))
    quantity = db.Column(db.Integer)


class StockInfo(db.Model):
    symbol = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100))


class PriceRow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conID = db.Column(db.String(50), nullable=False, unique=True)
    buyerID = db.Column(db.String(5))
    sellerID = db.Column(db.String(5))
    qty = db.Column(db.Integer)
    rate = db.Column(db.Float)
    buyerName = db.Column(db.String(100))
    sellerName = db.Column(db.String(100))
    symbol = db.Column(db.String(10))

    def __repr__(self):
        return f'<Task {self.id}>'

    def to_dict(self):
        """Convert SQLAlchemy object to a dictionary."""
        return {
            'id': self.id,
            'conID': self.conID,
            'buyerID': self.buyerID,
            'sellerID': self.sellerID,
            'qty': self.qty,
            'rate': self.rate,
            'buyerName': self.buyerName,
            'sellerName': self.sellerName,
            'symbol': self.symbol
        }
