import mysql.connector

def connect_db():
    # mydb = mysql.connector.connect(
    # host='163.172.165.87',
    # user='LinguiC',
    # password='ImAcGOAT',
    # database='LinguiC'
    # )
    mydb = mysql.connector.connect(
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
        print("Doing action : " + str(action) , ". Using data = action(mycursor, key) with key = ", key)

    elif not infos and key=="":
        action(mydb, mycursor)
        print("Doing action : " + str(action) + ". Using action(mydb, mycursor) no returns")

    elif infos and key != "" :
        data = action(mydb, mycursor, key, infos)
        print("Doing action : " + str(action) + ". Using data = action(mydb, mycursor, key, infos) with key = ", key, ", infos = ", infos)

    disconnect_db(mydb, mycursor)
    return data

def update(mycursor):
    mycursor.execute("SELECT * FROM Countries")
    countries = mycursor.fetchall()
    print(countries)

    print('-------')

    for country in mycursor:
        print(country)
def get(mycursor, key):
    if key == "c" :
        get_countries(mycursor)
    elif key == "l" :
        get_languages(mycursor)
    elif key == "poi" :
        get_points_of_interest(mycursor)
    
def get_countries(mycursor):
    mycursor.execute("SELECT * FROM Countries")
    countries = mycursor.fetchall()

    return countries

def get_country(mycursor, id):
    mycursor.execute("SELECT * FROM Countries WHERE Countries.idCountry =" + id + ";")
    countries = mycursor.fetchone()

    return countries

def get_languages(mycursor):
    mycursor.execute("SELECT l.*, SUM(chl.nbOfLocutorsInThisCountry) AS totalSpeakers FROM Countries_has_Languages AS chl JOIN Languages AS l ON chl.idLanguage = l.idLanguage GROUP BY l.idLanguage;")
    languages = mycursor.fetchall()

    return languages

def get_language(mycursor, id):
    mycursor.execute("SELECT l.*, SUM(chl.nbOfLocutorsInThisCountry) AS totalSpeakers FROM Countries_has_Languages AS chl JOIN Languages AS l ON chl.idLanguage = l.idLanguage WHERE l.idLanguage = " + id + ";")
    language = mycursor.fetchone()

    return language

def get_points_of_interest(mycursor):
    mycursor.execute("SELECT * FROM InterestPoints")
    points_of_interest = mycursor.fetchall()

    return points_of_interest

def get_point_of_interest(mycursor, id):
    mycursor.execute("SELECT * FROM InterestPoints WHERE InterestPoints.idInterestPoint =" + id + ";")
    point_of_interest = mycursor.fetchone()

    return point_of_interest

# TO CHANGE WITH ID

def get_point_of_interest_by_name(name, mycursor):
    mycursor.execute("SELECT * FROM InterestPoints WHERE nameInterestPoint = '" + name + "'")
    result = mycursor.fetchone()
    return result

def add(mydb, mycursor, key, infos):
    if key == "c" :
        add_country(mydb, mycursor, infos)
    elif key == "l" :
        add_language(mydb, mycursor, infos)
    elif key == "poi" :
        add_point_of_interest(mydb, mycursor, infos)

def add_country(mydb, mycursor, infos): 
    mycursor.execute('''SELECT MAX(idCountry) FROM Countries''')
    infos.id = mycursor.fetchone()[0] + 1
    mycursor.execute('''INSERT INTO Countries VALUES (''' + infos.id +''',"''' + infos.name + '''","''' + infos.desc + '''",''' + infos.inhab + ''',''' + "'" + infos.date + "'" +'''"'''+ infos.gouv + '''"''' +''')''')
    for i in infos.lang :
        mycursor.execute('''INSERT INTO Countries_has_languages VALUES (''' + infos.id +''',''' + infos.lang[i] + ''',"''' + infos.lang[i+1] +''')''') 
    mydb.commit()
def add_language(mydb, mycursor, infos): 
    mycursor.execute('''SELECT MAX(idLanguage) FROM Languages''')
    infos.id = mycursor.fetchone()[0] + 1
    mycursor.execute('''INSERT INTO Languages VALUES (''' + infos.id +''',"''' + infos.name + '''","''' + infos.gender + '''",''' + infos.order + ''')''')
    mydb.commit()
def add_point_of_interest(mydb, mycursor, infos): 
    mycursor.execute('''SELECT MAX(idInterestPoint) FROM InterestPoints''')
    infos.id = mycursor.fetchone()[0] + 1
    mycursor.execute('''INSERT INTO Languages VALUES (''' + infos.id +''',"''' + infos.name + '''",''' + "'"+ infos.date +"'"+ ''',"''' + infos.desc + '''",''' + infos.type + ''',''' + infos.coun +''')''')
    mydb.commit()

def delete(mydb, mycursor, key, infos):
    if key == "c" :
        delete_country(mydb, mycursor, infos)
    elif key == "l" :
        delete_language(mydb, mycursor, infos)
    elif key == "poi" :
        delete_point_of_interest(mydb, mycursor, infos)

def delete_country(mydb, mycursor, id):
    mycursor.execute('''DELETE FROM Countries_has_languages WHERE idCountry= '''+ str(id))
    mycursor.execute('''DELETE FROM InterestPoints WHERE idCountry= '''+ str(id))
    mycursor.execute('''DELETE FROM Countries WHERE idCountry= '''+ str(id))
    mydb.commit()
def delete_language(mydb, mycursor, id):
    mycursor.execute('''DELETE FROM Countries_has_languages WHERE idLanguage= '''+ str(id))
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

def reinsert(mydb, mycursor):
    print('test')

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
