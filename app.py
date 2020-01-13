"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template
from forms import LoginFom
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

@app.route("/")
def homepage():
    """View function for Home Page."""
    # return render_template("home.html", pets=pets)
    return render_template("home.html", pets = pets)


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")

@app.route("/pet-details/<int:pet_id>")
def pet_details(pet_id):
    # for pet in pets:
    #     if pet['id'] == pet_id:
    #         return render_template("pet-details.html", pet = pet)
    #         url_for('pet_details', pet_id=pet['id'])
    #     abort(404, description="No Pet was Found with the given ID")   
    pet = next((pet for pet in pets if pet["id"] == pet_id), None) 
    if pet is None: 
        abort(404, description="No Pet was Found with the given ID")
    return render_template("pet-details.html", pet = pet)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
