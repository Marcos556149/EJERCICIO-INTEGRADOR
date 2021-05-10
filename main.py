from ClaseManejadorProyecto import ManejadorProyecto
from ClaseManejadorIntegrantesProyecto import ManejadorIntegrantesProyecto
if __name__=='__main__':
    listaProyectoo= ManejadorProyecto()
    listaProyectoo.leerArchivoProyecto()
    listaIntegranteProyecto= ManejadorIntegrantesProyecto()
    listaIntegranteProyecto.leerArchivoIntegrantes()
    listaProyectoo.calcularPuntos(listaIntegranteProyecto)
    listaProyectoo.listarProyectos()
