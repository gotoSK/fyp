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
﻿
iblamesugam
iblamesugam
 
document.addEventListener('DOMContentLoaded', function() {
    
    var socket = io();
    
    // Store the last known values
    var uname = sessionStorage.getItem('uname') ? sessionStorage.getItem('uname') : null;
    let balances = sessionStorage.getItem('balances') ? JSON.parse(sessionStorage.getItem('balances')) || {} : {}; // {'asset1':xxx, 'asset2':xxx, ...}
    let collateral = sessionStorage.getItem('collateral') ? parseFloat(sessionStorage.getItem('collateral')) : 0.0;  // symbol that is being displayed

    var dataMat = sessionStorage.getItem('dataMat') ? JSON.parse(sessionStorage.getItem('dataMat')) || [] : [];  // [LTP, Symbol, Name, PrevClose, [chart plots]] for each stock

    var symbol = sessionStorage.getItem('symbol') ? sessionStorage.getItem('symbol') : null;  // symbol that is being displayed

    var lastSellOB = sessionStorage.getItem('lastSellOB') ? JSON.parse(sessionStorage.getItem('lastSellOB')) || [] : []; 
    var lastBuyOB = sessionStorage.getItem('lastBuyOB') ? JSON.parse(sessionStorage.getItem('lastBuyOB')) || [] : [];
    
    var lastDatabase = sessionStorage.getItem('lastDatabase') ? JSON.parse(sessionStorage.getItem('lastDatabase')) || [] : [];
    
    var placedOrders = sessionStorage.getItem('placedOrders') ? JSON.parse(sessionStorage.getItem('placedOrders')) || [] : [];
    
    let lastCheckTime = sessionStorage.getItem('lastCheckTime') ? sessionStorage.getItem('lastCheckTime') : Date.now();
    var labels = sessionStorage.getItem('labels') ? JSON.parse(sessionStorage.getItem('labels')) || [] : [];  // For x-axis labels (timestamps)
    
    var ctx = document.getElementById('priceChart').getContext('2d');  // Get the canvas context for drawing the chart


    // Listen for user_info event from Flask
    socket.on("user_info", function (data) {
        // Update username
        if (data.uname) {
            uname = data.uname;
            sessionStorage.setItem('uname', uname);
        }

        // Update user's name
        if (data.name) {
            document.getElementById("user-name").innerText = `${data.name}`;
        }
        
        // Update collateral display
        if (data.collateral) {
            collateral = data.collateral;
            sessionStorage.setItem("collateral", collateral);
            document.getElementById("collateral-display").innerText = `Collateral: NPR ${collateral.toFixed(2)}`;
        }
        
        // Update balance list
        if (data.balance) {
            balances = data.balance;
            sessionStorage.setItem('balances', JSON.stringify(balances));
            let balancesList = document.getElementById("balances");
            balancesList.innerHTML = ""; // Clear previous values
    
            for (let asset in balances) {
                let listItem = document.createElement("li");
                listItem.innerText = `${asset}: ${balances[asset]}`;
                balancesList.appendChild(listItem);
            }
        }
    });

    // Collateral deduction request from server for market orders
    socket.on("deduct_req", function (data) {
        let amt = data.amt
        socket.emit('deduct_buy', { amt });
    });


    function load_exploreTab() {
        // Get the class 'explore' element
        const exploreElement = document.querySelector('.explore');
    
        // Clear any existing rows to avoid duplication
        exploreElement.innerHTML = `
            <div class="header">
                <span>Scrip</span>
                <span>LTP</span>
                <span>% Change</span>
            </div>
        `;
    
        // Track the currently selected row
        let selectedRow = null;
    
        // Loop through the dataMat and add rows dynamically
        dataMat.forEach((row, index) => {
            const scrip = row[1];
            const ltp = row[0];
            const pC = row[3];
            change = (((ltp - pC) / pC) * 100);
            const percentChange = change > 0 ? '+' + change.toFixed(2) : change.toFixed(2);
    
            // Create a new row
            const rowElement = document.createElement('div');
            rowElement.classList.add('row');
            rowElement.setAttribute('data-scrip', scrip); // Store the scrip as a custom attribute
            rowElement.innerHTML = `
                <span>${scrip}</span>
                <span>${ltp}</span>
                <span>${percentChange}%</span>
            `;
    
            // Check if this row should be selected by default
            if (scrip === symbol) {
                rowElement.classList.add('selected');
                selectedRow = rowElement; // Set as the initially selected row
            }
    
            // Add an event listener for clicks
            rowElement.addEventListener('click', () => {
                // Remove 'selected' class from the previously selected row
                if (selectedRow) {
                    selectedRow.classList.remove('selected');
                }
    
                // Highlight the currently selected row
                rowElement.classList.add('selected');
                selectedRow = rowElement; // Update the selectedRow variable
    
                socket.emit('scrip_selected', { scrip });
    
                // Update the page
                symbol = scrip;
                sessionStorage.setItem('symbol', symbol);
                load_topbar();
    
                lastBuyOB = [];
                lastSellOB = [];
                sessionStorage.setItem('lastSellOB', JSON.stringify(lastSellOB));
                sessionStorage.setItem('lastBuyOB', JSON.stringify(lastBuyOB));
                document.getElementById('order-book-table-body').innerHTML = '';
                
                updateChart(symbol);
                load_Floorsheet();
            });
    
            // Append the row to the exploreElement
            exploreElement.appendChild(rowElement);
        });
    } load_exploreTab();    

    socket.on('stock_list', function(data) {
        dataMat.push([data.ltp, data.sym, data.scripName, data.prevClose, []]);
        
        sessionStorage.setItem('dataMat', JSON.stringify(dataMat));

        load_exploreTab();
    });

    socket.on('display_asset', function(data) {
        symbol = data.sym;
        
        sessionStorage.setItem('symbol', symbol);

        load_topbar();
    });
    
    function load_topbar() {
        var stockInfo = document.getElementById('stock-info');
        stockInfo.innerHTML = '';  // Clear current content

        for (let x of dataMat) {
            if (symbol == x[1]) {
                // Insert Symbol
                var col = document.createElement('div');
                col.textContent = symbol;
                stockInfo.appendChild(col);
        
                // Insert Security's Name
                var col = document.createElement('div');
                col.textContent = x[2];
                stockInfo.appendChild(col);
        
                // Insert price (LTP)
                col = document.createElement('div');
                col.textContent = x[0];
                stockInfo.appendChild(col);
                
                // Insert %change
                col = document.createElement('div');
                change = ((x[0] - x[3]) / x[3]) * 100;
                if (change > 0) {
                    col.textContent = '+' + change.toFixed(2) + '%';
                }
                else {
                    col.textContent = change.toFixed(2) + '%';
                }
                stockInfo.appendChild(col);
        
                // Insert Prev. Day's Closing Price
                col = document.createElement('div');
                col.textContent = 'Pre Close: ' + x[3];
                stockInfo.appendChild(col);

                break;
            }
        }
        
    } load_topbar();


    function load_OrderBook() {
        var orderBookTableBody = document.getElementById('order-book-table-body');
        orderBookTableBody.innerHTML = '';  // Clear current table content

        var sellOrders = lastSellOB.slice().reverse();

        // Insert rows for flipped 'sellOB'
        sellOrders.forEach(function(order) {
            var row = document.createElement('tr');
            order.forEach(function(value) {
                var cell = document.createElement('td');
                cell.textContent = value;
                row.appendChild(cell);
            });
            orderBookTableBody.appendChild(row);
        });
        
        // Insert a single row for 'LTP'
        for (let x of dataMat) {
            if (x[1] == symbol) {
                var ltpRow = document.createElement('tr');
                var ltpCell = document.createElement('td');
                ltpCell.setAttribute('colspan', '3');  // Make it span 3 columns
                ltpCell.textContent = 'LTP: ' + x[0];
                ltpCell.style.textAlign = 'left';  // Align LTP to the left
                ltpRow.appendChild(ltpCell);
                orderBookTableBody.appendChild(ltpRow);
                break;
            }
        }

        // Insert rows for 'buyOB'
        lastBuyOB.forEach(function(order) {
            var row = document.createElement('tr');
            order.forEach(function(value) {
                var cell = document.createElement('td');
                cell.textContent = value;
                row.appendChild(cell);
            });
            orderBookTableBody.appendChild(row);
        });
    } load_OrderBook();

    function ext_pricePlots(sym) {
        if (!sym) {
            for (let x of dataMat) {
                if (x[1] == symbol) {
                    return x[4];
                }
            }
            return [];
        }
        else {
            for (let x of dataMat) {
                if (x[1] == sym) {
                    return [x[0], x[3], x[4]];
                }
            }
        }
    }
    
    // Create a real-time line chart
    var priceChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,  // X-axis labels
            datasets: [{
                label: 'Stock Price',  // Name of the dataset
                data: ext_pricePlots(),  // Y-axis data for LTP arr
                borderColor: function() {
                    pricePlots = ext_pricePlots();
                    // if price is above day's open then green else red
                    return pricePlots[pricePlots.length - 1] >= pricePlots[1] ? 'rgba(0, 200, 0, 1)' : 'rgba(200, 0, 0, 1)';
                },  // Line color
                backgroundColor: function() {
                    var gradient = ctx.createLinearGradient(0, 0, 0, 400);  // Create a gradient background for the line
                    pricePlots = ext_pricePlots();
                    if (pricePlots[pricePlots.length - 1] >= pricePlots[1]) {  // if price is above day's open then green else red
                        // Green gradient for upward trend
                        gradient.addColorStop(0, 'rgba(0, 200, 0, 0.3)');
                        gradient.addColorStop(1, 'rgba(0, 200, 0, 0)');
                    } else {
                        // Red gradient for downward trend
                        gradient.addColorStop(0, 'rgba(200, 0, 0, 0.3)');
                        gradient.addColorStop(1, 'rgba(200, 0, 0, 0)');
                    }
                    return gradient;
                },
                borderWidth: 2,  // Line width
                fill: true,  // Don't fill the area under the line
                pointRadius: function(context) {
                    pricePlots = ext_pricePlots();
                    // Show a point only on the last data point
                    return context.dataIndex === pricePlots.length - 1 ? 5 : 0;
                },
                pointHoverRadius: 3,  // Hover effect on the last point
                pointBackgroundColor: function() {
                    pricePlots = ext_pricePlots();
                    // if price is above day's open then green else red
                    return pricePlots[pricePlots.length - 1] >= pricePlots[1] ? 'rgba(0, 200, 0, 1)' : 'rgba(200, 0, 0, 1)';
                },  // Color for the last point
                pointBorderWidth: function(context) {
                    pricePlots = ext_pricePlots();
                    // Make the last point thicker
                    return context.dataIndex === pricePlots.length - 1 ? 1 : 0;
                }
            }]
        },
        options: {
            scales: {
                x: {
                    grid: {
                        display: false,  // Hide gridlines for X-axis
                    },
                    ticks: {
                        color: '#ccc',  // X-axis label color
                        display: false
                    }
                },
                y: {
                    position: 'right', // Position price scale on the right side
                    grid: {
                        display: false,  // Hide gridlines for Y-axis
                    },
                    ticks: {
                        color: '#ccc'  // Y-axis label color
                    },
                    beginAtZero: false  // Stock prices don't start from zero
                }
            },
            plugins: {
                legend: {
                    display: false  // Disable legend to simplify the chart
                },
                tooltip: {
                    mode: 'index',  // Show all points at the same index
                    intersect: false,  // Show the tooltip on hover regardless of exact point
                    usePointStyle: true,  // Use point style in tooltip
                    callbacks: {
                        label: function(tooltipItem) {
                            return ' NPR ' + tooltipItem.raw;  // Custom label in tooltip
                        }
                    }
                }
            },
            elements: {
                line: {
                    tension: 0.4  // Smooth out the line
                }
            },
            hover: {
                mode: 'index',  // Show tooltip and hover effect on closest point along x-axis
                intersect: false  // Activate hover effect even when not intersecting with the line
            }
        }
    });

    function load_Floorsheet() {
        var floorsheetTableBody = document.getElementById('floorsheet-table-body');
        floorsheetTableBody.innerHTML = '';  // Clear current floorsheet table content

        // Use provided database or fallback to last known database
        var floorsheetData = lastDatabase.slice().reverse();

        // Insert rows for floorsheet with updated format
        floorsheetData.forEach(function(entry) {
            var row = document.createElement('tr');
            
            if (entry.symbol == symbol) {
                // Calculate amount = qty * rate
                var amount = entry.qty * entry.rate;

                // Add cells for each column
                var idCell = document.createElement('td');
                idCell.textContent = entry.id;
                row.appendChild(idCell);

                var conIDCell = document.createElement('td');
                conIDCell.textContent = entry.conID;
                row.appendChild(conIDCell);

                var qtyCell = document.createElement('td');
                qtyCell.textContent = entry.qty;
                row.appendChild(qtyCell);

                var rateCell = document.createElement('td');
                rateCell.textContent = entry.rate;
                row.appendChild(rateCell);

                var amountCell = document.createElement('td');
                amountCell.textContent = amount.toFixed(2);  // Keep 2 decimal places for amount
                row.appendChild(amountCell);

                var buyerNameCell = document.createElement('td');
                buyerNameCell.textContent = entry.buyerName;
                row.appendChild(buyerNameCell);

                var sellerNameCell = document.createElement('td');
                sellerNameCell.textContent = entry.sellerName;
                row.appendChild(sellerNameCell);

                floorsheetTableBody.appendChild(row);
            }
        });
    } load_Floorsheet();

    function updateChart(sym) {
        const currentTime = Date.now();
        pricePlots = ext_pricePlots(sym);  // [LTP, PrevClose, chart-plots]

        // if time within 1 minu. interval
        if (currentTime-lastCheckTime < 60000) {
            // Add the new LTP value to the chart data
            if (pricePlots[2].length == 0){
                pricePlots[2].push(pricePlots[1]);  // fill first index of chart as previous closing price
                pricePlots[2].push(pricePlots[0]);  // fill second index of chart as the first LTP of the day
            }
            else pricePlots[2][pricePlots[2].length - 1] = pricePlots[0];  // fill rest of the indices of chart as incoming LTPs
            sessionStorage.setItem('dataMat', JSON.stringify(dataMat));
            
            // Add label (time for the x-axis)
            if (labels.length == 0) {
                labels.push('');  // this label is empty for the previous day's close which is the first plotted price on chart
                labels.push(new Date().toLocaleTimeString());  // print time label
                labels.push('');  // leave a gap from last plotted price
                sessionStorage.setItem('labels', JSON.stringify(labels));
            }
        }

        // if 1 minu. interval finished
        else {
            lastCheckTime = currentTime;
            labels[labels.length-1] = new Date().toLocaleTimeString();
            labels.push('');
            dataMat.forEach(x => {
                x[4].push(x[0]);
            });
            sessionStorage.setItem('lastCheckTime', lastCheckTime);
            sessionStorage.setItem('dataMat', JSON.stringify(dataMat));
            sessionStorage.setItem('labels', JSON.stringify(labels));
        }
        if (sym == symbol)  priceChart.update();
    }

    function load_placedOrders() {
        // Clear the current table content
        $('#open-orders-table-body').empty();
        $('#filled-orders-table-body').empty();

        placedOrders.forEach(function(order) {
            if (order && order[7] == uname) {
                var row = '<tr>' +
                    '<td>' + order[1] + '</td>' + // Symbol
                    '<td>' + order[2] + '</td>' + // Qty
                    '<td>' + order[3] + '</td>' + // Rate
                    '<td>' + order[4] + '</td>' + // Rem.
                    '<td>' + order[5] + '</td>';  // Type (Buy/Sell)

                // If Success is False, show loading circle
                if (!order[6]) {
                    row += '<td><div class="loading-circle"></div></td>';
                }
                else{
                    row += '<td>Yes</td>';
                }
                
                row += '</tr>';
                // If Rem. is greater than 0, it's an open order
                if (order[4] > 0) {
                    $('#open-orders-table-body').append(row);
                } else {
                    $('#filled-orders-table-body').append(row);
                }
            }
        });
    } load_placedOrders();


    // Listen for 'order_book' event from the server
    socket.on('order_book', function(data) {
        // Update last known values if new data is provided
        if (data.sym == symbol) {
            if (data.sellOB) {
                lastSellOB = data.sellOB;
                sessionStorage.setItem('lastSellOB', JSON.stringify(lastSellOB));
            }
            if (data.buyOB) {
                lastBuyOB = data.buyOB;
                sessionStorage.setItem('lastBuyOB', JSON.stringify(lastBuyOB));
            }
        }
        if (data.ltp) {
            for (let x of dataMat) {
                if (x[1] == data.sym) {
                    x[0] = data.ltp;
                    break;
                }
            }
            sessionStorage.setItem('dataMat', JSON.stringify(dataMat));
        }

        load_OrderBook();
        updateChart(data.sym);
        load_topbar();
        load_exploreTab();
    });

    // Listen for 'floorsheet' event from the server
    socket.on('floorsheet', function(data) {
        // Update last known database if new data is provided
        lastDatabase = data.database;
        
        sessionStorage.setItem('lastDatabase', JSON.stringify(lastDatabase));

        load_Floorsheet();
    });

    // Toggle between Chart, Database and Stats
    $('#chart-container-btn').click(function() {
        $(this).addClass('active');
        $('#database-container-btn').removeClass('active');
        $('#stats-container-btn').removeClass('active');
        $('#chart-container').show();
        $('#database-container').hide();
        $('#stats-container').hide();
    });
    $('#database-container-btn').click(function() {
        $(this).addClass('active');
        $('#chart-container-btn').removeClass('active');
        $('#stats-container-btn').removeClass('active');
        $('#chart-container').hide();
        $('#database-container').show();
        $('#stats-container').hide();
    });
    $('#stats-container-btn').click(function() {
        $(this).addClass('active');
        $('#chart-container-btn').removeClass('active');
        $('#database-container-btn').removeClass('active');
        $('#chart-container').hide();
        $('#database-container').hide();
        $('#stats-container').show();
    });

    // Handle form submission via AJAX to avoid page reload
    $('.order-form').on('submit', function(event) {
        event.preventDefault();  // Prevent default form submission
        var formData = $(this).serialize();  // Serialize the form data
        var form = $(this); // Save reference to the current form

        // Validate before sending AJAX request
        var rate = parseFloat(form.find('#rate').val());
        var qty = parseInt(form.find('#qty').val());
        var action = form.find('input[name="action"]').val();
        
        // Validation
        if (rate != 0) {
            if (action == 'Buy' && rate > lastSellOB[0][2]) {
                alert('Buy Limit exceeds top bid price');
                return;
            }
            else if (action == 'Sell' && rate < lastBuyOB[0][2]) {
                alert('Sell Limit falls short to top ask price');
                return;
            }

            for (let x of dataMat) {
                if (x[1] == symbol) {
                    prevClose = x[3];
                    break;
                }
            }
            let p1 = (prevClose*0.9).toString();
            let decimalIndex = p1.indexOf('.');
            if (decimalIndex !== -1 && p1.length - decimalIndex - 1 === 2) {
                p1 = parseFloat(p1.slice(0, -1)) + 0.1;prevClose
            } else {
                p1 = parseFloat(p1.slice(0, -1));
            }
            let p2 = (prevClose*1.1).toString();
            decimalIndex = p2.indexOf('.');
            if (decimalIndex !== -1 && p2.length - decimalIndex - 1 === 2) {
                p2 = parseFloat(p2.slice(0, -1));
            }
            if (rate < p1 || rate > p2) {
                alert(`You're breaking circuit. Rate must be within (${p1}(${prevClose*0.9}) - ${p2}(${prevClose*1.1})).`);
                return;
            }
            if (!/^\d+(\.\d{1})?$/.test(rate)) {
                alert(`Rate must be multiple of 0.1. ${rate}`);
                return;
            }
        }

        if (qty < 10) {
            alert('Quantity must be of at least 10 units.');
            return;
        }
        
        // Validating with user balance and collateral
        if (action == 'Sell') { // Limit/Market sell
            if (qty > balances[symbol]) {
                alert(`Sell amount exceeds your balance! Your balance for ${symbol}: ${balances[symbol]}`);
                return;
            }
        }
        if (action == 'Buy') { // Limit Buy
            if (rate != 0 && rate*qty > collateral) {
                alert(`Buy amount exceeds your collateral! Your collateral: NPR ${collateral}`);
                return;
            }
            else if (rate == 0) { // Market Buy
                // set price as the lower circuit for conservative estimation of the market order's rate
                let mktRate = dataMat.find(asset => asset[1] == symbol) [3] * 0.9 
                if (mktRate * qty > collateral) {
                    alert(`Buy amount exceeds your collateral! Your collateral: NPR ${collateral}`);
                    return;
                }
            }
        }

        // Deducting collateral
        if (action == 'Buy') {
            let amt = qty * rate;
            if (amt != 0) { // Limit order (for market orders deduction occurs when order is filled at market price)
                collateral -= amt;
                sessionStorage.setItem("collateral", collateral);
                // Emit deduction event to Flask
                socket.emit('deduct_buy', { amt });
            }
        }
        // Deducting asset balance
        if (action == 'Sell') {
            balances[symbol] -= qty
            sessionStorage.setItem('balances', JSON.stringify(balances));
            socket.emit('deduct_sell', { qty });
        }

        // Submit form data via AJAX
        $.ajax({
            url: '/place_order',
            method: 'POST',
            data: formData,
            success: function(response) {
                alert(action + ' order placed successfully!');
                form.find('input[type="number"]').val('');  // Clear the rate and quantity inputs
            },
            error: function(error) {
                alert('Error placing ' + action + ' order.');
            }
        });
    });

    // Toggle between Limit Order and Market Execution forms
    $('#limit-order-btn').click(function() {
        $(this).addClass('active');
        $('#market-execution-btn').removeClass('active');
        $('#limit-order-form').show();
        $('#market-execution-form').hide();
    });
    $('#market-execution-btn').click(function() {
        $(this).addClass('active');
        $('#limit-order-btn').removeClass('active');
        $('#market-execution-form').show();
        $('#limit-order-form').hide();
    });

    // Listen for 'placed_orders' event from the server
    socket.on('placed_orders', function(data) {
        if (data.placedOrders) placedOrders = data.placedOrders;
        sessionStorage.setItem('placedOrders', JSON.stringify(placedOrders));
        load_placedOrders();
    });

    // Toggle between "Open Orders" and "Filled Orders"
    $('#open-orders-btn').click(function() {
        $(this).addClass('active');
        $('#filled-orders-btn').removeClass('active');
        $('#open-orders').show();
        $('#filled-orders').hide();
    });
    $('#filled-orders-btn').click(function() {
        $(this).addClass('active');
        $('#open-orders-btn').removeClass('active');
        $('#filled-orders').show();
        $('#open-orders').hide();
    });
    
    socket.on('finished_matching', function(data) {
        for (let i in dataMat) {
            if (dataMat[i][1] == data.sym) {
                dataMat.splice(i, 1);
                sessionStorage.setItem('dataMat', JSON.stringify(dataMat));
                break;
            }
        }
        load_exploreTab();
    });

    // ensure the chart values are saved before the page is unloaded (for data integrity &/or backup for unexpected interruptions)
    window.addEventListener("beforeunload", function () {
        sessionStorage.setItem('uname', uname);
        sessionStorage.setItem('balances', JSON.stringify(balances));
        sessionStorage.setItem("collateral", collateral);
        sessionStorage.setItem('dataMat', JSON.stringify(dataMat));
        sessionStorage.setItem('symbol', symbol);
        sessionStorage.setItem('lastSellOB', JSON.stringify(lastSellOB));
        sessionStorage.setItem('lastBuyOB', JSON.stringify(lastBuyOB));
        sessionStorage.setItem('lastDatabase', JSON.stringify(lastDatabase));
        sessionStorage.setItem('lastCheckTime', lastCheckTime);
        sessionStorage.setItem('labels', JSON.stringify(labels));
        sessionStorage.setItem('placedOrders', JSON.stringify(placedOrders));
    });
});
message.txt
29 KB
