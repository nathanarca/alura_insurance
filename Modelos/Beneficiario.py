from Modelos.Pessoa import Pessoa
class Beneficiario(Pessoa):

    def __init__(self,tipoRelacaoSegurado,nome,sobrenome,cpf,rg,data_nascimento,sexo,endereco,contato):

        self.__tipoRelacaoSegurado = tipoRelacaoSegurado

        Pessoa.__init__(self,nome,sobrenome,cpf,rg,data_nascimento,sexo,endereco,contato)