from flask import Flask, render_template, request, redirect, url_for, jsonify
import os  # 👈 добавляем импорт os

app = Flask(__name__)

@app.route("/")
def home():
    lang = request.args.get("lang", "ru")
    return render_template("index.html", lang=lang)

@app.route('/ru')
def landing_ru():
    return render_template('index.html', lang='ru')

@app.route('/en')
def landing_en():
    return render_template('index.html', lang='en')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    lang = request.form.get('lang', 'ru')
    if email:
        with open('emails.txt', 'a') as f:
            f.write(email + '\n')
        print(f'New subscriber ({lang}): {email}')
        return jsonify({'message': 'success'}), 200
    return jsonify({'message': 'missing email'}), 400

if __name__ == '__main__':
    # 👇 теперь порт и хост читаются из переменных окружения — это нужно для Render
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

