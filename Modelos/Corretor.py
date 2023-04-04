from typing import List
from Modelos.Apolice import Apolice
from Modelos.Pessoa import Pessoa
from Modelos.Endereco import Endereco
from Modelos.Contato import Contato
from Services.CalculadoraComissaoService import CalculadoraComissaoService


class Corretor(Pessoa):

    def __init__(self, numeroSusep, nome, sobrenome, cpf, rg, data_nascimento, sexo, endereco: Endereco, contato: Contato):

        self.__apolices: List[Apolice] = []

        self.__numeroSusep = numeroSusep

        Pessoa.__init__(self, nome, sobrenome, cpf, rg,
                        data_nascimento, sexo, endereco, contato)

        self.__validar()

    def __validar(self):
        self.__validarNumeroSusep()

    def __validarNumeroSusep(self):
        start = "154146"
        if (not self.__numeroSusep.startswith(start) or len(self.__numeroSusep) != 17):
            raise Exception("Número Susep inválido")

    def adicionarApolice(self, apolice: Apolice):
        self.__apolices.append(apolice)

    def removerApolice(self, numeroApolice):
        for apolice in self.apolices:
            if apolice.numero == numeroApolice:
                self.__apolices.remove(apolice)
                return True
        return False

    def getApolice(self, numeroApolice) -> Apolice:

        for apolice in self.__apolices:
            if apolice.numero == numeroApolice:
                return apolice
        return None

    def getNumeroSusep(self):
        return self.__numeroSusep

    def getApolices(self) -> List[Apolice]:
        return self.__apolices

    def calcularComissao(self):
        calculadorComissao = CalculadoraComissaoService()
        return calculadorComissao.calcular(self.__apolices)

    def __str__(self) -> str:
        return super().__str__() + " numeroSusep:" + self.__numeroSusep + " apolices:" + str(self.__apolices)
