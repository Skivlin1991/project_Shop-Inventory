from flask import Flask, render_template

from controllers.stock_controller.py import stock_blueprint


app = Flask(__name__)

app.register_blueprint(stock_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)