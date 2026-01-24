from flask import Flask
import random

app = Flask(__name__)

# ---------- PÁGINA PRINCIPAL ----------
@app.route("/")
def home():
    frases_iniciais = [
        "NOS AMAMOS A SAMY!! ❤️",
        "SAMY É A MELHOR PESSOA DO MUNDO!! ❤️",
        "EU TE AMO MAIS DO QUE TUDO ❤️"
    ]

    frase = random.choice(frases_iniciais)

    return f"""
    <html>
        <head>
            <title>❤️</title>
            <style>
                body {{
                    background: white;
                    color: pink;
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

            <h1>{frase}</h1>

            <p>
                ELA É TÃO INCRÍVEL QUE EU NÃO CONSIGO NEM DESCREVER.<br>
                É COM ELA QUE EU QUERO PASSAR O RESTO DA MINHA VIDA.
            </p>

            <p>
                SEM PARANOIAS.<br>
                SÓ AMOR. TODO O AMOR QUE EU TENHO PRA DAR.
            </p>

            <a href="/memorias">
                <button>Ver nossas memórias 💭</button>
            </a>

            <a href="/coisas_que_amo">
                <button>Coisas que amo em você ❤️</button>
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
            <title>Memórias ❤️</title>
            <style>
                body {
                    background: white;
                    color: pink;
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
                    box-shadow: 0 0 25px red;
                }
                p {
                    margin-top: 15px;
                    font-size: 1.1em;
                }
                a {
                    color: pink;
                    display: block;
                    text-align: center;
                    margin-top: 50px;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>

            <h1>Os melhores dias da minha vida</h1>

            <div class="card">
                <img src="/static/samy.jpeg">
                <p>
                    Minha foto favorita nossa.
                    Ta até como gif de boot no meu aparelho.
                </p>
            </div>

            <div class="card">
                <img src="/static/samy2.jpeg">
                <p>
                    Um dos melhores dias da minha vida.
                    Só nós dois, curtindo despreucupados.
                </p>
            </div>

            <div class="card">
                <img src="/static/samy3.jpeg">
                <p>
                    A pessoa rouba meu aparelho pra jogar
                    joguinho kkkkkk e ainda pra me humilhar kkkk
                </p>
            </div>

            </div class="card">
                <img src="/static/samy4.jpeg">
                <p>
                    O dia do nosso primeiro beijo.
                    14/12/2024 - Nunca vou esquecer.
                </p>
            </div>

            </div class="card">
                <img src="/static/samy5.jpeg">
                <p>
                    O primeiro rolê nosso juntos, só nós.
                </p>
            </div>

            <a href="/">⬅ Voltar</a>

        </body>
    </html>
    """

@app.route("/coisas_que_amo")
def coisas_que_amo():
    return """
    <html>
        <head>
            <title>Coisas que amo em você ❤️</title>
            <style>
                body {
                    background: white;
                    color: pink;
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
                    box-shadow: 0 0 25px red;
                }
                p {
                    margin-top: 15px;
                    font-size: 1.1em;
                }
                a {
                    color: pink;
                    display: block;
                    text-align: center;
                    margin-top: 50px;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>

            <h1>Coisas que amo em você ❤️</h1>

            <div class="card">
                <p>
                    Sua risada, sua voz, seu jeitinho.
                </p>
            </div>

            <div class="card">
                <p>
                    Sua maneira de ser. Seus olhos
                </p>
            </div>

            <div class="card">
                <p>
                    Sua fé. Seu jeito único de me acalmar.
                </p>
            </div>

            </div class="card">
                <p>
                    Sua paciência, seu amor, sua presença.
                </p>
            </div>

            </div class="card">
                <p>
                    Sua coragem, sua determinação, seu espírito.
                </p>
            </div>

            <a href="/">⬅ Voltar</a>

        </body>
    </html>
    """

# ---------- START DO SERVIDOR ----------
if __name__ == "__main__":
    app.run(port=5000, debug=False)
