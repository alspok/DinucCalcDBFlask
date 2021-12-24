
from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def main():
#   return "Hello World, hello evrybody and evryone!"
    with open("access_id", "r") as fh:
        file_lines = fh.readlines()

    return render_template("main.html", file_lines = file_lines)

if __name__ == '__main__':
   app.run(host="127.0.0.1", port=5000, debug=True)