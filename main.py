from flask import Flask, render_template
import json

app = Flask(__name__)


def load_coupons(path='coupons.json'):
    """Load coupon data from a JSON file."""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


@app.route('/')
def index():
    coupons = load_coupons()
    return render_template('index.html', coupons=coupons)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
