import urllib.request

class Internet_connection():

    @staticmethod
    def conectar(self, host='http://google.com'):
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False