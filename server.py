from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    contract_account = request.args.get('contractAccount')
    

    print(f'contractAccount={contract_account}')

    url = f'https://www.se.com.sa/api/BillDetails/GetViewBillGuest?contractAccount={contract_account}'
    response = requests.get(url)
    print("=================================Response===================================================")
    print(response.text)
    print("=================================END Response===================================================")

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
