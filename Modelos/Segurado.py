from ast import List
from datetime import datetime
from Modelos.Pessoa import Pessoa
from Modelos.Beneficiario import Beneficiario


class Segurado(Pessoa):

    def __init__(self, nome, sobrenome, cpf, rg, data_nascimento, sexo, endereco, contato, beneficiario: Beneficiario):

        Pessoa.__init__(self, nome, sobrenome, cpf, rg,
                        data_nascimento, sexo, endereco, contato)

        self.__beneficiarios: List[Beneficiario] = []

        self.addBeneficiario(beneficiario)
        
        self.__validarNascimento()

    def addBeneficiario(self, beneficiario: Beneficiario):
        self.__validarSePodeAdicionarBeneficiario(beneficiario)
        self.__beneficiarios.append(beneficiario)

    def __validarNascimento(self):
        idade = datetime.now().year - self.getDataNascimento().year
        if (idade < 18):
            raise Exception("O segurado deve ter no mínimo 18 anos")

    def __validarSePodeAdicionarBeneficiario(self, beneficiario: Beneficiario):

        # validar se o beneficiario já existe  pelo cpf
        if (self.__beneficiarios.__len__() > 0):
            for item in self.__beneficiarios:
                if (item.getCpf() == beneficiario.getCpf()):
                    raise Exception("O beneficiário já existe")

        if (self.__beneficiarios.__len__() >= 10):
            raise Exception("O segurado já possui 10 beneficiários")

    def __str__(self) -> str:
        return super().__str__() + " beneficiario:" + str(self.__beneficiario)
