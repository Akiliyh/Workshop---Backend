import mysql.connector

def connect_db():
    mydb = mysql.connector.connect(
    # host='163.172.165.87',
    # user='LinguiC',
    # password='ImAcGOAT',
    # database='LinguiC')
    
    host='localhost',
    user='root',
    password='root',
    database='linguic'
    )
    mycursor = mydb.cursor(dictionary=True)
    
    return mydb, mycursor

def disconnect_db(mydb, mycursor):
    mycursor.close()
    mydb.close()

def actionBDD(action, key="", infos = {}) :
    mydb, mycursor = connect_db()
    if not infos and not key == "" :
        data = action(mycursor, key)
        print("Doing action : ",action.__name__,". Using data = action(mycursor, key) with key = ", key)

    elif not infos and key=="":
        action(mydb, mycursor)
        print("Doing action : ",action.__name__,". Using action(mydb, mycursor) no returns")

    elif infos and not key == "" :
        data = action(mydb, mycursor, key, infos)
        print("Doing action : ",action.__name__,". Using data = action(mydb, mycursor, key, infos) with key = ", key, ", infos = ", infos)

    else :
        data = action(mydb, mycursor, infos)
        print("Doing action : ",action.__name__,". Using data = action(mydb, mycursor, infos) with infos = ", infos)

    disconnect_db(mydb, mycursor)
    return data

def get(mycursor, key):
    if key == "c" :
        get_countries(mycursor)
    elif key == "l" :
        get_languages(mycursor)
    elif key == "poi" :
        get_points_of_interest(mycursor)
    elif key == "tpoi" :
        get_types_of_points(mycursor)
    elif key == "wo" :
        get_word_orders(mycursor)
    
def get_countries(mycursor):
    mycursor.execute("SELECT * FROM Countries")
    countries = mycursor.fetchall()

    return countries

def get_country(mycursor, id):
    mycursor.execute("SELECT * FROM Countries WHERE Countries.idCountry =" + id + ";")
    countries = mycursor.fetchone()

    return countries

def get_languages(mycursor):
    mycursor.execute("SELECT l.*, SUM(chl.nbOfLocutorsInThisCountry) AS totalSpeakers FROM Countries_has_Languages AS chl RIGHT JOIN Languages AS l ON chl.idLanguage = l.idLanguage GROUP BY l.idLanguage;")
    languages = mycursor.fetchall()

    return languages

def get_language(mycursor, id):
    mycursor.execute("SELECT l.*, SUM(chl.nbOfLocutorsInThisCountry) AS totalSpeakers FROM Countries_has_Languages AS chl RIGHT JOIN Languages AS l ON chl.idLanguage = l.idLanguage WHERE l.idLanguage = " + id + ";")
    language = mycursor.fetchone()

    return language

def get_types_of_points(mycursor):
    mycursor.execute("SELECT * FROM TypePOI")
    type_of_points = mycursor.fetchall()

    return type_of_points

def get_type_of_points(mycursor, id):
    mycursor.execute("SELECT * FROM TypePOI WHERE TypePOI.idType =" + id + ";")
    type_of_points = mycursor.fetchone()

    return type_of_points

def get_points_of_interest(mycursor):
    mycursor.execute("SELECT * FROM InterestPoints")
    points_of_interest = mycursor.fetchall()

    return points_of_interest

def get_point_of_interest(mycursor, id):
    mycursor.execute("SELECT * FROM InterestPoints WHERE InterestPoints.idInterestPoint =" + str(id) + ";")
    point_of_interest = mycursor.fetchone()

    return point_of_interest

def get_word_orders(mycursor):
    mycursor.execute("SELECT * FROM WordOrder")
    word_orders = mycursor.fetchall()

    return word_orders

def get_word_order(mycursor, id):
    mycursor.execute("SELECT * FROM WordOrder WHERE WordOrder.idWordOrder =" + str(id) + ";")
    point_of_interest = mycursor.fetchone()

    return point_of_interest

# TO CHANGE WITH ID

def get_point_of_interest_by_name(name, mycursor):
    mycursor.execute("SELECT * FROM InterestPoints WHERE nameInterestPoint = '" + name + "'")
    result = mycursor.fetchone()
    return result

def get_points_of_interest_from_country(mycursor, id):
    mycursor.execute("SELECT InterestPoints.idInterestPoint, InterestPoints.nameInterestPoint, InterestPoints.idType FROM Countries JOIN InterestPoints ON Countries.idCountry = InterestPoints.idCountry WHERE Countries.idCountry =" + str(id) + ";")
    word_orders = mycursor.fetchall()

    return word_orders

