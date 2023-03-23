from Modelos.Endereco import Endereco
from Modelos.Contato import Contato

class Pessoa:
    def __init__(self,nome,sobrenome,cpf,rg,data_nascimento,sexo,endereco: Endereco,contato: Contato):

        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__rg = rg
        self.__data_nascimento = data_nascimento
        self.__sexo = sexo
        self.__endereco = endereco
        self.__contato = contato

    def getNome(self):
        return self.__nome
    
    def getSobrenome(self):

        return self.__sobrenome
    
    def getNomeCompleto(self):
        return self.__nome + " " + self.__sobrenome