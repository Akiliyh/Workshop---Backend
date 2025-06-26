from flask import request, jsonify
import model

def register_api_routes(myapp):
    @myapp.route("/api/init", methods=["PUT"])
    def api_init():
        mydb, mycursor = model.connect_db()
        model.reinit(mydb, mycursor)
        model.disconnect_db(mydb, mycursor)
        return jsonify({"message": "Database reinitialised"}), 201
    
    @myapp.route("/api/country", methods=["GET"])
    def api_get_countries():
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_countries(mycursor))
        model.disconnect_db(mydb, mycursor)
        return result
    
    @myapp.route("/api/country/<int:id>", methods=["GET"])
    def api_get_country(id):
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_country(mycursor, str(id)))
        model.disconnect_db(mydb, mycursor)
        return result if result else ("Not found", 404)
    
    @myapp.route("/api/country", methods=["POST"])
    def api_add_country():
        mydb, mycursor = model.connect_db()
        data = request.form.to_dict()
        print(data)
        # data = request.json
        # print(data)
        lang_count = sum( # here what we want to do is to store the amount of languages people speak inside this country
            1 for key, value in data.items()
            if key.startswith('nbspeaker_') and value.strip()
        )

        data['lang'] = str(lang_count)

        lang_speakers = []
        for key, value in data.items():
            if key.startswith('nbspeaker_') and value.strip():
                lang_id = key.replace('nbspeaker_', '')
                speakers = int(value)
                lang_speakers.append({'language_id': lang_id, 'speakers': speakers})

        data['lang_speakers'] = lang_speakers

        new_id = model.add_country(mydb, mycursor, data)
        model.disconnect_db(mydb, mycursor)
        print(data)
        print(new_id)
        return jsonify({"message": "Added country", "id": new_id}), 201
    
    @myapp.route('/api/country/<int:id>', methods=['DELETE'])
    def api_delete_country(id):
        mydb, mycursor = model.connect_db()
        model.delete(mydb, mycursor, 'c', id)
        model.disconnect_db(mydb, mycursor)
        return jsonify({"message": "Country deleted"})
    
    @myapp.route("/api/language", methods=["GET"])
    def api_get_languages():
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_languages(mycursor))
        model.disconnect_db(mydb, mycursor)
        return result
    
    @myapp.route("/api/language/<int:id>", methods=["GET"])
    def api_get_language(id):
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_language(mycursor, str(id)))
        model.disconnect_db(mydb, mycursor)
        return result if result else ("Not found", 404)

    @myapp.route("/api/language", methods=["POST"])
    def api_add_language():
        mydb, mycursor = model.connect_db()
        data = request.form.to_dict()
        print(data)
        # data = request.json
        # print(data)
        model.add_language(mydb, mycursor, data)
        new_id = mycursor.lastrowid
        model.disconnect_db(mydb, mycursor)
        return jsonify({"message": "Added language", "id": new_id}), 201

    @myapp.route("/api/language/<int:id>", methods=["PUT"])
    def api_update_language(id):
        data = request.json
        model.update_language(id, data["nameLanguage"])
        return jsonify({"message": "Language updated"})

    @myapp.route('/api/language/<int:id>', methods=['DELETE'])
    def api_delete_language(id):
        mydb, mycursor = model.connect_db()
        model.delete(mydb, mycursor, 'l', id)
        model.disconnect_db(mydb, mycursor)
        return jsonify({"message": "Language deleted"})

    @myapp.route("/api/point_of_interest", methods=["GET"])
    def api_get_points_of_interest():
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_points_of_interest(mycursor))
        model.disconnect_db(mydb, mycursor)
        return result
    
    @myapp.route("/api/point_of_interest/<int:id>", methods=["GET"])
    def api_get_point_of_interest(id):
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_point_of_interest(mycursor, str(id)))
        model.disconnect_db(mydb, mycursor)
        return result
    
    @myapp.route("/api/point_of_interest", methods=["POST"])
    def api_add_point_of_interest():
        mydb, mycursor = model.connect_db()
        data = request.form.to_dict()
        print(data)
        # data = request.json
        # print(data)
        model.add_point_of_interest(mydb, mycursor, data)
        new_id = mycursor.lastrowid
        model.disconnect_db(mydb, mycursor)
        return jsonify({"message": "Added point of interest", "id": new_id}), 201
    
    @myapp.route("/api/point_of_interest/<int:id>", methods=["POST"])
    def api_update_poi(id):
        mydb, mycursor = model.connect_db()
        data = {'id':id}
        data.update(request.form.to_dict())
        print("data : ", data)
        model.update_point_of_interest(mydb, mycursor, data)
        model.disconnect_db(mydb, mycursor)
        return jsonify({"message": "Point of interest updated"})

    @myapp.route('/api/point_of_interest/<int:id>', methods=['DELETE'])
    def api_delete_poi(id):
        mydb, mycursor = model.connect_db()
        model.delete(mydb, mycursor, 'poi', id)
        model.disconnect_db(mydb, mycursor)
        return jsonify({"message": "Point of Interest deleted"})

    @myapp.route("/api/country/language/<int:id>", methods=["GET"])
    def api_get_countries_from_language(id):
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_countries_from_language(mycursor, str(id)))
        model.disconnect_db(mydb, mycursor)
        return result if result else ("Not found", 404)

    @myapp.route("/api/language/country/<int:id>", methods=["GET"])
    def api_get_languages_from_country(id):
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_languages_from_country(mycursor, str(id)))
        model.disconnect_db(mydb, mycursor)
        return result if result else ("Not found", 404)

    @myapp.route("/api/point_of_interest/country/<int:id>", methods=["GET"])
    def api_get_poi_from_country(id):
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_points_of_interest_from_country(mycursor, str(id)))
        model.disconnect_db(mydb, mycursor)
        return result if result else ("Not found", 404)
    
    @myapp.route('/api/type_of_point', methods=['GET'])
    def api_get_types():
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_types_of_points(mycursor))
        model.disconnect_db(mydb, mycursor)
        return result
    
    @myapp.route('/api/type_of_point/<int:id>', methods=['GET'])
    def api_get_type(id):
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_type_of_points(mycursor, str(id)))
        model.disconnect_db(mydb, mycursor)
        return result
    
    @myapp.route('/api/word_order', methods=['GET'])
    def api_get_word_orders():
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_word_orders(mycursor))
        model.disconnect_db(mydb, mycursor)
        return result
    
    @myapp.route('/api/word_order/<int:id>', methods=['GET'])
    def api_get_word_order(id):
        mydb, mycursor = model.connect_db()
        result = jsonify(model.get_word_order(mycursor, str(id)))
        model.disconnect_db(mydb, mycursor)
        return result