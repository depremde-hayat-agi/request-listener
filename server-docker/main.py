from flask import jsonify, request
import flask
import os


port = int(os.environ.get("PORT", 8000))
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "Welcome Corona API"


@app.route('/ts', methods=['GET'])
def push():
    filter_case = int(request.args['caseMore']) if 'caseMore' in request.args else 0
    index_case = int(request.args['indexCase']) if 'indexCase' in request.args else 100
    return jsonify({'a':1})

#
# @app.route('/summary', methods=['GET'])
# def get():
#     pass

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)
