from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "DEV"

# The top melons at Ubermleon
MOST_LOVED_MELONS = {
    "cren": {
        "img": "http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg",
        "name": "Crenshaw",
        "num_loves": 584,
    },
    "jubi": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg",
        "name": "Jubilee Watermelon",
        "num_loves": 601,
    },
    "sugb": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg",
        "name": "Sugar Baby Watermelon",
        "num_loves": 587,
    },
    "texb": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg",
        "name": "Texas Golden Watermelon",
        "num_loves": 598,
    },
}


@app.route("/top-melons")
def show_top_melons():
    """Display info of melons in MOST_LOVED_MELONS."""

    if "name" not in session:
        return redirect("/")

    return render_template("top-melons.html", melons=MOST_LOVED_MELONS)


@app.route("/")
def show_homepage():
    """Show homepage."""

    if "name" in session:
        return redirect("/top-melons")

    return render_template("homepage.html")


@app.route("/get-name")
def get_name():
    """Get name and store in session."""

    name = request.args.get("name")

    if name:
        session["name"] = name

    return redirect("/top-melons")


# Extra credit


@app.route("/love-melon", methods=["POST"])
def process_love_melon():
    """Process form submission to love a melon."""

    melon_id = request.form.get("melon")
    if melon_id in MOST_LOVED_MELONS:
        MOST_LOVED_MELONS[melon_id]["num_loves"] += 1

    return render_template("thank-you.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
