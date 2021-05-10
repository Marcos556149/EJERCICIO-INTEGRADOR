class Proyecto:
    __idProyecto= ''
    __titulo= ''
    __palabrasClave= ''
    __puntos= ''
    def __init__(self,id='',tit='',pal='',pun=''):
        self.__idProyecto = id
        self.__titulo = tit
        self.__palabrasClave = pal
        self.__puntos = pun
    def __str__(self):
        return 'idProyecto: {}, Titulo: {}, Palabras Clave: {}, Puntos: {}'.format(self.__idProyecto,self.__titulo,self.__palabrasClave,self.__puntos)
    def getID(self):
        return self.__idProyecto
    def setPuntos(self,puntaje):
        self.__puntos += puntaje
    def getPuntos(self):
        return self.__puntos
    def __gt__(self,otro):
        return self.__puntos > otro.getPuntos()
