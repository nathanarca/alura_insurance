class Endereco:

    def __init__(self,rua,numero,bairro,complemento,cidade,cep,estado):

        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__complemento = complemento
        self.__cidade = cidade
        self.__cep = cep
        self.__estado = estado

    def getEnderecoFormatado(self):
        return self.__rua + ", " + self.__numero + " - " + self.__bairro + " - " + self.__cidade + " - " + self.__estado