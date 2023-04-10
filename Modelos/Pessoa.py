from datetime import datetime
from Modelos.Endereco import Endereco
from Modelos.Contato import Contato
from Services.ValidadorService import ValidadorService


class Pessoa:
    def __init__(self, nome, sobrenome, cpf, rg, data_nascimento: datetime, sexo, endereco: Endereco, contato: Contato):

        self.__nome = nome
        self.__sobrenome = sobrenome

        self.__cpf = cpf
        self.__rg = rg
        self.__data_nascimento: datetime = data_nascimento
        self.__sexo = sexo
        self.__endereco = endereco
        self.__contato = contato

        self.__validar()

    def __validar(self):
        self.__validarNome()
        self.__validarCpf()
        self.__validarDataNascimentoFutura()
        self.__validaRg()

    def __validarDataNascimentoFutura(self):
        if (self.__data_nascimento > datetime.now()):
            raise Exception("Data de nascimento não pode ser futura")

    def __validaRg(self):
        if (ValidadorService().stringIsEmpty(self.__rg)):
            raise Exception("RG Inválido")

    def __validarCpf(self):
        if (ValidadorService().isCpf(self.__cpf) == False):
            raise Exception("CPF Inválido")

    def __validarNome(self):
        if (ValidadorService().stringIsEmpty(self.__nome) | ValidadorService().stringIsEmpty(self.__sobrenome)):
            raise Exception("Nome e sobrenome não podem ser vazios")

        if (len(self.__nome) < 2 | len(self.__sobrenome) < 2):
            raise Exception(
                "Nome e sobrenome devem ter no mínimo 2 caracteres")

    def getCpf(self):
        return self.__cpf

    def getNome(self):
        return self.__nome

    def getSobrenome(self):
        return self.__sobrenome

    def getDataNascimento(self):
        return self.__data_nascimento

    def getNomeCompleto(self):
        return self.__nome + " " + self.__sobrenome

    def __str__(self) -> str:
        return "nome:" + self.__nome + " sobrenome:" + self.__sobrenome + " cpf:" + self.__cpf + " rg:" + self.__rg + " data_nascimento:" + self.__data_nascimento + " sexo:" + self.__sexo + " endereco:" + str(self.__endereco) + " contato:" + str(self.__contato)
