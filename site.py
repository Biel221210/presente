from flask import Flask
import random

app = Flask(__name__)

# ---------- PÁGINA PRINCIPAL ----------
@app.route("/")
def home():
    
    frase_inicial = "sudo rm ~/*"

    return f"""
    <html>
        <head>
            <title>.</title>
            <style>
                body {{
                    background: black;
                    color: white;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 60px;
                }}
                h1 {{
                    font-size: 3em;
                }}
                p {{
                    font-size: 1.3em;
                }}
                button {{
                    margin-top: 40px;
                    padding: 15px 35px;
                    font-size: 1.2em;
                    background: red;
                    color: black;
                    border: none;
                    border-radius: 12px;
                    cursor: pointer;
                }}
                button:hover {{
                    background: darkred;
                }}
            </style>
        </head>
        <body>

            <h1>{frase_inicial}</h1>

            <p>
                Ela é dhr.<br>
                Meio resenha.
            </p>

            <a href="/memorias">
                <button>memórias</button>
            </a>

            <a href="/coisas_que_amo">
                <button>Coisas que curto em você</button>
            </a>

        </body>
    </html>
    """

# ---------- PÁGINA DE MEMÓRIAS ----------
@app.route("/memorias")
def memorias():
    return """
    <html>
        <head>
            <title>Memórias</title>
            <style>
                body {
                    background: black;
                    color: white;
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    text-align: center;
                    color: pink;
                }
                .card {
                    margin: 40px auto;
                    max-width: 400px;
                    text-align: center;
                }
                img {
                    width: 100%;
                    border-radius: 20px;
                    box-shadow: 0 0 25px pink;
                }
                p {
                    margin-top: 15px;
                    font-size: 1.1em;
                }
                a {
                    color: white;
                    display: block;
                    text-align: center;
                    margin-top: 50px;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>

            <h1>Dias legais que vc ta neles</h1>

            <div class="card">
                <img src="/static/samy.jpeg">
                <p>
                    Nossa... Como eu to gato nessa foto.
                </p>
            </div>

            <div class="card">
                <img src="/static/samy2.jpeg">
                <p>
                    Um dia, apenas.
                </p>
            </div>

            <div class="card">
                <img src="/static/samy3.jpeg">
                <p>
                    A pessoa rouba meu aparelho pra jogar
                </p>
            </div>

            </div class="card">
                <img src="/static/samy4.jpeg">
                <p>
                    O dia que eu perdi o BV.
                </p>
            </div>

            </div class="card">
                <img src="/static/samy5.jpeg">
                <p>
                    O primeiro rolê nosso juntos.
                </p>
            </div>

            <a href="/">⬅ Voltar</a>

        </body>
    </html>
    """

# ---------- START DO SERVIDOR ----------
if __name__ == "__main__":
    app.run(port=5000, debug=False)
