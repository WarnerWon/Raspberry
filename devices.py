from gpiozero import DistanceSensor
from gpiozero import MotionSensor
import datetime
from time import sleep
from mongo import Mymongo
from internet import Internet_connection
from signal import pause

class Ultrasonido():

    def __init__(self, sensorId=1, echo=23, trigger=24):
        self.id = sensorId
        self.sensor = DistanceSensor(echo, trigger)
    
    def leerDistancia(self):
        return self.sensor.distance

    def subirDatos(self):
        datos = {
            "id": self.id,
            "Dispositivo" : "Ultrasonido",
            "Distancia" : self.sensor.distance}

        if (Internet_connection.conectar()):
            puntero = Mymongo()
            puntero.insert(datos=datos)


class PIR():

    def __init__(self, sensorId=1, señal=23):
        self.sensorId = sensorId    
        self.sensor = MotionSensor(señal)
    
    def estaActivo(self):
        esta_activo = self.sensor.value
        
        if (esta_activo==1): return True

        if (esta_activo==0): return False

    def subirDatos(self):
        datos = {
            "Dispositivo" : "PIR",
            "Fecha_Activacion" : datetime.datetime.now()}

        if (Internet_connection.conectar()):
            puntero = Mymongo()
            puntero.insert(datos=datos)
            
class Dht11():

    def __init__(self,):    
        return None
    
    def leerDistancia(self):
        esta_activo = self.sensor.value
        
        if (esta_activo==1): return True

        if (esta_activo==0): return False

    def subirDatos(self):
        datos = {"Fecha_Activacion" : datetime.datetime.now()}
        coleccion = "PIR"

        if (Internet_connection.conectar()):
            puntero = Mymongo()
            puntero.insert(coleccion=coleccion,datos=datos)
            

