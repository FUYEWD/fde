from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/pain-index', methods=['POST'])
def calculate_pain_index():
    data = request.get_json()
    unemployment_rate = data.get('unemployment')
    inflation_rate = data.get('inflation')
    pain_index = unemployment_rate + inflation_rate
    return jsonify({'pain_index': pain_index})


if __name__ == '__main__':
    app.run(debug=True)
