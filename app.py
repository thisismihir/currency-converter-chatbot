from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
@app.route('/', methods = ['POST'])
def index():
    request_json = request.get_json()
    source_currency = request_json['queryResult']['parameters']['unit-currency']['currency']
    source_amount = request_json['queryResult']['parameters']['unit-currency']['amount']
    destination_currency = request_json['queryResult']['parameters']['currency-name']

    conv = fetch_conversion_rates(source_currency, destination_currency)
    final_amount = round(source_amount * conv, 1)
    response = {
        'fulfillmentText': "{} {} is {} {}".format(source_amount,
                                                    source_currency,
                                                    final_amount,
                                                    destination_currency)
    }
    return jsonify(response)

def fetch_conversion_rates(source, destination):
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_Key}&currencies={
            destination}&base_currency={source}"
    response = requests.get(url)
    response = response.json()
    return response['data'][destination]

if __name__ == '__main__':
    app.run(debug=True)