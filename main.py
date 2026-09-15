from flask import Flask, render_template, request
app = Flask(__name__)

# --- HOME ---
@app.route('/')
def home():
    return render_template('home')

# --- TELA LOGIN ---

# --- TELA CADASTRO ---




if __name__ == '__main__':
    app.run()