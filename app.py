from flask import Flask, jsonify
from flask.globals import request

app = Flask(__name__)

data = {
    "200000": 1,
    "201010": 10,
    "200028": 100,
    "180199": 1000
}

error = {
    "Error": "No record available"
}


@app.route('/coins', methods=['GET'])
def coinsGet():
    return "POST methods only!"


@app.route('/coins', methods=['POST'])
def coins():
    dt = dict(request.get_json())
    query = dt["rollno"]

    assert(type(query) == str)

    if query in data:
        return jsonify({
            "coins": data[query]
        })
    else:
        return jsonify(error)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
