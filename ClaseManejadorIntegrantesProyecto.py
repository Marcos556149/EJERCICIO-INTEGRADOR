import csv
from ClaseIntegrantesProyecto import IntegrantesProyecto
class ManejadorIntegrantesProyecto:
    __listaIntegrantes= []
    def __init__(self):
        self.__listaIntegrantes= []
    def leerArchivoIntegrantes(self):
        archivo2= open('integrantesProyecto.csv')
        reader= csv.reader(archivo2,delimiter=';')
        bandera= True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                id= fila[0]
                apeNom= fila[1]
                dn= fila[2]
                cat= fila[3]
                ro= fila[4]
                integrante= IntegrantesProyecto(id,apeNom,dn,cat,ro)
                self.__listaIntegrantes.append(integrante)
        archivo2.close()
    def consultarIntegrantes(self,id):
        cant=0
        for IntegrantesProyecto in self.__listaIntegrantes:
            if (IntegrantesProyecto.getIdd() == id)and(IntegrantesProyecto.getRol() == 'integrante'):
                cant += 1
        return cant
    def verificarDirector(self,idd):
        numVerificar= 0
        j= 0
        bandera= True
        while (bandera)and(j < len(self.__listaIntegrantes)):
            if (self.__listaIntegrantes[j].getIdd() == idd)and(self.__listaIntegrantes[j].getRol() == 'director'):
                bandera= False
                numVerificar= 1
                if (self.__listaIntegrantes[j].getCategoria() == 'I')or(self.__listaIntegrantes[j].getCategoria() == 'II'):
                    numVerificar= 2
            j += 1
        return numVerificar
    def verificarCodirector(self,iddd):
        numVerificar1= 0
        k= 0
        bandera1= True
        while (bandera1)and(k < len(self.__listaIntegrantes)):
            if (self.__listaIntegrantes[k].getIdd() == iddd)and(self.__listaIntegrantes[k].getRol() == 'codirector'):
                bandera1= False
                numVerificar1= 1
                if (self.__listaIntegrantes[k].getCategoria() == 'I')or(self.__listaIntegrantes[k].getCategoria() == 'II')or(self.__listaIntegrantes[k].getCategoria() == 'III'):
                    numVerificar1= 2
            k += 1
        return numVerificar1
