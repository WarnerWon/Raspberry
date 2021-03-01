from pymongo import MongoClient

class Mymongo():

    def __init__(self):
        self.puntero = MongoClient("")
        self.baseDatos = self.puntero['Raspberry']

    def insert(self,datos={}):
        mycol = self.baseDatos["Dispositivos"]
        x = mycol.insert_one(datos)
        return x
