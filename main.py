import stripe
from flask import Flask, jsonify, request, render_template, url_for, redirect
import os
import json

stripe.api_key = 'sk_test_51IymvIFaKZXpq6rXs2XcaO55i78p9kgTVkXSbhki1UZGk663XsLY1Se2c2kg47nzgCxCxwdkxsitrtizuBDEupYz00M7hTrgrn'

price = 0

app = Flask(__name__,
            static_url_path='',
            static_folder='.')

YOUR_DOMAIN = 'http://localhost:4242'


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


dict_of_items = {"arduino": 25,
                 "circuit_1": 5,
                 "circuit_2": 10,}


def calculate_order_amount():
    return 2500


@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        data = json.loads(request.data)
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(),
            currency='usd'
        )

        return jsonify({
          'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403


if __name__ == '__main__':
    app.run(port=4242, debug=True)

