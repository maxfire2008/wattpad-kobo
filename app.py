import flask

app = flask.Flask(__name__)
app.jinja_options["autoescape"] = lambda _: True

@app.route("/")
def index():
    return flask.render_template("index.html.j2")

@app.route("/share-target/")
def share_target():
    print(flask.request.params)
