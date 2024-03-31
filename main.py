from flask import Flask, render_template, redirect, url_for, request, session
import request_api
from pprint import pprint

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    if (t := request.args.to_dict()).get("date"):
        print(t)
        data = request_api.func_light_in_one_room(*t['date'].split("-"))
        pprint(data)
        return render_template("main.html", dates=request_api.days_info(),
                               data=data[0], data2=data[1])
    else:
        return render_template("main.html", dates=request_api.days_info())


@app.route("/get_data", methods=["GET"])
def get_data():
    return "123"


if __name__ == "__main__":
    app.run(debug=True, port=5050)
