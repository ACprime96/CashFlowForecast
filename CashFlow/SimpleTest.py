from flask import Flask, request, jsonify
from CashFlow_Forecast import cashflow_forecast
import sys

app = Flask(__name__)

@app.route("/cash", methods=['POST', 'GET'])
def index():
    try:
        dict = cashflow_forecast()
        return jsonify(dict)
    except:
        return ("Unexpected error:", sys.exc_info()[0])

if __name__ == '__main__':
    app.run()
