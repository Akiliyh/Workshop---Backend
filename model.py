import mysql.connector

def connect_db():
    mydb = mysql.connector.connect(
    host='163.172.165.87',
    user='LinguiC',
    password='ImAcGOAT',
    database='LinguiC'
    )

    mycursor = mydb.cursor()
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

def get_languages(mycursor):
    mycursor.execute("SELECT l.*, SUM(chl.nbOfLocutorsInThisCountry) AS totalSpeakers FROM Countries_has_Languages AS chl JOIN Languages AS l ON chl.idLanguage = l.idLanguage GROUP BY l.idLanguage;")
    languages = mycursor.fetchall()

    return languages

def get_points_of_interest(mycursor):
    mycursor.execute("SELECT * FROM InterestPoints")
    points_of_interest = mycursor.fetchall()

    return points_of_interest

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
        delete_country(mydb, mycursor, infos.id)
    elif key == "l" :
        delete_language(mydb, mycursor, infos.id)
    elif key == "poi" :
        delete_point_of_interest(mydb, mycursor, infos.id)

def delete_country(mydb, mycursor, id):
    mycursor.execute('''DELETE FROM Countries_has_languages WHERE idCountry= '''+ id)
    mycursor.execute('''DELETE FROM InterestPoints WHERE idCountry= '''+ id)
    mycursor.execute('''DELETE FROM Countries WHERE idCountry= '''+ id)
    mydb.commit()
def delete_language(mydb, mycursor, id):
    mycursor.execute('''DELETE FROM Countries_has_languages WHERE idLanguage= '''+ id)
    mycursor.execute('''DELETE FROM Languages WHERE idLanguage= '''+ id)
    mydb.commit()
def delete_point_of_interest(mydb, mycursor, id):
    mycursor.execute('''DELETE FROM InterestPoints WHERE idInterestPoint= '''+ id)
    mydb.commit()

