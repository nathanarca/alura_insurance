from Modelos.Corretor import Corretor
from Modelos.Segurado import Segurado


class Apolice:
    def __init__(self,numero,tipo,valorPremio,valorBeneficio,segurado,corretor,vigencia,dataCriacao,status):

        if not isinstance(segurado,Segurado):
            raise TypeError("Segurado deve ser do tipo Segurado")
        
        if not isinstance(corretor,Corretor):
            raise TypeError("Corretor deve ser do tipo Corretor")

        self.__corretor = corretor
        self.__segurado = segurado
        self.__numero = numero
        self.__tipo  = tipo
        self.__valorPremio = valorPremio
        self.__valorBeneficio = valorBeneficio
        self.__vigencia = vigencia
        self.__dataCricao = dataCriacao
        self.__status = status