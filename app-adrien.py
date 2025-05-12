from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():

    return "Je fais mon examen 2 ! change diogo"
    return "Je fais mon examen 2 !"
    return "test"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
