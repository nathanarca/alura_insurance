import datetime
import decimal
import uuid
from Modelos.Enumns.StatusApolice import StatusApolice
from Modelos.Enumns.TipoApolice import TipoApolice
from Modelos.Segurado import Segurado


class Apolice:
    def __init__(self, tipo: TipoApolice, valorPremio, valorBeneficio, segurado: Segurado, vigencia: datetime, dataCriacao: datetime, status: StatusApolice):

        self.__numero = uuid.uuid4()
        self.__segurado = segurado
        self.__tipo = TipoApolice(tipo)
        self.__valorPremio = valorPremio
        self.__valorBeneficio = valorBeneficio
        self.__vigencia = vigencia
        self.__dataCricao = dataCriacao
        self.__status = StatusApolice(status)

        self.__validar()

    def __validar(self):
        self.__validarSegurado()
        self.__validarValorBeneficio()
        self.__validarValorPremio()
        self.__validarVigencia()
        self.__validarDataCriacao()
        self.__validarStatus()
        self.__validarTipo()

    def __validarTipo(self):
        tiposLiberados = [TipoApolice.VIDA]
        if (self.__tipo not in tiposLiberados):
            raise Exception("Tipo de apólice não permitido")

    def __validarStatus(self):
        if (self.__status is None):
            raise Exception("O status é obrigatório")

    def __validarDataCriacao(self):
        if (self.__dataCricao > datetime.datetime.now()):
            raise Exception(
                "A data de criação não pode ser maior que a data atual")

    def __validarVigencia(self):
        if (self.__vigencia < datetime.datetime.now()):
            raise Exception("A vigência não pode ser menor que a data atual")

    def __validarValorPremio(self):
        if (self.__valorPremio <= 0):
            raise Exception("O valor do prêmio deve ser maior que zero")

    def __validarValorBeneficio(self):
        if (self.__valorBeneficio <= 0):
            raise Exception("O valor do benefício deve ser maior que zero")

    def __validarSegurado(self):
        if (self.__segurado is None):
            raise Exception("O segurado é obrigatório")

    def getPremio(self) -> decimal:
        return self.__valorPremio

    def getValorApolice(self) -> decimal:
        return self.__valorBeneficio

    def getTipo(self) -> TipoApolice:
        return self.__tipo

    def __str__(self) -> str:
        return "codigoSusepCorretor: " + self.__corretor + " segurado: " + self.__segurado + " numero: " + self.__numero + " tipo: " + str(self.__tipo) + " valorPremio: " + self.__valorPremio + " valorBeneficio: " + self.__valorBeneficio + " vigencia: " + self.__vigencia + " dataCricao: " + self.__dataCricao + " status: " + self.__status
