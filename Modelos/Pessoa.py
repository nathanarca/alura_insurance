from Modelos.Endereco import Endereco
from Modelos.Contato import Contato

class Pessoa:
    def __init__(self,nome,sobrenome,cpf,rg,data_nascimento,sexo,endereco,contato):


        if not isinstance(endereco,Endereco):
            raise TypeError("Endereço deve ser do tipo Endereco")

        if not isinstance(contato,Contato):
            raise TypeError("Contato deve ser do tipo Contato")

        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__rg = rg
        self.__data_nascimento = data_nascimento
        self.__sexo = sexo
        self.__endereco = endereco
        self.__contato = contato