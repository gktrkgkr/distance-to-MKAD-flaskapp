import os
from flask import Flask, render_template
from blueprint import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix="")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)))
