import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>RotMG Damage Calc</h1><p>This App is my take on a damage calculator for RotMG since the popular one a lot of people used is on flash.</p>"

if __name__ == '__main__':
    app.run()