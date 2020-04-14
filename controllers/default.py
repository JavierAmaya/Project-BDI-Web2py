# -*- coding: utf-8 -*-
def view_catalogo():
    #catalogo = db.select(db.catalogo.CatalogoName)
    print("Estoy en el controller")
    catalogo= db(db.Catalogo.CatalogoID > 0).select(db.Catalogo.CatalogoName,db.Catalogo.Description)
    #s = db(db.Catalogo.CatalogoName)
    #people = s.select()
    return {"catalogo":catalogo}