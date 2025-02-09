import threading
from flask_socketio import SocketIO
from modules.graph_settlement import TransactionGraph
from modules.order_book_simulation import order_book_simulator
from datetime import datetime
import pandas as pd
from flask_login import UserMixin, login_required, current_user
from flask import Blueprint, abort, jsonify, render_template, request, redirect, url_for, flash, session
from sqlalchemy import func
from login import login
from models import Holding, MarketData, db, User, PriceRow, Order, MatchedOrder


bp = Blueprint('routes', __name__)


@bp.route('/', methods=['GET', 'POST'])
def login_route():
    return login(request)


@bp.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if 'username' not in session or not session['is_admin']:
        return redirect(url_for('routes.login_route'))

    # Fetch the user's details from the database
    user = User.query.filter_by(username=session['username']).first()
    flash('Welcome ' + (user.first_name if user.first_name else 'Admin'))

    if not user:
        flash('User not found')
        return redirect(url_for('routes.login_route'))

    # Pass the user's first name to the template
    return render_template('/admin/admin.html', user=user)


@login_required
@bp.route('/user/dashboard')
def user_dashboard():
    if 'username' not in session:
        return redirect(url_for('routes.login_route'))

    # Fetch the user's details from the database
    user = User.query.filter_by(username=session['username']).first()

    if not user:
        flash('User not found')
        return redirect(url_for('route.login_route'))

    # Pass the user's first name to the template
    return render_template('/users/user.html', user=user)


@login_required
@bp.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect(url_for('routes.login_route'))


@login_required
@bp.route('/page/<string:name>')
def load_page(name):
    admin_pages = ['home', 'create_user', 'marketdepth', 'live_market', 'order_book', 'user_table', 'index',
                   # Whitelisted pages
                   'contact', 'graph', 'search_users', 'settings', 'documentation', 'settlement']
    user_pages = ['home', 'about',
                  'contact', 'graph', 'settings']  # Whitelisted pages
    user = User.query.filter_by(username=session['username']).first()
    if 'username' not in session or not session['is_admin']:
        if name in user_pages:
            return render_template(f'/users/pages/{name}.html', user=user)
        return jsonify({"error": "Page not found"}), 404
    else:
        if name in admin_pages:
            return render_template(f'/admin/pages/{name}.html', user=user)
        return jsonify({"error": "Page not found"}), 404


@login_required
@bp.route('/load_csv', methods=['POST'])
def load_csv():
    if not session.get('is_admin'):
        return render_template('login.html')

    # Specify the file path directly
    csv_path = 'data/2024-08-01_view.csv'

    # Try to read the file
    try:
        df = pd.read_csv(csv_path)

        # Ensure 'csv_id' column is not in the DataFrame (let the database auto-generate it)
        if 'csv_id' in df.columns:
            df.drop(columns=['csv_id'], inplace=True)

        # Load data into the database
        df.to_sql(MarketData.__tablename__, db.engine,
                  if_exists='append', index=False)

        flash('CSV data successfully loaded into market_data table', 'success')

    except FileNotFoundError:
        flash(f"File {csv_path} not found", 'error')

    return redirect(url_for('routes.admin_dashboard'))


@login_required
@bp.route('/admin/create_user', methods=['POST'])
def create_user():
    if not session['is_admin']:
        return redirect(url_for('login'))

    new_user = User(
        username=request.form['username'],
        first_name=request.form['first_name'],
        middle_name=request.form['middle_name'],
        last_name=request.form['last_name'],
        city=request.form['city'],
        district=request.form['district'],
        province=request.form['province'],
        email=request.form['email'],
        phone_number=request.form['phone_number'],
        demat_id=request.form['demat_id'],
        collateral=float(request.form['collateral']),
        is_admin='is_admin' in request.form
    )
    new_user.set_password(request.form['password'])
    db.session.add(new_user)
    db.session.commit()
    flash('User  created successfully.')
    return redirect(url_for('routes.admin_dashboard'))


@login_required
@bp.route('/admin/users')
def admin_users():
    search_users()
    return render_template('admin/pages/search_users.html')


@login_required
@bp.route('/admin/search_users', methods=['GET'])
def search_users():
    search_query = request.args.get('search', '')

    # Fetch users based on the search query
    if search_query:
        users = User.query.filter(
            (User .username.like(f'%{search_query}%')) |
            (User .email.like(f'%{search_query}%')) |
            (User .demat_id.like(f'%{search_query}%'))
        ).all()  # Fetch users matching the search criteria
    else:
        users = User.query.all()  # Fetch all users if no search term is provided

    return render_template('admin/pages/user_table.html', users=users)


