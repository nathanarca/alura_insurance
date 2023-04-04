
from typing import List
from Modelos.Apolice import Apolice
from Modelos.RegrasDeComissao.RegraComissaoFactory import RegraComissaoFactory


class CalculadoraComissaoService():

    def __init__(self):
        self.__regraComissaoFactory = RegraComissaoFactory()

    def calcular(self, apolices: List[Apolice]):

        comissaoTotal = 0

        for apolice in apolices:
            comissaoTotal += self.__regraComissaoFactory.getRegraComissao(
                apolice).calcula(apolice)

        return comissaoTotal
