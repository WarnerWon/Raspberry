import mysql.connector as BD

class Mysql():

    def __init__(self):
        self.mydb = BD.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="dispositivos",
        port=3307
        )
        self.mycursor = self.mydb.cursor()

    def insert(self,table="",data={}):

        sql = self.sentenceGenerator("INSERT",table,data.keys())
        
        myInput = self.valuesGenerator(data.values())

        self.mycursor.execute(sql,myInput)

        self.mydb.commit()

    def sentenceGenerator(self, action="", table="", keys=[]):
        parentesis = "( "
        val_count = "("

        for key in keys:
            parentesis += key
            parentesis += ", " 
            val_count += "%s,"

        parentesis = parentesis[:-2]
        val_count = val_count[:-1]
        parentesis += ")"
        val_count +=")"

        sql = action + " INTO " + table + " " + parentesis + " VALUES " + val_count

        return sql
        
    def valuesGenerator(self, values):
        
        newValues = []
        for val in values:
            newValues.append(val)
        myInput = tuple(newValues)

        return myInput