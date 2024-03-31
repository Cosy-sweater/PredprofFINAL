from flask import Flask, render_template, redirect, url_for, request, session
import request_api

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    default_args = {
        'date': "0-0-0"
    }
    print(request.args.to_dict())

    return render_template("main.html", dates=request_api.days_info())


@app.route("/get_data", methods=["GET"])
def get_data():
    print(app.config)
    return "123"


if __name__ == "__main__":
    app.run(debug=True, port=5050)
