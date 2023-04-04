from Modelos.Pessoa import Pessoa
from Modelos.Beneficiario import Beneficiario

class Segurado(Pessoa):

    def __init__(self,nome,sobrenome,cpf,rg,data_nascimento,sexo,endereco,contato, beneficiario: Beneficiario):

        Pessoa.__init__(self,nome,sobrenome,cpf,rg,data_nascimento,sexo,endereco,contato)
        
        self.__beneficiario = beneficiario