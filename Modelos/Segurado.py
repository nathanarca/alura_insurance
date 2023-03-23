from Modelos.Pessoa import Pessoa
from Modelos.Beneficiario import Beneficiario

class Segurado(Pessoa):

    def __init__(self,nome,sobrenome,cpf,rg,data_nascimento,sexo,endereco,contato, beneficiario):

        if not isinstance(beneficiario,Beneficiario):
            raise TypeError("Endereço deve ser do tipo Endereco")

        Pessoa.__init__(self,nome,sobrenome,cpf,rg,data_nascimento,sexo,endereco,contato)
        
        self.__beneficiario = beneficiario

    def getNomeCompleto(self):
        return self.__nome + " " + self.__sobrenome
