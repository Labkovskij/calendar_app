from flask import Flask, render_template 
from datetime import date
import os # додали цей імпорт для рендер

app = Flask(__name__)

@app.route('/')
def home():
    today_date = date.today()
    return render_template('index.html', date=today_date)

if __name__ == '__main__':
     # Отримуємо порт із змінної середовища, або використовуємо 5000 за замовчуванням
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)