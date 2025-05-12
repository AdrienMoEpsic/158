from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():

    return "voici le test de la branche (Adrien)2 !"

    return "Je fais mon examen 2 ! change diogo"
    return "Je fais mon examen 2 !"
    return "test Arthur"


 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
