"""Flask app for paw rescue center"""
from flask import Flask, render_template
app = Flask(__name__)

Users = {
        "Archie":"Amsterdam", 
        "Veronica":"London", 
        "Betty":"San Francisco", 
        "Jughead":"Los Angeles"
    }
@app.route("/")
def home():
    return render_template('home.html', users=Users)
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port =3000)