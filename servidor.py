from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/alerta", methods=["GET"])
def alerta():
    return jsonify({
        "actual": {
            "nivel": "ninguna",
            "proxima": 1
        }
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)