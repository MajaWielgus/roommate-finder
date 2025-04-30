from flask import Blueprint, render_template, request
from .models import Offer
from . import db

main = Blueprint('main', __name__)

city_coordinates = {
    'Gdańsk': {'lat': 54.3520, 'lng': 18.6466, 'radius': 5000},
    'Sopot': {'lat': 54.4400, 'lng': 18.5600, 'radius': 3000},
    'Gdynia': {'lat': 54.5186, 'lng': 18.5300, 'radius': 5000}
}

@main.route("/", methods=["GET", "POST"])
def home():
    selected_city = None
    offers = []

    if request.method == "POST":
        selected_city = request.form.get("location")
        balcony = "balcony" in request.form
        smoking = "smoking" in request.form
        pets = "pets" in request.form

        query = Offer.query

        if selected_city:
            query = query.filter_by(location=selected_city)
        if balcony:
            query = query.filter_by(balcony=True)
        if smoking:
            query = query.filter_by(smoking=True)
        if pets:
            query = query.filter_by(pets=True)

        offers = query.all()

    return render_template("index.html", 
                           city_coordinates=city_coordinates, 
                           selected_city=selected_city, 
                           offers=offers)
