from flask import Flask, request, jsonify, send_from_directory
from prefect import flow
from pipeline import BandoriTeams  # Adjust the import accordingly


app = Flask(__name__)


@app.route('/')
def index():
    return send_from_directory('', 'index.html')


@app.route('/run-flow', methods=['POST'])
def run_flow():
    name = request.json.get("name", "World")
    result = BandoriTeams()
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
