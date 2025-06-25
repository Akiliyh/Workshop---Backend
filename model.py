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


def update(mycursor):
    mycursor.execute("SELECT * FROM Countries")
    countries = mycursor.fetchall()
    print(countries)

    print('-------')

    for country in mycursor:
        print(country)

    
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

def add(infos):   
    if infos == "c":
        mycursor.execute('''SELECT MAX(idCountry) FROM Countries''')
        id = mycursor.fetchone()[0] + 1
        mycursor.execute('''INSERT INTO Countries VALUES (''' + id +''',"''' + infos.name + '''","''' + infos.desc + '''",''' + infos.inhab + ''',''' + "'" + infos.date + "'" +'''"'''+ infos.gouv + '''"''' +''')''')
        for i in infos.lang :
            mycursor.execute('''INSERT INTO Countries_has_languages VALUES (''' + id +''',''' + infos.lang[i] + ''',"''' + infos.lang[i+1] +''')''') 
        mydb.commit()
    elif infos == "l":
        mycursor.execute('''SELECT MAX(idLanguage) FROM Languages''')
        id = mycursor.fetchone()[0] + 1
        mycursor.execute('''INSERT INTO Languages VALUES (''' + id +''',"''' + infos.name + '''","''' + infos.gender + '''",''' + infos.order + ''')''')
        mydb.commit()
    elif infos == "poi":
        mycursor.execute('''SELECT MAX(idInterestPoint) FROM InterestPoints''')
        id = mycursor.fetchone()[0] + 1
        mycursor.execute('''INSERT INTO Languages VALUES (''' + id +''',"''' + infos.name + '''",''' + "'"+ infos.date +"'"+ ''',"''' + infos.desc + '''",''' + infos.type + ''',''' + infos.coun +''')''')
        mydb.commit()

def delete(type, id, mycursor, mydb):
    if type == "c":
        mycursor.execute('''DELETE FROM Countries_has_languages WHERE idCountry= '''+ id)
        mycursor.execute('''DELETE FROM InterestPoints WHERE idCountry= '''+ id)
        mycursor.execute('''DELETE FROM Countries WHERE idCountry= '''+ id)
        mydb.commit()
    if type == "l":
        mycursor.execute('''DELETE FROM Countries_has_languages WHERE idLanguage= '''+ id)
        mycursor.execute('''DELETE FROM Languages WHERE idLanguage= '''+ id)
        mydb.commit()
    if type == "poi":
        mycursor.execute('''DELETE FROM InterestPoints WHERE idInterestPoint= '''+ id)
        mydb.commit()

