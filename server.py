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
    # model.update(mycursor)
    myCountries = model.get_countries(mycursor)
    myLanguages = model.get_languages(mycursor)
    myPointsOfInterest = model.get_points_of_interest(mycursor)
    model.disconnect_db(mydb, mycursor)
    return render_template('index.html', countries = myCountries, languages = myLanguages, points_of_interest = myPointsOfInterest)

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
    model.disconnect_db(mydb, mycursor)
    return render_template('form_point_of_interest.html', content=point_of_interest, countries=myCountries)

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
    return render_template('form_point_of_interest.html', content=id)

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