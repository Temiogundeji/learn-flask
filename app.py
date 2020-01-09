from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/<my_name>")
def greetings(my_name):
    return "Welcome" + my_name + "!"

@app.route('/square/<int:number>')
def show_square(number):
    return "Square of" + str(number * number) + " is:"
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port =3000)