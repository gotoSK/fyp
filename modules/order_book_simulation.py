# order_book_simulation.py
import random
import threading
import time
from datetime import datetime
from models import StockInfo, User, db, MarketData, Order, MatchedOrder, Holding
from sqlalchemy import func


class OrderBookSimulator:
    def __init__(self):
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def run(self):
        while self.running:
            self.generate_dummy_order()
            self.match_orders()
            time.sleep(random.randint(10, 15))

    def update_order_book(self):
        # Fetch all active orders
        active_buy_orders = Order.query.filter_by(
            is_buy=True, status='pending').all()
        active_sell_orders = Order.query.filter_by(
            is_buy=False, status='pending').all()

        # Simulate price changes based on LTP
        for order in active_buy_orders + active_sell_orders:
            ltp = self.get_last_traded_price(order.symbol)
            new_price = self.simulate_price_change(ltp)
            order.price = new_price
            db.session.commit()

        # Match orders
        self.match_orders()

    def get_last_traded_price(self, symbol):
        last_trade = MarketData.query.filter_by(stock_symbol=symbol).order_by(
            MarketData.trade_time.desc()).first()
        return last_trade.contract_rate if last_trade else 100  # Default price if no trades

    def simulate_price_change(self, ltp):
        # Simulate a price change within 10% of LTP
        import random
        change = random.uniform(-0.1, 0.1) * ltp
        new_price = ltp + change
        return max(new_price, 0)  # Ensure price doesn't go negative

    def match_orders(self):
        # Get orders with price-time priority
        active_buy_orders = Order.query.filter_by(
            is_buy=True, status='pending'
        ).order_by(Order.price.desc(), Order.timestamp.asc()).all()

        active_sell_orders = Order.query.filter_by(
            is_buy=False, status='pending'
        ).order_by(Order.price.asc(), Order.timestamp.asc()).all()

        for buy_order in active_buy_orders:
            for sell_order in active_sell_orders:
                if buy_order.symbol == sell_order.symbol and buy_order.price >= sell_order.price:
                    matched_quantity = min(
                        buy_order.quantity, sell_order.quantity)
                    self.create_matched_order(
                        buy_order, sell_order, matched_quantity)
                    self.update_holdings(
                        buy_order.user_id, sell_order.user_id, buy_order.symbol, matched_quantity)
                    self.update_market_data(
                        buy_order, sell_order, matched_quantity)

                    buy_order.quantity -= matched_quantity
                    sell_order.quantity -= matched_quantity

                    if buy_order.quantity == 0:
                        buy_order.status = 'matched'
                    if sell_order.quantity == 0:
                        sell_order.status = 'matched'

                    db.session.commit()
        market_data = MarketData(
            # ... other fields ...
            security_name=StockInfo.query.filter_by(symbol=symbol
                                                    ).first().name if StockInfo.query.first() else 'Unknown'
        )

    def create_matched_order(self, buy_order, sell_order, quantity):
        matched_order = MatchedOrder(
            buyer_id=buy_order.user_id,
            seller_id=sell_order.user_id,
            symbol=buy_order.symbol,
            price=buy_order.price,
            quantity=quantity,
            timestamp=datetime.utcnow()
        )
        db.session.add(matched_order)
        db.session.commit()

    def update_holdings(self, buyer_id, seller_id, symbol, quantity):
        # Update buyer's holdings
        buyer_holding = Holding.query.filter_by(
            user_id=buyer_id, symbol=symbol).first()
        if buyer_holding:
            buyer_holding.quantity += quantity
        else:
            buyer_holding = Holding(
                user_id=buyer_id, symbol=symbol, quantity=quantity)
            db.session.add(buyer_holding)

        # Update seller's holdings
        seller_holding = Holding.query.filter_by(
            user_id=seller_id, symbol=symbol).first()
        if seller_holding:
            seller_holding.quantity -= quantity
            if seller_holding.quantity == 0:
                db.session.delete(seller_holding)

        db.session.commit()

    def update_market_data(self, buy_order, sell_order, quantity):
        market_data = MarketData(
            contract_id=MarketData.query.count() + 1,
            contract_type='trade',
            stock_symbol=buy_order.symbol,
            buyer_member_id=buy_order.user_id,
            seller_member_id=sell_order.user_id,
            contract_quantity=quantity,
            contract_rate=buy_order.price,
            contract_amount=buy_order.price * quantity,
            business_date=datetime.utcnow().date(),
            trade_book_id='SIM',
            stock_id=buy_order.symbol,
            buyer_broker_name='SIM',
            seller_broker_name='SIM',
            trade_time=datetime.utcnow(),
            security_name=buy_order.symbol
        )
        db.session.add(market_data)
        db.session.commit()

    def generate_dummy_order(self, symbol):
        # Generate dummy orders
        symbols = [row.stock_symbol for row in
                   MarketData.query.with_entities(MarketData.stock_symbol).distinct(MarketData.stock_symbol).all()]
        for _ in range(random.randint(3, 7)):  # Random number of dummy orders
            symbol = random.choice(symbols)
            order = self.generate_dummy_order(symbol)
            db.session.add(order)
        db.session.commit()

        # Create dummy user if needed
        if not User.query.filter(User.username.like('dummy_%')).first():
            db.session.add(User.create_dummy_user())
            db.session.commit()

        dummy_user = User.query.filter(User.username.like('dummy_%')).first()
        ltp = self.get_last_traded_price(symbol)

        return Order(
            user_id=dummy_user.id,
            symbol=symbol,
            price=round(ltp * random.uniform(0.98, 1.02), 2),
            quantity=random.randint(1, 100),
            is_buy=random.choice([True, False]),
            status='pending'
        )


order_book_simulator = OrderBookSimulator()
