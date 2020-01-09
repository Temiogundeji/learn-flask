from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"
@app.route("/about")
def about():
    return "<h2>About Page</h2><p>We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology hop!</p>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port =3000)