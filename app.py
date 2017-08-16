from flask import Flask, redirect, render_template
import re
app = Flask(__name__)


@app.route("/")
def usage():
    return render_template('usage.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
