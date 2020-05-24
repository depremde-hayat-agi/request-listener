from flask import request
import flask
import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '.')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

data_path = os.getenv('DATABASE_PATH')

print(data_path)


port = int(os.environ.get("PORT", 8000))
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "Welcome Corona API"


@app.route('/push', methods=['POST'])
def push():
    eventId = request.form['original_lat']
    userId = request.form['original_long']
    rating = request.form['id']
    return 'Done'


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)
