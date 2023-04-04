import datetime
import decimal
from Modelos.Enumns import TipoApolice
from Modelos.Segurado import Segurado


class Apolice:
    def __init__(self, numero, tipo: TipoApolice, valorPremio, valorBeneficio, segurado: Segurado, vigencia: datetime, dataCriacao: datetime, status):

        self.__segurado = segurado
        self.__numero = numero
        self.__tipo = tipo
        self.__valorPremio = valorPremio
        self.__valorBeneficio = valorBeneficio
        self.__vigencia = vigencia
        self.__dataCricao = dataCriacao
        self.__status = status

    def getPremio(self) -> decimal:
        return self.__valorPremio

    def getValorApolice(self) -> decimal:
        return self.__valorBeneficio

    def getTipo(self) -> TipoApolice:
        return self.__tipo

    def __str__(self) -> str:
        return "codigoSusepCorretor: " + self.__corretor + " segurado: " + self.__segurado + " numero: " + self.__numero + " tipo: " + str(self.__tipo) + " valorPremio: " + self.__valorPremio + " valorBeneficio: " + self.__valorBeneficio + " vigencia: " + self.__vigencia + " dataCricao: " + self.__dataCricao + " status: " + self.__status
