from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initial stock data
stocks = {
    "Alpha": 100,
    "Beta": 120,
    "Gamma": 85,
    "Delta": 75,
    "Epsilon": 95,
    "Zeta": 105
}

@app.route('/')
def index():
    return render_template('index.html', stocks=stocks)

@app.route('/update', methods=['POST'])
def update():
    for name in stocks:
        new_price = request.form.get(name)
        if new_price:
            stocks[name] = int(new_price)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)