def get_languages_from_country(mycursor, id):
    mycursor.execute("SELECT Languages.idLanguage, Languages.nameLanguage FROM Languages JOIN Countries_has_Languages ON Languages.idLanguage = Countries_has_Languages.idLanguage JOIN Countries ON Countries_has_Languages.idCountry = Countries.idCountry WHERE Countries.idCountry =" + str(id) + ";")
    languages = mycursor.fetchall()

    return languages

def get_countries_from_language(mycursor, id):
    mycursor.execute("SELECT Countries.idCountry, Countries.nameCountry FROM Languages JOIN Countries_has_Languages ON Languages.idLanguage = Countries_has_Languages.idLanguage JOIN Countries ON Countries_has_Languages.idCountry = Countries.idCountry WHERE Languages.idLanguage =" + str(id) + ";")
    countries = mycursor.fetchall()

    return countries

def add(mydb, mycursor, key, infos):
    if key == "c" :
        add_country(mydb, mycursor, infos)
    elif key == "l" :
        add_language(mydb, mycursor, infos)
    elif key == "poi" :
        add_point_of_interest(mydb, mycursor, infos)

def convertValue(value) :
    if value is None or value == "":
        return "NULL"
    elif value.isdigit() :
        return f"{value}"
    else :
        return f'''"{value}"'''

def valueDictToStr(dict, begin, end="") : #begin = first index included, end = last index included
    foundBeginning = False
    values = '''''' #formated values

    for i in dict :
        name, value = i, dict[i]
        # while we have not reached beginning
        if name != begin and not foundBeginning: continue
        # we reached beginning
        elif name == begin and not foundBeginning: foundBeginning = True
        elif name==end : 
            values += convertValue(value) + ","
            break #we reached end
        
        values += convertValue(value) + ","
    print(values)
    return values[:-1] #we don't want last ","

def add_country(mydb, mycursor, infos): 
    values = valueDictToStr(infos, "name", "gouv")
    query = f'''INSERT INTO Countries(nameCountry,descCountry,inhabitants,capital,date,governmentType)
               VALUES({values})'''
    # mycursor.execute('''INSERT INTO Countries(nameCountry,descCountry,inhabitants,capital,date,governmentType)
    #                     VALUES ("''' + str(infos['name']) + '''","''' + str(infos['desc']) + '''",''' + str(infos['nbHab']) + ''',"''' + str(infos['cap']) + '''","''' + str(infos['date']) + '''","''' + str(infos['gouv'])  +'''")''')
    mycursor.execute(query)
    country_id = mycursor.lastrowid
    for i in range(len(infos['lang_speakers'])):
        mycursor.execute('''
        INSERT INTO Countries_has_Languages(idCountry, idLanguage, nbOfLocutorsInThisCountry) 
        VALUES (''' + str(country_id) + ''',''' + str(infos['lang_speakers'][i]['language_id']) + ''',''' + str(infos['lang_speakers'][i]['speakers']) + ''')
        ''')

    mydb.commit()
    return country_id # only useful in the form redirect cause we have two queries here so it's not working very good


def add_language(mydb, mycursor, infos): 
    if 'gend' not in infos:
        infos['gend'] = '0'
    # Fix the order of infos if we create gend by hand
    ordered_infos = {
        "name": infos.get("name"),
        "gend": infos.get("gend"),
        "order": infos.get("order")
    }

    values = valueDictToStr(infos, "name", "order")
    values = valueDictToStr(ordered_infos, "name", "order")
    query = f'''INSERT INTO Languages(nameLanguage,gender,idWordOrder)
                VALUES({values});'''
    print(query)
    mycursor.execute(query)
    # mycursor.execute('''INSERT INTO Languages(nameLanguage,gender,idWordOrder)
    #                     VALUES ("''' + infos['name'] + '''",''' + str(infos['gend']) + ''',''' + infos['order'] + ''')''')
    mydb.commit()

def add_point_of_interest(mydb, mycursor, infos): 
    print("\tinfos add_poi : ", infos)
    # mycursor.execute('''INSERT INTO InterestPoints(nameInterestPoint,dateInterestPoint,descInterestPoint,idType,idCountry)
    #                     VALUES ("''' + infos['name'] + '''",''' + infos['date'] + ''',"''' + infos['desc'] + '''",''' + infos['type'] + ''',''' + infos['coun'] +''')''')

    values = valueDictToStr(infos, "name", "coun")
    query = f'''INSERT INTO  InterestPoints(nameInterestPoint,dateInterestPoint,descInterestPoint,idType,idCountry)
               VALUES({values});'''
    print(query)
    mycursor.execute(query)
    mydb.commit()

def update(mydb, mycursor, key, infos):
    if key == "c" :
        update_country(mydb, mycursor, infos)
    elif key == "l" :
        update_language(mydb, mycursor, infos)
    elif key == "poi" :
        update_point_of_interest(mydb, mycursor, infos)

