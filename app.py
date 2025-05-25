from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Initial stock prices
stock_prices = {
    "Wockhardt": 20,
    "HDFC": 25,
    "Tata": 40,
    "ONGC": 55,
    "Relaince": 75,
    "Infosys": 80
}

@app.route('/')
def index():
    is_admin = request.args.get('admin') == 'true'
    return render_template('index.html', stocks=stock_prices, admin=is_admin)

@socketio.on('update_stock')
def update_stock(data):
    name = data['name']
    price = data['price']
    stock_prices[name] = price
    emit('stock_update', {name: price}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=9000)