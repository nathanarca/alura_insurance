import decimal
from Modelos.Apolice import Apolice
from Modelos.Enumns import TipoApolice


class RegraComissao():

    def __init__(self, tipo: TipoApolice):
        self.__tipo = tipo

    def aplica(self, apolice: Apolice):
        apolice.getTipo() == self.getTipo()

    def calcula(self, apolice: Apolice) -> decimal:
        raise NotImplementedError

    def getTipo(self):
        return self.__tipo
