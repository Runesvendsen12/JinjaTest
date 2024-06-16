import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("base.html", title="Jenny's Server")

if __name__ == "__main__":
    app.run(debug=True)

#url http://localhost:5000/