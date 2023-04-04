from Modelos.Segurado import Segurado

class RepositorioSegurado:

    def __init__(self):
        self.__segurados = []

    def inserir(self, segurado : Segurado):
        
        self.__segurados.append(segurado)

    def listar(self) -> list[Segurado]:
        return self.__segurados

    def buscar_por_cpf(self, cpf) -> Segurado: 
        for segurado in self.__segurados:
            if segurado.cpf == cpf:
                return segurado
        return None

    def remover(self, cpf):
        segurado = self.buscar_por_cpf(cpf)
        if segurado:
            self.__segurados.remove(segurado)
