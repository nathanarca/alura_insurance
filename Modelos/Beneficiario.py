from Modelos.Enumns import TipoRelacaoSegurado
from Modelos.Pessoa import Pessoa
from Modelos.Endereco import Endereco
from Modelos.Contato import Contato


class Beneficiario(Pessoa):

    def __init__(self, tipoRelacaoSegurado: TipoRelacaoSegurado, nome, sobrenome, cpf, rg, data_nascimento, sexo, endereco: Endereco, contato: Contato):

        self.__tipoRelacaoSegurado = tipoRelacaoSegurado

        Pessoa.__init__(self, nome, sobrenome, cpf, rg,
                        data_nascimento, sexo, endereco, contato)
        
    def __str__(self) -> str:
        return super().__str__() + " tipoRelacaoSegurado:" + str(self.__tipoRelacaoSegurado)
