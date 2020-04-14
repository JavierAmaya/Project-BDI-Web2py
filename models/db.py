# -*- coding: utf-8 -*-

#from gluon.dal import DAL, Field
import pyodbc 
from pydal import DAL, Field

server = 'tcp:unahvjamaya.database.windows.net' 
database = 'ingreso_vehiculos' 
username = 'vjamaya' 
password = 'Admin203Amaya.' 
#db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

#db = DAL("mssql://vjamaya:Admin203Amaya.@unahvjamaya.database.windows.net/ingreso_vehiculos",migrate_enabled=False)
db = DAL('mssql://DRIVER={ODBC Driver 17 for SQL Server};SERVER=unahvjamaya.database.windows.net;DATABASE=ingreso_vehiculos;UID=vjamaya;PWD=Admin203Amaya.',migrate_enabled = False)

db.define_table(
    "Catalogo",
    Field("CatalogoID",type="id"),
    Field("CatalogoName"),
    Field("Description"),
    migrate=False
)
id = db.Catalogo.insert(CatalogoID="222", CatalogoName="MandeleGAs",Description="La gran banda")
#id=db.post.insert(title="Juan", content="esto es parte del contenido")
#s = db(db.person.age > 18)
#people = s.select()

#De aqui para abajo funciona con pyodbc

#cursor = cnxn.cursor()
#Sample insert query
#cursor.execute("""
#INSERT INTO museo.Catalogo (CatalogoID,CatalogoName, Description) 
#VALUES (?,?,?)""",
#'100', 'Yeso','esta es una descripcion') 
#cnxn.commit()
#row = cursor.fetchone()
#while row: 
#    print('Inserted Product key is ' + str(row[4]))
#    row = cursor.fetchone()