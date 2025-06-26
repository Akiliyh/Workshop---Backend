original = {'idLanguage': 3, 'nameLanguage': 'Gnegnegnah', 'gender': 0, 'idWordOrder': 5}
new = {'id': 3, 'name': 'Gnegnegnahkkkkk', 'gend': '1', 'order': '1'}

def convertValue(value) :
    # if value is None:
    #     return "NULL"
    if value.isdigit() :
        return f"{value}"
    elif value == "" :
        return "NULL"
    else :
        return f'''"{value}"'''

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
            differences.update({field:value})
            
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

setDifferencesQuery(original, new)