from flask import Flask, render_template, request, redirect, url_for
import random
import mysql.connector
import model
import sqlite3

from flask_cors import CORS

myapp = Flask(__name__)
CORS(myapp)


mydb, mycursor = model.connect_db()
# Liste de Countries pour le form_point_of_interest
mycursor.execute("SELECT idCountry, nameCountry FROM Countries")
rows = mycursor.fetchall()
countries = [{'idCountry': row[0], 'nameCountry': row[1]} for row in rows]
model.disconnect_db(mydb, mycursor)


@myapp.route("/")
def home():
    mydb, mycursor = model.connect_db()
    model.update(mycursor)
    myCountries = model.get_countries(mycursor)
    myLanguages = model.get_languages(mycursor)
    myPointsOfInterest = model.get_points_of_interest(mycursor)
    model.disconnect_db(mydb, mycursor)
    return render_template('index.html', countries = myCountries, languages = myLanguages, points_of_interest = myPointsOfInterest)

@myapp.route("/country/<nameC>", methods=['GET', 'POST'])
def country(nameC):
    return render_template('country.html', content=nameC)

@myapp.route("/language/<nameL>", methods=['GET', 'POST'])
def language(nameL):
    return render_template('language.html', content=nameL)

@myapp.route("/point_of_interest/<namePOI>", methods=['GET', 'POST'])
def point_of_interest(namePOI):
    mydb, mycursor = model.connect_db()
    poi = model.get_point_of_interest_by_name(namePOI, mycursor)
    model.disconnect_db(mydb, mycursor)
    return render_template('point_of_interest.html', content=poi)

# Formulaires

@myapp.route("/point_of_interest/action", methods=['GET', 'POST'])
def form_poi():
    mydb, mycursor = model.connect_db()
    myCountries = model.get_countries(mycursor)
    model.disconnect_db(mydb, mycursor)
    return render_template('form_point_of_interest.html', content=point_of_interest, countries=myCountries)

@myapp.route("/country/action", methods=['GET', 'POST'])
def form_c():
    # Liste de Language pour le form_country
    mydb, mycursor = model.connect_db()
    mycursor.execute("SELECT idLanguage, nameLanguage FROM Languages")
    rows = mycursor.fetchall()
    languages = [{'id': row[0], 'name': row[1]} for row in rows]
    model.disconnect_db(mydb, mycursor)
    return render_template('form_country.html', content=country, languages=languages)

@myapp.route("/language/action", methods=['GET', 'POST'])
def form_l():
    return render_template('form_language.html', content=language)

# Modifications de propriétés

@myapp.route("/language/action/<nameL>", methods=['GET', 'POST'])
def form_l_update(nameL):
    return render_template('form_language.html', content=nameL)

@myapp.route("/country/action/<nameC>", methods=['GET', 'POST'])
def form_c_update(nameC):
    return render_template('form_country.html', content=nameC)

@myapp.route("/point_of_interest/action/<namePOI>", methods=['GET', 'POST'])
def form_poi_update(namePOI):
    return render_template('form_point_of_interest.html', content=namePOI)

# @myapp.route("/update", methods=['GET', 'POST'])
# def update():
#     placeholder_data = ["","",""]
#     if request.args.get('id'):
#         placeholder_data = (myList[int(request.args.get('id'))])
#     return render_template('form.html', content=placeholder_data)

# @myapp.route("/ajout", methods=['GET', 'POST'])
# def add():  
#     if request.method == "POST":
#         name = request.form.get('game_name')
#         price = request.form.get('price')
#         desc = request.form.get('desc')

#         myList.append({
#             'name': name,
#             'price': price,
#             'description': desc
#         })

#     if request.args.get('delete') == 'true':
#         print(request.args.get('delete'))
#         game_id = int(request.args.get('id'))
#         myList.pop(game_id)
#     # redirect because if we'd refresh on the cur page we'd create another game of the same value
#     return redirect(url_for('list')) 

# @myapp.route("/list", methods=['GET', 'POST'])
# def list():  
#     return render_template('list.html', content=myList)

# @myapp.route("/form2", methods=['GET', 'POST'])
# def form2():
#     return render_template('form2.html')

# @myapp.route("/traitement", methods=['GET', 'POST'])
# def traitement():
#     # return request.args
#     return render_template('traitement.html', content=request.args)
#     # return "Cher" +  request.args.get('firstname') + " " + request.args.get('firstname') + ", votre demande de " + request.args.get('seats') + " places pour " + request.args.get('brest') " destination est enregistrée" 

# @myapp.route("/appli")
# def appli():
#     return render_template('appli.html', content="Bienvenue dans l'application")

# @myapp.route("/game", methods=['GET', 'POST'])
# def game():
#     message = ""
#     if 'value' in request.args:
#         inputValue = request.args.get('value', type=int)
#         # if not inputValue.isdigit(): 
#         #     return render_template('game.html', content="Veuillez entrer un nombre valide.")
#         if inputValue < randValue:
#             message = "Plus grand !"
#         elif inputValue > randValue:
#             message = "Plus petit !"
#         elif inputValue == randValue:
#             message = "C'est bon ! la réponse était " + str(randValue)
#     return render_template('game.html', content=message)

# @myapp.route("/game_response", methods=['GET', 'POST'])
# def game_response():
#     randValue = random.randint(0, 100)
#     inputValue = int(request.args.get('value'))
#     return render_template('game.html', content=inputValue)


# DELETE INFORMATION

@myapp.route('/delete/<type>/<id>', methods=['GET', 'POST'])
def delete(type, id):
    mydb, mycursor = model.connect_db()
    model.delete(type, id, mycursor, mydb)
    model.disconnect_db(mydb, mycursor)
    return redirect(url_for('home'))
