import mysql.connector

def connect_db():
    mydb = mysql.connector.connect(
    host='163.172.165.87',
    user='LinguiC',
    password='ImAcGOAT',
    database='LinguiC'
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM Countries")
    countries = mycursor.fetchall()
    print(countries)

    print('-------')

    for country in mycursor:
        print(country)

    mycursor.close()
    mydb.close()




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

def delete(type, id):
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
        mycursor.execute('''DELETE FROM InterstPoints WHERE idPointInterst= '''+ id)
        mydb.commit()