@login_required
@bp.route('/admin/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.first_name = request.form['first_name']
        user.middle_name = request.form['middle_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        user.phone_number = request.form['phone_number']
        user.demat_id = request.form['demat_id']
        user.collateral = float(request.form['collateral'])
        if request.form['password']:
            user.set_password(request.form['password'])
        user.is_admin = 'is_admin' in request.form
        db.session.commit()
        flash('User  information updated successfully.')
        return redirect(url_for('admin_dashboard'))

    return render_template('edit_user.html', user=user)


@bp.route('/entities')
def entities():
    """Fetch unique buyer and seller names from the database."""
    buyers = db.session.query(PriceRow.buyerName).distinct().all()
    sellers = db.session.query(PriceRow.sellerName).distinct().all()
    entities = list(set([row.buyerName for row in buyers] +
                    [row.sellerName for row in sellers]))
    return jsonify(entities)


@bp.route('/symbols')
def symbols():
    """Fetch unique symbols from the database."""
    symbols = db.session.query(PriceRow.symbol).distinct().all()
    symbols = [row.symbol for row in symbols]
    return jsonify(symbols)


@bp.route('/graph_data')
def graph_data():
    """Fetch data from the database, process it using TransactionGraph, and return graph data as JSON."""
    entity = request.args.get('entity')
    symbol = request.args.get('symbol')
    transactions = PriceRow.query.filter(
        ((PriceRow.buyerName == entity) | (PriceRow.sellerName == entity)) & (
            PriceRow.symbol == symbol)
    ).all()
    print(f"Transactions: {transactions}")

    transaction_graph = TransactionGraph()

    for transaction in transactions:
        transaction_graph.add_transaction(
            transaction.buyerID, transaction.sellerID, transaction.qty)
        transaction_graph.graph[transaction.buyerID][transaction.sellerID]['rate'] = transaction.rate

    edges = []
    for u, v, data in transaction_graph.graph.edges(data=True):
        edges.append({"source": u, "target": v,
                     "qty": data['qty'], "rate": data['rate']})
    return jsonify(edges)


@bp.route('/normalized_graph_data')
def normalized_graph_data():
    """Fetch data from the database, process it using TransactionGraph, and return normalized graph data as JSON."""
    entity = request.args.get('entity')
    symbol = request.args.get('symbol')
    transactions = PriceRow.query.filter(
        ((PriceRow.buyerName == entity) | (PriceRow.sellerName == entity)) & (
            PriceRow.symbol == symbol)
    ).all()

    transaction_graph = TransactionGraph()
    for transaction in transactions:
        transaction_graph.add_transaction(
            transaction.buyerID, transaction.sellerID, transaction.qty)
        transaction_graph.graph[transaction.buyerID][transaction.sellerID]['rate'] = transaction.rate

    transaction_graph.normalize()
    normalized_graph = transaction_graph.get_normalized_graph()
    return jsonify(normalized_graph)


# @bp.route('/entities')
# def entities():
#     """Fetch unique buyer and seller names from the database."""
#     buyers = db.session.query(MarketData.buyer_broker_name).distinct().all()
#     sellers = db.session.query(MarketData.seller_broker_name).distinct().all()
#     entities = list(set([row.buyer_broker_name for row in buyers] +
#                         [row.seller_broker_name for row in sellers]))
#     return jsonify(entities)


# @bp.route('/symbols')
# def symbols():
#     """Fetch unique symbols from the database."""
#     symbols = db.session.query(MarketData.stock_symbol).distinct().all()
#     symbols = [row.stock_symbol for row in symbols]
#     return jsonify(symbols)


# @bp.route('/graph_data')
# def graph_data():
#     entity = request.args.get('entity')
#     symbol = request.args.get('symbol')

#     # Fetch data from the MarketData table using buyer_broker_name
#     transactions = MarketData.query.filter(
#         ((MarketData.buyer_broker_name == entity) | (
#             MarketData.seller_broker_name == entity))
#     ).all()

#     # Create a TransactionGraph object
#     transaction_graph = TransactionGraph()
#     for transaction in transactions:
#         transaction_graph.add_transaction(
#             transaction.buyer_member_id,  # Ensure this is correct
#             transaction.seller_member_id,
#             transaction.contract_quantity
#         )

#     # Get the graph edges
#     edges = transaction_graph.get_normalized_graph()

#     return jsonify(edges)


# @bp.route('/normalized_graph_data')
# def normalized_graph_data():
#     entity = request.args.get('entity')
#     symbol = request.args.get('symbol')

#     # Fetch data from the MarketData table
#     transactions = MarketData.query.filter(
#         ((MarketData.buyer_broker_name == entity) | (
#             MarketData.seller_broker_name == entity))
#     ).all()

#     # Create a TransactionGraph object
#     transaction_graph = TransactionGraph()
#     for transaction in transactions:
#         transaction_graph.add_transaction(
#             transaction.buyer_member_id,  # Ensure this is correct
#             transaction.seller_member_id,
#             transaction.contract_quantity
#         )

#     # Apply netting to the graph
#     transaction_graph.apply_netting()

#     # Get the normalized graph edges
#     edges = transaction_graph.get_normalized_graph()

#     # Return the graph data in the expected format
#     return jsonify(edges)

# Admin market control endpoints


@bp.route('/admin/market_control', methods=['POST'])
@login_required
def market_control():
    if not current_user.is_admin:
        abort(403)

    action = request.form.get('action')
    if action == 'start':
        order_book_simulator.start()
        flash('Market simulation started', 'success')
    elif action == 'stop':
        order_book_simulator.stop()
        flash('Market simulation stopped', 'warning')
    return redirect(url_for('routes.admin_dashboard'))


# # Update place_order route with collateral checks
# @bp.route('/place_order', methods=['POST'])
# @login_required
# def place_order():
#     symbol = request.form['symbol']
#     ltp = get_ltp(symbol)
#     price = float(request.form['price'])
#     quantity = int(request.form['quantity'])
#     is_buy = request.form['is_buy'] == 'true'

#     # Price validation
#     if not (ltp * 0.98 <= price <= ltp * 1.02):
#         flash("Price must be within ±2% of LTP")
#         return redirect(url_for('routes.order_book', symbol=symbol))

#     # Collateral/Holding checks
#     if is_buy:
#         required_collateral = price * quantity
#         if current_user.collateral < required_collateral:
#             flash(
#                 f"Insufficient collateral. Required: रु{required_collateral:.2f}")
#             return redirect_back()
#     else:
#         holding = Holding.query.filter_by(
#             user_id=current_user.id, symbol=symbol).first()
#         if not holding or holding.quantity < quantity:
#             flash("Insufficient shares to sell")
#             return redirect_back()

#     # Create order
#     order = Order(
#         user_id=current_user.id,
#         symbol=symbol,
#         price=price,
#         quantity=quantity,
#         is_buy=is_buy
#     )

#     # Reserve collateral
#     if is_buy:
#         current_user.collateral -= price * quantity
#         db.session.add(order)
#         db.session.commit()

#     flash("Order placed successfully")
#     return redirect(url_for('routes.order_book', symbol=symbol))


# # Displays Order Book for Buy anf Sell Orders
# @bp.route('/page/order_book', methods=['GET', 'POST'])
# @login_required
# def order_book_data():
#     symbol = request.args.get('symbol', 'GUFL')
#     ltp = get_ltp(symbol)

#     buy_orders = Order.query.filter_by(is_buy=True, status='pending', symbol=symbol
#                                        ).group_by(Order.price).with_entities(
#         Order.price,
#         func.sum(Order.quantity).label('total_quantity'),
#         func.count(Order.id).label('order_count')
#     ).order_by(Order.price.desc()).limit(7).all()

#     sell_orders = Order.query.filter_by(is_buy=False, status='pending', symbol=symbol
#                                         ).group_by(Order.price).with_entities(
#         Order.price,
#         func.sum(Order.quantity).label('total_quantity'),
#         func.count(Order.id).label('order_count')
#     ).order_by(Order.price.asc()).limit(7).all()

#     return jsonify({
#         'buy_orders': [dict(zip(('price', 'quantity', 'count'), o)) for o in buy_orders],
#         'sell_orders': [dict(zip(('price', 'quantity', 'count'), o)) for o in sell_orders],
#         'ltp': ltp,
#         'security_name': MarketData.query.filter_by(stock_symbol=symbol
#                                                     ).first().security_name if MarketData.query.first() else ''
#     })


# @bp.route('/holdings')
# @login_required
# def holdings():
#     user_holdings = Holding.query.filter_by(user_id=current_user.id).all()
#     return render_template('holdings.html', holdings=user_holdings)


# @bp.route('/matched_orders_today')
# def matched_orders_today():
#     today = datetime.today().date()
#     matched = MatchedOrder.query.filter(
#         func.date(MatchedOrder.timestamp) == today
#     ).all()
#     return jsonify([{
#         'symbol': m.symbol,
#         'price': m.price,
#         'quantity': m.quantity,
#         'time': m.timestamp.strftime('%H:%M:%S')
#     } for m in matched])


# def get_ltp(symbol):
#     return MarketData.query.filter_by(stock_symbol=symbol
#                                       ).order_by(MarketData.trade_time.desc()).first().contract_rate
