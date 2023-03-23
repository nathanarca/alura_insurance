from Modelos.Pessoa import Pessoa
class Corretor(Pessoa):

    def __init__(self,numeroSusep,nome,sobrenome,cpf,rg,data_nascimento,sexo,endereco,contato):

        self.__apolices = []
        self.__numeroSusep = numeroSusep

        Pessoa.__init__(self,nome,sobrenome,cpf,rg,data_nascimento,sexo,endereco,contato)

    def adicionarApolice(self,apolice):
        self.__apolices.append(apolice)

    def removerApolice(self,numeroApolice):
        for apolice in self.apolices:
            if apolice.numero == numeroApolice:
                self.__apolices.remove(apolice)
                return True
        return False
    
    def getApolice(self,numeroApolice):

        for apolice in self.__apolices:
            if apolice.numero == numeroApolice:
                return apolice
        return None

    def getApolices(self):
        return self.__apolices
    
    def calcularComissao(self):
        comissao = 0
        for apolice in self.__apolices:
            comissao += apolice.valorPremio * 0.01
        return comissao
