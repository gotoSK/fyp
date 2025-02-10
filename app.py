Anish
anish0698
Online

iblamesugam — 8/30/2024 2:49 PM
https://discord.gg/DFXErWw4
iblamesugam — 12/17/2024 6:35 PM
1)TCP Socket Programming:

Create a Java client-server program using TCP sockets where the client sends a string, and the server responds with the reversed string.

2)UDP Socket Programming:
Expand
LabQues.txt
1 KB
print("Enter your port: 1234\nEnter reciever's port: 5678\nYou: Hola!\nFriend: Can you speak english?\nYou:\n\n")
print("Enter your port: 5678\nEnter reciever's port: 1234\nYou: \nFriend: Hola!\nYou: Can you speak english?\nFriend: \n")
output_cheat.py
1 KB
package Lab.NetworkProgramming;

import java.io.*;
import java.net.*;

public class Lab1Client {
Expand
Lab1Client.java
1 KB
package Lab.NetworkProgramming;

/*
* 1)TCP Socket Programming:
*   Create a Java client-server program using TCP sockets where the client sends a string, and the server responds with the reversed string.
* */
Expand
Lab1Server.java
2 KB
package Lab.NetworkProgramming;

import java.io.*;
import java.net.*;
import java.util.Scanner;
Expand
Lab2Client.java
2 KB
package Lab.NetworkProgramming;

/*
* 2)UDP Socket Programming:

Write a UDP-based chat application where one instance acts as the sender and the other as the receiver.
Expand
Lab2Server.java
2 KB
package Lab.NetworkProgramming;

/*
* 3)Working with URLs:

Develop a Java program that fetches the HTML content of a given URL and displays all the hyperlinks present on the webpage.
Expand
Lab3.java
2 KB
package Lab.NetworkProgramming;

import javax.mail.*;
import javax.mail.search.FlagTerm;
import java.util.Properties;
Expand
Lab4ReceiveMail.java
2 KB
package Lab.NetworkProgramming;

/*
*4)Java Mail API, Sending and Receiving Email
Sending Emails:
Expand
Lab4SendMail.java
3 KB
Anish — 2/7/2025 2:39 PM
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User
app = Flask(name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
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

if name == 'main':
    app.run(debug=True)
yo code hera ta
iblamesugam — 2/7/2025 2:40 PM
m tyo report milaudai xu, akai xin hai
Anish — 2/7/2025 2:40 PM
class User(db.Model, UserMixin):
    tablename = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(80))
    middle_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    demat_id = db.Column(db.String(80), unique=True)
    collateral = db.Column(db.Float, default=0.0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
yesbata fetch garna lako
iblamesugam — 2/7/2025 3:29 PM
thik xa ta code ta. timle lekhya ho ki parag le? 
problem chai k aayo dekhau ta
Anish — 2/7/2025 3:34 PM
mero ho
mero ma structure na mile ho ki k ho
time run gri hera ta
iblamesugam — 2/7/2025 3:36 PM
database file diyo paarg le?
tyo chaiyo ni ta suru ma
site.db vanne file hola
models.py vanne ni hola, tes bata tanya xa values haru
Anish — 2/7/2025 3:38 PM
class User(db.Model, UserMixin):
    tablename = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(80))
    middle_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    demat_id = db.Column(db.String(80), unique=True)
    collateral = db.Column(db.Float, default=0.0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
iblamesugam — 2/7/2025 3:38 PM
maile ta arkai tarika le garya theya. simple thyo
db file ni dyou ta
Anish — 2/7/2025 3:43 PM
messanger hera ta
iblamesugam — 2/7/2025 3:49 PM
site.db vanne file xa timi sita?
Image
Anish — 2/7/2025 3:50 PM
nai model matra xa
tyo ta teti ko lagi haina ra
iblamesugam — 2/7/2025 3:51 PM
ani data nai tes vitra hunxa .db vanne file vitra
tyo naayesi read garnai milena ni data 
Anish — 2/7/2025 3:52 PM
parag le ta malie tyoo model matra deko xa
ma ta tyoo model bata fetch garne matra banauna lako thyoo
iblamesugam — 2/7/2025 3:54 PM
model ta hamro python code matra vayo. tara data chaiyo ni read garna lai. tyo maga na database file
Anish — 2/7/2025 3:54 PM
aee lala
Anish — 2/7/2025 9:24 PM
oi diagram haru deu ta
activity diagram
iblamesugam — Today at 4:58 PM
tyo hamro data set lai jupyter ma manipulate garera heri rakha na. voli sodyo vane defense ma feri asti ko jastai lyang hunxa
Anish — Today at 4:58 PM
ma herxu
k k garne ho??
iblamesugam — Today at 5:00 PM
particular stock symbol lai matra display garau na
stockSymbol vanne column bata
Anish — Today at 5:09 PM
oi tyo code deu na ma commit garxu
iblamesugam — Today at 5:12 PM
ruka na vaisakyo
mildaudai xu kunai kunai error aako
Anish — Today at 5:13 PM
aee lala
iblamesugam — Today at 5:55 PM
static/css
 vitra yo haldyou
.user-area {
    padding-left: 5vw;
}

/* Style for the user dropdown */
.dropdown {
Expand
user.css
3 KB
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    text-align: center;
}
Expand
login.css
1 KB
file name change nagara hai
ani 
statc/js
 vitra yo thapdyou
document.addEventListener("DOMContentLoaded", function() {

    const dropbtn = document.querySelector(".dropbtn");
    const dropdownContent = document.querySelector(".dropdown-content");

    dropbtn.addEventListener("click", function(event) {
Expand
user.js
1 KB
Anish — Today at 5:56 PM
python code pani deu na
iblamesugam — Today at 5:56 PM
suru ma yo hala na
templates   vtira yo add gara 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/login.css') }}">
Expand
login.html
2 KB
ati add garesi vana
Anish — Today at 6:00 PM
oi tyo sidai main branch ma commit garna milxa?
ki arkai bata garru
iblamesugam — Today at 6:01 PM
main ma ho aba sidai
voli defence xa main mai herxa tesle
teti commit garera vana ma py code dinxu
iblamesugam — Today at 6:21 PM
xito gara na parag le herxa
Anish — Today at 6:21 PM
vaisakyo ta
iblamesugam — Today at 6:23 PM
yo chai bahira folder mai
from utils import assets
import time

print("Loading Users ...")

class User:
Expand
user.py
2 KB
Anish — Today at 6:28 PM
aru ni xa ra
iblamesugam — Today at 6:34 PM
JS halxou? auta xa script.js lai update gareko xu
Anish — Today at 6:51 PM
ah deu
iblamesugam — Today at 6:52 PM
terminal batai commit garxou ki github ko website bata?
Anish — Today at 6:52 PM
bash bata gareko ho maile
iblamesugam — Today at 6:53 PM
https://github.com/gotoSK/fyp/blob/main/static/js/script.js
GitHub
fyp/static/js/script.js at main · gotoSK/fyp
Order Matching & Clearing Obligations. Contribute to gotoSK/fyp development by creating an account on GitHub.
yo link khola ta
Anish — Today at 6:54 PM
tei halnu ho
iblamesugam — Today at 6:54 PM
Image
tyo edit garne ma click gara ta
ani tya vako code ctrl+A garera metaidyou sab
garyou?
Anish — Today at 6:55 PM
garyo
iblamesugam — Today at 6:56 PM
document.addEventListener('DOMContentLoaded', function() {
    
    var socket = io();
    
    // Store the last known values
    var uname = sessionStorage.getItem('uname') ? sessionStorage.getItem('uname') : null;
Expand
message.txt
29 KB
ani yo paste gardyou
ani tyo garesi comit changes ma click handyou
Anish — Today at 6:57 PM
gari sakyo
iblamesugam — Today at 7:01 PM
arko app.py ma ni change garya xa. commit garxou?
Anish — Today at 7:02 PM
mathi ko commit garyo
app.py xaina
iblamesugam — Today at 7:03 PM
ah mathi ko ta script.js matra ho
app.py ni garxou vane dinxu tesko code
Anish — Today at 7:03 PM
ahh deu
iblamesugam — Today at 7:03 PM
https://github.com/gotoSK/fyp/blob/main/app.py
GitHub
fyp/app.py at main · gotoSK/fyp
Order Matching & Clearing Obligations. Contribute to gotoSK/fyp development by creating an account on GitHub.
fyp/app.py at main · gotoSK/fyp
agi ko jasri metau. tya vako code jati 
garyou haina?
Anish — Today at 7:05 PM
ahh deu na arko
change garne code
iblamesugam — Today at 7:05 PM
from utils import *
from gen_prices import genPrices
from user import users

import random
import time
Expand
message.txt
24 KB
﻿
iblamesugam
iblamesugam
 
from utils import *
from gen_prices import genPrices
from user import users

import random
import time
from datetime import timedelta

from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from sqlalchemy.exc import IntegrityError


# App setups
print("Configuring App & DB setups ...")
app = Flask(__name__)
socketio = SocketIO(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

app.secret_key = 'your_secret_key'  # Change this to a secure random string


# Defining the database model
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


event_firstEmit = threading.Event()
lock_start = threading.Lock()
lock_db = threading.Lock()
lock_emit = threading.Lock()


def genConID(rem_mkt_order):
    global placedOrders

    if rem_mkt_order == True:
        placedOrders.append([None])

    return datecode + '1' + '0' * (7 - len(str(Orders))) + str(Orders)

def MKT_execute(obj):
    global placedOrders
    i = MKT_Orders[0] # grab order id of this order

    # Order ready to be filled
    if placedOrders[i-1][6] == False:
        placedOrders[i-1][6] = True
        socketio.emit('placed_orders', {'placedOrders': placedOrders})

    # When the best bid/ask qty < mkt order's qty
    if (placedOrders[i-1][4] >= obj.sellOB[0][1] and placedOrders[i-1][5] == 'Buy') or (placedOrders[i-1][4] >= obj.buyOB[0][1] and placedOrders[i-1][5] == 'Sell'):
        # Update LTP & deduct collateral
        if placedOrders[i-1][5] == 'Buy':
            socketio.emit('order_book', {'ltp': obj.sellOB[0][2], 'sym': placedOrders[i-1][1]})
            socketio.emit('deduct_req', {'amt': obj.sellOB[0][2] * obj.sellOB[0][1]})
        else:
            socketio.emit('order_book', {'ltp': obj.buyOB[0][2], 'sym': placedOrders[i-1][1]})

        # Add data to database
        with app.app_context():
            try:
                global Orders
                rand = random.choice(obj.arr)
                if placedOrders[i-1][5] == 'Buy':
                    if placedOrders[i-1][2] == placedOrders[i-1][4]:
                        new_row = PriceRow(conID=genConID(False), buyerID=100, sellerID=rand[3], qty=obj.sellOB[0][1], rate=obj.sellOB[0][2], buyerName=placedOrders[i-1][8], sellerName=rand[8], symbol=obj.arr[0][9])
                    else:
                        Orders += 1
                        new_row = PriceRow(conID=genConID(True), buyerID=100, sellerID=rand[3], qty=obj.sellOB[0][1], rate=obj.sellOB[0][2], buyerName=placedOrders[i-1][8], sellerName=rand[8], symbol=obj.arr[0][9])
                else:
                    if placedOrders[i-1][2] == placedOrders[i-1][4]:
                        new_row = PriceRow(conID=genConID(False), buyerID=rand[2], sellerID=100, qty=obj.buyOB[0][1], rate=obj.buyOB[0][2], buyerName=rand[7], sellerName=placedOrders[i-1][8], symbol=obj.arr[0][9])
                    else:
                        Orders += 1
                        new_row = PriceRow(conID=genConID(True), buyerID=rand[2], sellerID=100, qty=obj.buyOB[0][1], rate=obj.buyOB[0][2], buyerName=rand[7], sellerName=placedOrders[i-1][8], symbol=obj.arr[0][9])
                db.session.add(new_row)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()  # Rollback in case of error
            tranData = PriceRow.query.order_by(PriceRow.id).all()
            tranDataDict = [row.to_dict() for row in tranData] # Convert data to a list of dictionaries
            socketio.emit('floorsheet', {'database': tranDataDict})

        # remaining orders to get filled
        if placedOrders[i-1][5] == 'Buy':
            placedOrders[i-1][4] -= obj.sellOB[0][1]
        else:
            placedOrders[i-1][4] -= obj.buyOB[0][1]
        socketio.emit('placed_orders', {'placedOrders': placedOrders})

        if placedOrders[i-1][4] == 0: # when all qty is filled
            del MKT_Orders[0]

    # When the best bid/ask qty > mkt order's qty
    else:
        # update the top bid/ask
        topAskBid = obj.sellOB if placedOrders[i-1][5] == 'Buy' else obj.buyOB
        topAskBid[0][0] = int(topAskBid[0][0] * (1 - (placedOrders[i-1][4] / topAskBid[0][1]))) if topAskBid[0][0] > 1 else topAskBid[0][0]
        topAskBid[0][1] -= placedOrders[i-1][4]
        if placedOrders[i-1][5] == 'Buy':
            socketio.emit('order_book', {'sellOB': topAskBid, 'ltp': topAskBid[0][2], 'sym': placedOrders[i-1][1]})
            socketio.emit('deduct_req', {'amt': obj.sellOB[0][2] * obj.sellOB[0][1]})
        else:
            socketio.emit('order_book', {'buyOB': topAskBid, 'ltp': topAskBid[0][2], 'sym': placedOrders[i-1][1]})

        # Add data to database
        with app.app_context():
            try:
                rand = random.choice(obj.arr)
                if placedOrders[i-1][5] == 'Buy':
                    if placedOrders[i-1][2] == placedOrders[i-1][4]:
                        new_row = PriceRow(conID=genConID(False), buyerID=100, sellerID=rand[3], qty=placedOrders[i-1][4], rate=obj.sellOB[0][2], buyerName=placedOrders[i-1][8], sellerName=rand[8], symbol=obj.arr[0][9])
                    else:
                        Orders += 1
                        new_row = PriceRow(conID=genConID(True), buyerID=100, sellerID=rand[3], qty=placedOrders[i-1][4], rate=obj.sellOB[0][2], buyerName=placedOrders[i-1][8], sellerName=rand[8], symbol=obj.arr[0][9])
                else:
                    if placedOrders[i-1][2] == placedOrders[i-1][4]:
                        new_row = PriceRow(conID=genConID(False), buyerID=rand[2], sellerID=100, qty=placedOrders[i-1][4], rate=obj.buyOB[0][2], buyerName=rand[7], sellerName=placedOrders[i-1][8], symbol=obj.arr[0][9])
                    else:
                        Orders += 1
                        new_row = PriceRow(conID=genConID(True), buyerID=rand[2], sellerID=100, qty=placedOrders[i-1][4], rate=obj.buyOB[0][2], buyerName=rand[7], sellerName=placedOrders[i-1][8], symbol=obj.arr[0][9])
                db.session.add(new_row)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()  # Rollback in case of error
            tranData = PriceRow.query.order_by(PriceRow.id).all()
            tranDataDict = [row.to_dict() for row in tranData] # Convert data to a list of dictionaries
            socketio.emit('floorsheet', {'database': tranDataDict})

        # all qty filled
        placedOrders[i-1][4] = 0
        socketio.emit('placed_orders', {'placedOrders': placedOrders})
        del MKT_Orders[0]


def orderMatch_sim(obj):

    def genOB(rate):
        # top bid & ask prices in order book
        bidPrices = []; askPrices = []
        bidPrices = genPrices(rate, 'bids', obj.prices)
        askPrices = genPrices(rate, 'asks', obj.prices)

        # generating asks order book
        for i in range(0, TOP_BIDSASKS_NO): # filling each row in order book
            obj.sellOB.append([0, 0, askPrices[i]]) # initializing row data: [orders, qty, price]
            brokers = [] # collects all the brokers in the list for that particular price
            if(i == 0):
                idx = 0
                while(idx < len(obj.arr) and obj.arr[idx][5] == obj.sellOB[i][2]):
                    idx += 1
                idx -= 1
                if(idx != -1):
                    for x in obj.queue:
                        count = -1
                        for y in x:
                            if(obj.sellOB[i][2] == y[5]):
                                obj.sellOB[i][1] += y[4]
                                brokers.append(y[3])
                                count += 1
                                if(count == idx):
                                    break
                        if(obj.sellOB[i][1] != 0):
                            break
            else:
                for x in obj.queue:
                    for y in x:
                        if(obj.sellOB[i][2] == y[5]): # to find orders data realted to current price in queue
                            obj.sellOB[i][1] += y[4] # fetching qty and adding
                            brokers.append(y[3]) # append all brokers
                        else:
                            break
                    if(obj.sellOB[i][1] != 0):
                        break
            if(len(brokers) == 0):
                obj.sellOB[i][1] = int(random.triangular(10, 1300, 200)) # random qty between 10-1300, mostly being of 100-300
                obj.sellOB[i][0] = int(random.triangular(1, 20, 7)) # random qty between 1-20, mostly being around 7
            else:
                obj.sellOB[i][0] = len(obj.remove_duplicates(brokers)) # total orders
        
        # generating bids order book
        for i in range(0, TOP_BIDSASKS_NO):
            obj.buyOB.append([0, 0, bidPrices[i]])
            brokers = []
            for x in obj.queue:
                for y in x:
                    if(obj.buyOB[i][2] == y[5]):
                        obj.buyOB[i][1] += y[4]
                        brokers.append(y[2])
                    else:
                        break
                if(obj.buyOB[i][1] != 0):
                    break
            if(len(brokers) == 0):
                obj.buyOB[i][1] = int(random.triangular(10, 1300, 200))
                obj.buyOB[i][0] = int(random.triangular(1, 20, 7))
            else:
                obj.buyOB[i][0] = len(obj.remove_duplicates(brokers))

        
        with lock_emit:
            if obj.mkt_ex_mode == False:
                socketio.emit('order_book', {'sellOB': obj.sellOB, 'buyOB': obj.buyOB, 'ltp': obj.arr[0][5], 'sym': obj.arr[0][9]})
            else:
                socketio.emit('order_book', {'sellOB': obj.sellOB, 'buyOB': obj.buyOB, 'sym': obj.arr[0][9]})

    def linear_price():
        if len(obj.arr) > 1:
            price_diff = round(obj.arr[1][5] - obj.arr[0][5], 1)
            if abs(price_diff) > 0.3:
                factor = abs(price_diff)*10 - 1
                i = 1 if price_diff>0 else -1

                time_diff = obj.arr[1][6] - obj.arr[0][6]
                time_diff = time_diff.total_seconds()

                def next_rate(i):
                    return round(obj.arr[0][5] + 0.1*i, 1)
                
                while True:
                    flag = 0
                    while next_rate(i) != obj.arr[1][5]:
                        for price in obj.prices:
                            if price == next_rate(i):
                                i = i+1 if i>0 else i-1
                                flag = 1
                                factor += 1
                                break
                        if(flag == 0):
                            break
                        flag = 0
                    if next_rate(i) == obj.arr[1][5]:
                        break
                    obj.sellOB.clear()
                    obj.buyOB.clear()
                    # print("--------------------------------")
                    genOB(next_rate(i))
                    i = i+1 if i>0 else i-1

                    # if there are open market orders of this symbol
                    if len(MKT_Orders) != 0 and placedOrders[MKT_Orders[0] - 1][1] == obj.arr[0][9]:
                        MKT_execute(obj)
                        obj.mkt_ex_mode = True

                    else:
                        if obj.subThreads > 0 or obj.mkt_ex_mode == True:
                            if time_diff/factor > 1:
                                time.sleep(1)
                            else:
                                time.sleep(time_diff/factor)
                        else:
                            if time_diff/factor > 2:
                                time.sleep(time_diff/factor)
                            else:
                                time.sleep(2)
                obj.mkt_ex_mode = False

    def matchOrder():
        if obj.buyOB[0][2] == obj.sellOB[0][2]: # when top bid & ask price match
            for idx, x in enumerate(obj.queue):
                for y in x:
                    if obj.buyOB[0][2] == y[5]:
                        # Add data to database
                        with lock_db:
                            with app.app_context():
                                try:
                                    new_row = PriceRow(conID=y[1], buyerID=y[2], sellerID=y[3], qty=y[4], rate=y[5], buyerName=y[7], sellerName=y[8], symbol=y[9])
                                    db.session.add(new_row)
                                    db.session.commit()
                                except IntegrityError:
                                    db.session.rollback()  # Rollback in case of error
                                    
                                if obj.arr[0][9] == symbol:
                                    tranData = PriceRow.query.order_by(PriceRow.id).all()
                                    tranDataDict = [row.to_dict() for row in tranData] # Convert data to a list of dictionaries
                                    socketio.emit('floorsheet', {'database': tranDataDict})
                            
                        # if a LMT order matches
                        if y[1][8:9] == '1':
                            global placedOrders
                            for indx in range(9, 16):
                                if y[1][indx] != '0':
                                    placedOrders[int(y[1][indx:])-1][4] = 0
                                    socketio.emit('placed_orders', {'placedOrders': placedOrders})

                        linear_price()

                        del obj.queue[idx][0] # delete first order of that price
                        if len(obj.queue[idx]) == 0: # if orders in that price is empty
                            del obj.queue[idx] # delete that element of queue
                            del obj.prices[idx] # delete that particular price from prices list
                        del obj.arr[0]
                        return
                    else:
                        break

    
    with lock_start:
        event_firstEmit.wait()
        socketio.emit('stock_list', {'ltp': obj.arr[0][5], 'sym': obj.arr[0][9], 'scripName': obj.name, 'prevClose': obj.prevClose})

        if obj.arr[0][9] == symbol: # for default asset to display
                socketio.emit('display_asset', {'sym': symbol})

    sym = obj.arr[0][9]
    while len(obj.arr) != 0:
        genOB(obj.arr[0][5])
        matchOrder()
        obj.sellOB.clear()
        obj.buyOB.clear()
        if obj.subThreads > 0:
            obj.event_start_subThread.set()
            obj.event_place_LMT.wait()

            obj.event_start_subThread.clear()
            obj.event_place_LMT.clear()
    print(sym, "Finished matching")
    socketio.emit('finished_matching', {'sym': sym})


def LMT_place(Rate, Qty, OrderNo, type, key):
    OrderData = []
    
    def genTime(idx):
        if idx-1 < 0:
            return assets[key].arr[idx][6] + timedelta(microseconds=-1)
        if idx+1 == len(assets[key].arr):
            return assets[key].arr[idx][6] + timedelta(microseconds=1)
        else:
            return assets[key].arr[idx-1][6] + (assets[key].arr[idx][6] - assets[key].arr[idx-1][6]) / 2

    def write_orderData():
        nonlocal OrderData
        rand = random.choice(assets[key].arr)
        if type == 'Buy':
            OrderData = ['', genConID(False), 100, rand[3], Qty, Rate, genTime(idx), placedOrders[OrderNo-1][8], rand[8], assets[key].arr[0][9]]
        else:
            OrderData = ['', genConID(False), rand[2], 100, Qty, Rate, genTime(idx), rand[7], placedOrders[OrderNo-1][8], assets[key].arr[0][9]]

    def in_the_end():
        global placedOrders
        placedOrders[OrderNo-1][6] = True
        socketio.emit('placed_orders', {'placedOrders': placedOrders})
        assets[key].subThreads -= 1
        if assets[key].subThreads == 0:
            assets[key].event_place_LMT.set()
            assets[key].skip = False
        else:
            assets[key].skip = True

    with lock_orderPlacing[key]:
        if assets[key].skip == False:
            assets[key].event_start_subThread.wait() # wait for main-thread to check if orders have matched before overwriting the new order to the data structure
        
        compare = (lambda x, y: x < y) if type == 'Buy' else (lambda x, y: x > y)
        for idx, next in enumerate(assets[key].arr):
            if compare(next[5], Rate):
                write_orderData()
                assets[key].arr.insert(idx, OrderData)
                encounter = False
                for i, price in enumerate(assets[key].prices):
                    if price == Rate:
                        assets[key].queue[i].insert(0, OrderData)
                        encounter = True
                        break
                    elif price > Rate:
                        assets[key].prices.insert(i, Rate)
                        assets[key].queue.insert(i, [OrderData])
                        encounter = True
                        break
                if encounter == False:
                    assets[key].prices.append(Rate)
                    assets[key].queue.append([OrderData])
                in_the_end()
                return

            elif next[5] == Rate:
                count = 0
                while True:
                    if assets[key].arr[idx+1][5] == Rate:
                        idx += 1
                        count += 1
                    else:
                        write_orderData()
                        assets[key].arr.insert(idx+1, OrderData)
                        for i, price in enumerate(assets[key].prices):
                            if price == Rate:
                                write_orderData()
                                assets[key].queue[i].insert(count+1, OrderData)
                                break
                        break
                in_the_end()
                return

        if type == 'Buy':
            write_orderData()
            assets[key].arr.append(OrderData)
            assets[key].prices.insert(0, Rate)
            assets[key].queue.insert(0, [OrderData])
        else:
            write_orderData()
            assets[key].arr.append(OrderData)
            assets[key].prices.append(Rate)
            assets[key].queue.append([OrderData])
        in_the_end()


# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = users.get(username)

        if user and user.check_password(password):
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

# Net Settlement admin's route
@app.route('/settlement')
def manage_all_users():
    pass

# Home page
@app.route("/")
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("index.html")

# Handle the form submission (AJAX)
@app.route('/place_order', methods=['POST'])
def place_order():
    try:
        global Orders
        
        Rate = float(request.form.get('rate'))
        Qty = int(request.form.get('qty'))
        action = request.form.get('action')  # Get whether it's a buy or sell order
        Orders += 1

        if Rate == 0: # market execution
            placedOrders.append([Orders, symbol, Qty, 'MKT', Qty, action, False, session['username'], users.get(session['username']).name])
            MKT_Orders.append(Orders)
        else: # limit order
            placedOrders.append([Orders, symbol, Qty, Rate, Qty, action, False, session['username'], users.get(session['username']).name])
            for idx, asset in enumerate(assets):
                if asset.arr[0][9] == placedOrders[Orders-1][1]:
                    asset.subThreads += 1
                    threading.Thread(target=LMT_place, args=(Rate, Qty, Orders, action, idx)).start() # run process in background
                    break
        socketio.emit('placed_orders', {'placedOrders': placedOrders})

        return "Order successfully placed", 200
    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging line for error
        return str(e), 400


# Deduct collateral on purchase
@socketio.on('deduct_buy')
def handle_deduction(data):
    deduction = data.get('amt')

    user = users.get(session['username'])
    user.collateral -= deduction

    # Emit updated collateral value to the same client
    if 'username' in session:
        socketio.emit('user_info', {'collateral': user.collateral}, room=request.sid)

# Deduct asset balance on sell
@socketio.on('deduct_sell')
def handle_deduction(data):
    deduction = data.get('qty')

    user = users.get(session['username'])
    user.balance[symbol] -= deduction

    # Emit updated balance to the same client
    if 'username' in session:
        socketio.emit('user_info', {'balance': user.balance}, room=request.sid)


@socketio.on('connect')
def handle_conncet():
    if 'username' in session:
        socketio.emit('user_info', {
            'uname': users.get(session['username']).username,
            'name': users.get(session['username']).name,
            'balance': users.get(session['username']).balance,
            'collateral': users.get(session['username']).collateral
            }, room=request.sid)
        
        socketio.emit('placed_orders', {'placedOrders': placedOrders})

    event_firstEmit.set()

@socketio.on('scrip_selected')
def handle_scrip_selected(data):
    global symbol

    scrip = data.get('scrip')
    
    symbol = scrip


# Runner & debugger
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    print("Creating threads ...")
    for obj in assets:
        threading.Thread(target=orderMatch_sim, args=(obj,)).start()

    socketio.run(app, debug=True, use_reloader=False)
message.txt
24 KB
