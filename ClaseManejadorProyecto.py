import csv
from ClaseProyectos import Proyecto
from ClaseManejadorIntegrantesProyecto import ManejadorIntegrantesProyecto
class ManejadorProyecto:
    __listaProyectos= []
    def __init__(self):
        self.__listaProyectos= []
    def leerArchivoProyecto(self):
        archivo1= open('proyectos.csv')
        reader= csv.reader(archivo1,delimiter=';')
        bandera= True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                id= fila[0]
                tit= fila[1]
                pal= fila[2]
                pun= int(fila[3])
                proyectoo= Proyecto(id,tit,pal,pun)
                self.__listaProyectos.append(proyectoo)
        archivo1.close()
    def calcularPuntos(self,listaIntegranteProyecto):
        for i,Proyecto in enumerate(self.__listaProyectos):
            directorOcodirector= True
            idPro= Proyecto.getID()
            print("Proyecto: {}\n".format(idPro))
            total= listaIntegranteProyecto.consultarIntegrantes(idPro)
            if total >= 3:
                self.__listaProyectos[i].setPuntos(10)
            else:
                self.__listaProyectos[i].setPuntos(-20)
                print("El Proyecto debe tener como minimo 3 integrantes")
            verificar= listaIntegranteProyecto.verificarDirector(idPro)
            if verificar == 1:
                self.__listaProyectos[i].setPuntos(-5)
                print("El Director del Proyecto debe tener categoria I o II")
            elif verificar == 2:
                self.__listaProyectos[i].setPuntos(10)
            else:
                self.__listaProyectos[i].setPuntos(-10)
                directorOcodirector= False
                print("El Proyecto debe tener un Director")
            verificar2= listaIntegranteProyecto.verificarCodirector(idPro)
            if verificar2 == 1:
                self.__listaProyectos[i].setPuntos(-5)
                print("El Codirector del Proyecto debe tener como mínimo categoría III")
            elif verificar2 == 2:
                self.__listaProyectos[i].setPuntos(10)
            else:
                if directorOcodirector:
                    self.__listaProyectos[i].setPuntos(-10)
                print("El Proyecto debe tener un Codirector")
    def listarProyectos(self):
        self.__listaProyectos.sort(reverse=True)
        for Proyecto in self.__listaProyectos:
            print("\n",Proyecto)
