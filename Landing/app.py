from flask import Flask, render_template, request, redirect, url_for, jsonify

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
    app.run(debug=True)
