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
    
    def __str__(self) -> str:
        return "rua: " + self.__rua + " numero: " + self.__numero + " bairro: " + self.__bairro + " complemento: " + self.__complemento + " cidade: " + self.__cidade + " cep: " + self.__cep + " estado: " + self.__estado