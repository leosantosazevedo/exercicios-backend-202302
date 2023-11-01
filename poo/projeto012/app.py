import flask
import requests
import json2table

app = flask.Flask(__name__)
@app.route("/")

def OlaMundo():
        return "<p>Ola Mundo</p>"

@app.route("/consultaContinentes")
def consultaContinentes():
        response2 = requests.get("http://127.0.0.1:8000/getContinents")
        json_object = response2.json()
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style" : "width:100%", "border": "1px solid black"}
        html = json2table.convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
        #print(html)
        #return response2.json()
        return html

@app.route("/consultaRegioes")
def consultaRegioes():
        response2 = requests.get("http://127.0.0.1:8000/getRegions")
        json_object = response2.json()
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style" : "width:100%", "border": "1px solid black"}
        html = json2table.convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
        #print(html)
        #return response2.json()
        return html

@app.route("/consultaCountries")
def consultaCountries():
        response2 = requests.get("http://127.0.0.1:8000/getCountries")
        json_object = response2.json()
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style" : "width:100%", "border": "1px solid black"}
        html = json2table.convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
        #print(html)
        #return response2.json()
        return html
        
@app.route("/consultaCountriesLanguage")
def consultaCountriesLanguage():
        response2 = requests.get("http://127.0.0.1:8000/getCountryLanguage")
        json_object = response2.json()
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style" : "width:100%", "border": "1px solid black"}
        html = json2table.convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
        #print(html)
        #return response2.json()
        return html

if __name__ == '__main__':
    app.run(debug=True)