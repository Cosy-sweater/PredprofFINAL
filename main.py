from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)


# @app.route('/')
# def main():
#     if 'username' in session:
#         username = session['username']
#         is_admin = is_user_admin(username)
#         return render_template('main.html', username=username, is_admin=is_admin)
#     return render_template('main.html')


@app.route("/", methods=["GET"])
def main():
    return render_template("main.html", dates=[123, 456, 798])


@app.route("/test", methods=["GET"])
def test():
    print(123)
    return render_template("test.html")


@app.route("/get_data", methods=["GET"])
def get_data():
    return "123"


if __name__ == "__main__":
    app.run(debug=True, port=5050)
