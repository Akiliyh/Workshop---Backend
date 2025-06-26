from flask import Flask, render_template, request, redirect, url_for
import model
import api

from flask_cors import CORS

myapp = Flask(__name__)
CORS(myapp)


mydb, mycursor = model.connect_db()
# Liste de Countries pour le form_point_of_interest
mycursor.execute("SELECT idCountry, nameCountry FROM Countries")
rows = mycursor.fetchall()
countries = [{'idCountry': row['idCountry'], 'nameCountry': row['nameCountry']} for row in rows]
model.disconnect_db(mydb, mycursor)


api.register_api_routes(myapp)

@myapp.route("/")
def home():
    mydb, mycursor = model.connect_db()
    myCountries = model.get_countries(mycursor)
    myLanguages = model.get_languages(mycursor)
    myPointsOfInterest = model.get_points_of_interest(mycursor)
    myTypeOfPoints = model.get_types_of_points(mycursor)
    model.disconnect_db(mydb, mycursor)
    return render_template('index.html', countries = myCountries, languages = myLanguages, points_of_interest = myPointsOfInterest, type_of_points = myTypeOfPoints)

@myapp.route("/country/<int:id>", methods=['GET', 'POST'])
def country(id):
    return render_template('country.html', content=id)

@myapp.route("/language/<int:id>", methods=['GET', 'POST'])
def language(id):
    return render_template('language.html', content=id)

@myapp.route("/point_of_interest/<int:id>", methods=['GET', 'POST'])
def point_of_interest(id):
    return render_template('point_of_interest.html', content=id)

# Formulaires

@myapp.route("/point_of_interest/action", methods=['GET', 'POST'])
def form_poi():
    mydb, mycursor = model.connect_db()
    myCountries = model.get_countries(mycursor)
    typePOI = model.get_types_of_points(mycursor)
    model.disconnect_db(mydb, mycursor)
    return render_template('form_point_of_interest.html', content = {}, countries=myCountries, tpoi = typePOI, id = "")

@myapp.route("/country/action", methods=['GET', 'POST'])
def form_c():
    # Liste de Language pour le form_country
    mydb, mycursor = model.connect_db()
    mycursor.execute("SELECT idLanguage, nameLanguage FROM Languages")
    rows = mycursor.fetchall()
    languages = [{'id': row['idLanguage'], 'name': row['nameLanguage']} for row in rows]
    model.disconnect_db(mydb, mycursor)
    return render_template('form_country.html', content=country, languages=languages)

@myapp.route("/language/action", methods=['GET', 'POST'])
def form_l():
    return render_template('form_language.html', content=language)

# Modifications de propriétés

@myapp.route("/language/action/<int:id>", methods=['GET', 'POST'])
def form_l_update(id):
    return render_template('form_language.html', content=id)

@myapp.route("/country/action/<int:id>", methods=['GET', 'POST'])
def form_c_update(id):
    return render_template('form_country.html', content=id)

@myapp.route("/point_of_interest/action/<int:id>", methods=['GET', 'POST'])
def form_poi_update(id):
    print("\tprinting id of poi update : ", id)

    mydb, mycursor = model.connect_db()
    content = model.get_point_of_interest(mycursor, id)
    myCountries = model.get_countries(mycursor)
    myTypeOfPoints = model.get_types_of_points(mycursor)
    print("AHHH")
    print(myTypeOfPoints)
    model.disconnect_db(mydb, mycursor)

    print("\tprinting content : ", content)
    return render_template('form_point_of_interest.html', id = id, content=content, countries = myCountries, tpoi = myTypeOfPoints)