from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():

    return "voici le test de la branche (Adrien)2 !"
    return "t'as pas une clope ?"
    return "Je fais mon examen 2 ! change diogo"
    return "Je fais mon examen 2 !"
    return "test Arthur"
    return "test test Patrick"
    return "Deuxième ligne - Diogo"
    return "une autre ligne - Patrick"
    return "JE VEUX TERMINER CETTE DEUXIEME ANNEE ALED from CLI pitié2 - Monia2"
    return "Force à toi Monia - Besim" 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
