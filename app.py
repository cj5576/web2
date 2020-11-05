from flask import Flask,url_for,redirect,render_template,views,request
import splitList,dlt,ssq

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(dlt.dlt)

app.register_blueprint(ssq.ssq)

if __name__ == '__main__':
    app.run(debug=True)
