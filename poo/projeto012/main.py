import fastapi
import connection
app = fastapi.FastAPI()
@app.get("/")
def hello_world_root():
    return {"Olá": "Funciona"}

@app.get("/getContinents")
def getContinents():
    Continents_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from continents"
    mycursor.execute(sql)
    for data_continents in mycursor:
        Continents_list.append( data_continents )
    mycursor.close()
    return {"Continents": Continents_list}

@app.get("/getContinent/{continent_id}")
def getContinent(continent_id : int):
    Continents_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql="select * from continents where continent_id = {0}".format(continent_id)
    mycursor.execute(sql)
    for data_continents in mycursor:
        Continents_list.append( data_continents )
    mycursor.close()
    return {"Continent": Continents_list}

@app.get("/getCountries")
def getCountries():
    Countries_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from countries"
    mycursor.execute(sql)
    for data_countries in mycursor:
        Countries_list.append( data_countries )
    mycursor.close()
    return {"countries": Countries_list}

@app.get("/getCountries/{country_id}")
def getCountries(country_id : int):
    Countries_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql="select * from countries where country_id = {0}".format(country_id)
    mycursor.execute(sql)
    for data_countries in mycursor:
        Countries_list.append( data_countries )
    mycursor.close()
    return {"Countries": Countries_list}

@app.get("/getCountryLanguage")
def getCountryLanguage():
    CountryLanguage_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from country_languages"
    mycursor.execute(sql)
    for data_countrylanguage in mycursor:
        CountryLanguage_list.append( data_countrylanguage )
    mycursor.close()
    return {"countrylanguage": CountryLanguage_list}

@app.get("/getCountryLanguage/{language_id}")
def getCountryLanguage(language_id : int):
    CountryLanguage_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql="select * from country_languages where language_id = {0}".format(language_id)
    mycursor.execute(sql)
    for data_countrylanguage in mycursor:
        CountryLanguage_list.append( data_countrylanguage )
    mycursor.close()
    return {"Continent": CountryLanguage_list}





































@app.get("/getRegions")
def getRegions():
    Regions_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from regions"
    mycursor.execute(sql)
    for data_regions in mycursor:
        Regions_list.append( data_regions )
    mycursor.close()
    return {"Regions": Regions_list}

@app.get("/getRegion/{continent_id}")
def getRegion(continent_id : int):
    Regions_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql="select * from regions where continent_id = {0}".format(continent_id)
    mycursor.execute(sql)
    for data_regions in mycursor:
        Regions_list.append( data_regions )
    mycursor.close()
    return {"Region": Regions_list}

#Refazer!!!
@app.post('/createContinent/{continent_name}')
def createContinent(continent_name: str):
    if continent_name == "":
        return {'Error': 'Item vazio'}
    mycursor = connection.mydb.cursor(dictionary=True)
    sql=" INSERT INTO continents (name) values ('{0}')".format(continent_name)
    mycursor.execute(sql)
    mycursor.close()
    return {"Continent: OK"}