from flask import Flask, render_template 
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    today_date = date.today()
    return render_template('index.html', date=today_date)

if __name__ == '__main__':
    app.run(debug=True)
