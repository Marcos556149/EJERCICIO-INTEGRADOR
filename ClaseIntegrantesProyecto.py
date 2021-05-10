class IntegrantesProyecto:
    __idProyecto= ''
    __apellidoNombre= ''
    __dni= ''
    __categoriaInvestigacion= ''
    __rol= ''
    def __init__(self,id='',apeNom='',dn='',cat='',ro=''):
        self.__idProyecto = id
        self.__apellidoNombre = apeNom
        self.__categoriaInvestigacion = cat
        self.__dni = dn
        self.__rol = ro
    def __str__(self):
        return 'IdProyecto: {}, Apellido y Nombre: {}, DNI: {}, Categoria Investigacion: {}, Rol: {}'.format(self.__idProyecto,self.__apellidoNombre,self.__dni,self.__categoriaInvestigacion,self.__rol)
    def getIdd(self):
        return self.__idProyecto
    def getRol(self):
        return self.__rol
    def getCategoria(self):
        return self.__categoriaInvestigacion