original = {'idLanguage': 3, 'nameLanguage': 'Gnegnegnah', 'gender': 0, 'idWordOrder': 5, 'totalSpeakers': '0.1'}
new = {'id': 3, 'name': 'Gnegnegnahkkkkk', 'gend': '1', 'order': '1'}
def find_differences(original, new):
    differences = {}
    keys_original = list(original.keys())
    keys_new = list(new.keys())
    for i in range(len(original)) :
        field_original = keys_original[i]
        field_new = keys_new[i]
        
        field = field_original
        value = new[field_new]

        if original[field] != value :
            print("original : ", original)
            print("new : ", new)
            print(field_original, new[field_new])

            # rubbish fix code
            # the issue here is that in convertValue we add double quotes to non string however we already have double quotes and it fucks the sql up
            cleaned = convertValue(value)
            if isinstance(value,str) and cleaned.startswith('"') and cleaned.endswith('"'):
                cleaned = cleaned[1:-1]  # removes one from each side
                differences.update({field: cleaned})
            else:
                 differences.update({field:convertValue(value)})
            
    print("\tprinting differences : ", differences)
    return differences

#update countries set name = 'truc', cap = 'truc', lang = 2* where id = 1
def setDifferencesQuery(original, new) :
    differences = find_differences(original, new)
    query = ""
    for i in differences :
        name, value = i, differences[i]
        query += f"{name} = {convertValue(value)},"
    return query[:-1]

def update_country(mydb, mycursor, infos):
    # infos = {name, desc, nbHab, cap, date, gouv, lang, nb_speaker1}
    if "id" not in infos:
        raise ValueError("Missing ID for update operation")
    
    original = get_country(mycursor, str(infos['id']))
    values = setDifferencesQuery(original, infos)
    print("values country : ", values)
    if values !="" :
        query = f'''UPDATE Countries SET {values} WHERE Countries.idCountry ={infos["id"]};'''
        mycursor.execute(query)
        mydb.commit()

def reorder_language_dict (infos, dict_key_to_check_value, list_of_to_delete_keys) :
    key_to_check = list(dict_key_to_check_value.keys())[0]
    if key_to_check not in infos.keys() :
        inserted = False
        for key_to_delete in list_of_to_delete_keys :
            value = infos[key_to_delete]
            del infos[key_to_delete]

            if not inserted :
                infos.update(dict_key_to_check_value)

            infos.update({key_to_delete : value})
        
def update_language(mydb, mycursor, infos):
    # infos = {name, gend, order}
    if "id" not in infos:
        raise ValueError("Missing ID for update operation")
    
    original = get_language(mycursor, str(infos['id']))
    del original['totalSpeakers']
    reorder_language_dict(infos, {'gend':'0'}, ['order'])

    values = setDifferencesQuery(original, infos)
    print("values language : ", values)
    if values !="" :
        query = f'''UPDATE Languages SET {values} WHERE Languages.idLanguage ={infos["id"]};'''
        print("\tprinting query update languages :", query)
        mycursor.execute(query)
        mydb.commit()

def update_point_of_interest(mydb, mycursor, infos):
    # infos = {name, desc, date, type, coun}
    if "id" not in infos:
        raise ValueError("Missing ID for update operation")
    
    original = get_point_of_interest(mycursor, infos['id'])
    values = setDifferencesQuery(original, infos)
    print("values poi : ", values)
    if values != "" :
        query = f'''UPDATE InterestPoints SET {values} WHERE InterestPoints.idInterestPoint ={infos["id"]};'''
        mycursor.execute(query)
        mydb.commit()

def delete(mydb, mycursor, key, infos):
    if key == "c" :
        delete_country(mydb, mycursor, infos)
    elif key == "l" :
        delete_language(mydb, mycursor, infos)
    elif key == "poi" :
        delete_point_of_interest(mydb, mycursor, infos)

def delete_country(mydb, mycursor, id):
    mycursor.execute('''DELETE FROM Countries_has_Languages WHERE idCountry= '''+ str(id))
    mycursor.execute('''DELETE FROM InterestPoints WHERE idCountry= '''+ str(id))
    mycursor.execute('''DELETE FROM Countries WHERE idCountry= '''+ str(id))
    mydb.commit()
def delete_language(mydb, mycursor, id):
    mycursor.execute('''DELETE FROM Countries_has_Languages WHERE idLanguage= '''+ str(id))
    mycursor.execute('''DELETE FROM Languages WHERE idLanguage= '''+ str(id))
    mydb.commit()
def delete_point_of_interest(mydb, mycursor, id):
    mycursor.execute('''DELETE FROM InterestPoints WHERE idInterestPoint= '''+ str(id))
    mydb.commit()

