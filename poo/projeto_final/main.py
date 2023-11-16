import fastapi
import connection
import json

app = fastapi.FastAPI()
@app.get("/")
def hello_world_root():
    return {"Olá": "Funciona"}

@app.get("/getProduto")
def getProduto():
    Produto_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from Produto"
    mycursor.execute(sql)
    for data_produto in mycursor:
        Produto_list.append( data_produto )
    mycursor.close()
    return {"Produto": Produto_list}

@app.get("/getProduto/{Id_Produto}")
def getProduto(Id_Produto: int):
    Produto_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from Produto where IdProduto = {0}".format(Id_Produto)
    mycursor.execute(sql)
    for data_produto in mycursor:
        Produto_list.append( data_produto )
    mycursor.close()
    return {"Produto": Produto_list}

@app.post('/createProduto/{produto_name}/{produto_description}')
def createProduto(produto_name: str, produto_description: str):
    if produto_name == "" or produto_description == "":
        return {'Error': 'Item vazio'}
    mycursor = connection.mydb.cursor(dictionary=True)
    sql=" INSERT INTO Produto (NomeProduto, DescricaoProduto) values ('{0}','{1}')".format(produto_name,produto_description)
    mycursor.execute(sql)
    mycursor.execute("COMMIT;")
    mycursor.close()
    return {"Produto: OK"+produto_description}

@app.delete("/DeleteProduto/{produto_id}")
def DeleteContinent(produto_id : int):
    Produto_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql="select * from Produto where IdProduto = {0}".format(produto_id)
    mycursor.execute(sql)
    for data_produto in mycursor:
        Produto_list.append( data_produto )
    mycursor.close()
    if len(Produto_list) == 0:
        return {'Message': 'Produto não encontrado'}
    else:
        mycursor_del = connection.mydb.cursor(dictionary=True)
        sql_del = "DELETE from Produto where IdProduto = {0}".format(produto_id)
        mycursor_del.execute(sql_del)
        mycursor_del.execute("COMMIT;")
        mycursor_del.close()
        return {'Message': 'Produto deletado com sucesso - '+str(produto_id)}
    
@app.patch('/updateProduto/{produto_id}/{produto_name}')
def createProduto(produto_id : int, produto_name: str, produto_descricao: str):
    Produto_list = []
    if produto_name == "" or produto_id == 0:
        return {'Error': 'Empty Item'}
    mycursor = connection.mydb.cursor(dictionary=True)
    sql="select * from Produto where IdProduto = {0}".format(produto_id)
    mycursor.execute(sql)
    for data_produto in mycursor:
        Produto_list.append( data_produto )
    mycursor.close()
    if len(Produto_list) == 0:
        return {'Message': 'Produto não existe'}
    else:
        mycursor_del = connection.mydb.cursor(dictionary=True)
        sql_del = "update Produto set NomeProduto = '{0}' where IdProduto = {1}".format(produto_name,produto_id)
        mycursor_del.execute(sql_del)
        mycursor_del.execute("COMMIT;")
        mycursor_del.close()
        return {'Message': 'Produto Atualizado com Sucesso - '+str(produto_id)}