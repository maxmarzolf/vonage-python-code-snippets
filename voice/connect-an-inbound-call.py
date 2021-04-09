#!/usr/bin/env python3
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/webhooks/answer")
def answer_call():
    ncco = [
        {
            "action": "connect",
            "from": "VONAGE_NUMBER",
            "endpoint": [{
                "type": 'phone',
                "number": "YOUR_SECOND_NUMBER"
            }]
        }
    ]
    return jsonify(ncco)


if __name__ == '__main__':
    app.run(port=3000)