def reinit(mydb, mycursor):

    mycursor.execute("""TRUNCATE TABLE InterestPoints;""") 
    mycursor.execute("""TRUNCATE TABLE Countries_has_Languages;""") 
    mycursor.execute("""SET FOREIGN_KEY_CHECKS = 0;""") 
    mycursor.execute("""TRUNCATE TABLE Languages;""") 
    mycursor.execute("""TRUNCATE TABLE Countries;""") 
    mycursor.execute("""SET FOREIGN_KEY_CHECKS = 1;""")

    mydb.commit()

    mycursor.execute("""INSERT INTO Countries VALUES
        (1, 'Ioctotere', 'Le Ioctotere est la terre du Iocto', 167, 'Estes', '2020-01-01', 'Dictature'),
        (2, 'mapona', 'mapona est la royauté du bien', 131, 'ma', '2025-03-07', 'Monarchie'),
        (3, 'Survivortopia', 'Y a que les vrais survivors qui peuvent y vivre ! Les autres ils vont survivre ailleurs !', 1, 'Survivor-City', '2025-05-27', 'Mononarchie');""")

    mycursor.execute("""INSERT INTO Languages VALUES 
        (1, 'Iocto', false, 1),
        (2, 'toki pona', false, 1),
        (3, 'Gnegnegnah', true, 5);""")

    mycursor.execute("""INSERT INTO InterestPoints VALUES
        (1, 'Iocto Stalin Statue', 2021, 'Une belle statue pas vrai', 1, 1),
        (2, 'kasi soweli', 2026, 'Attention y a un ours !', 3, 2);""")

    mycursor.execute("""INSERT INTO Countries_has_Languages VALUES (1, 1, 150), 
        (2, 2, 131), (1, 2, 17), (3, 2, 20), (3, 1, 18), (3, 3, 1);""")

    mydb.commit()


#fonctions qu'on aura surement pas le temps d'utiliser :

def nb_sp_tot (mycursor,idL):
    mycursor.execute("SELECT sum(nbOfLocutorsInThisCountry) FROM Countries_has_languages WHERE idLanguage='"+idL+"' GROUP BY idLanguage ;")
    nb_speaker_in_word = mycursor.fetchall()

    return nb_speaker_in_word #retourne le nombre total de personne parlant une langue L

def nb_hab_tot (mycursor):
    mycursor.execute("SELECT sum(inhabitants) FROM Countries;")
    nb_inhabitant_in_word = mycursor.fetchall()

    return nb_inhabitant_in_word #retourne le nombre total d'habitant du monde

def prct_sp_tot (mycursor,idL):
    nb_h = nb_hab_tot(mycursor)
    nb_s = nb_sp_tot(mycursor, idL)
    nb_s_outof_h = nb_s * 100 /nb_h

    return nb_s_outof_h #retourne le pourcentage de personne parlant une langue L dans le monde

def prct_sp_in_c (mycursor, idC, idL):
    mycursor.execute("SELECT nbOfLocutorsInThisCountry FROM countries_has_languages WHERE idCountry='"+idC+"' AND idLanguage='"+idL+"';")
    nb_s = mycursor.fetchall()
    mycursor.execute("SELECT inhabitants FROM Countries WHERE idCountry='"+idC+"';")
    nb_h = mycursor.fetchall()
    nb_sp_in_country = nb_s * 100 / nb_h

    return nb_sp_in_country #retourne le pourcentage de gens parlant une langue L dans un pays C

def nb_sps_in_c (mycursor, idC):
    mycursor.execute("SELECT sum(nbOfLocutorsInThisCountry) FROM Countries_has_languages WHERE idCountry='"+idC+"' GROUP BY idCountry ;")
    nb_sps_in_country = mycursor.fetchall()

    return nb_sps_in_country
    #retourne le nombre de personne parlant une langue quelconque dans un pays C (la légende raconte que c'est censé être le même nombre que d'habitant du pays)

def verif_sp_h (mycursor, idC):
    mycursor.execute("SELECT inhabitants FROM Countries WHERE idCountry='"+idC+"';")
    nb_h = mycursor.fetchall()
    nb_sps = nb_sps_in_c(mycursor, idC)
    if nb_h == nb_sps :
        return True
    return False #verifie si le nombre de personne parlant une langue quelconque dans un pays C et le même nombre que celui de la population

def nb_hab_restant (mycursor, pop_max): #pop_max = 10000 aux dernières nouvelles
    nb_pop_world = nb_hab_tot (mycursor)
    nb_restant = pop_max - nb_pop_world

    return nb_restant #retourne le nombre d'habitants par encore placé dans un pays quelconque 

def verif_rest_hab (mycursor, pop_max):
    if nb_hab_restant (mycursor, pop_max)>0:
        return True
    return False #verifie s'il y a encore des habitants à mettre

