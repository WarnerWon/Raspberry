import jsonpickle

class FileManager:

    @staticmethod
    def readFile(archivo):

        route = archivo + 'test.json'

        with open(route, 'r') as inputLista:
            outputLista = []
            data = inputLista.read()
            jsonobject = jsonpickle.decode(data)
            lista = jsonobject["data"]
            for objeto in lista:
                outputLista.append(objeto)
            return outputLista

    @staticmethod
    def writeFile(archivo, datos):

        route = archivo +'.json'

        with open(route, 'w') as inputLista:
            datosCodificados = jsonpickle.encode(datos,indent=4)
            inputLista.write(datosCodificados)
            return True