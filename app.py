from flask import Flask , render_template , request
from flask import jsonify
from flask_cors import CORS
import azure.cognitiveservices.speech as speechsdk


app = Flask(__name__)
CORS(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True,port=7070,host= '0.0.0.0')

