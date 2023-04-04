from Services.ValidadorService import ValidadorService


class Endereco:

    def __init__(self, rua, numero, bairro, complemento, cidade, cep, estado):

        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__complemento = complemento
        self.__cidade = cidade
        self.__cep = cep
        self.__estado = estado

        self.__validar()

    def __validar(self):
        validador = ValidadorService()
        erros = []

        if (validador.stringIsEmpty(self.__rua)):
            erros.append("Rua não pode ser vazia")

        if (validador.stringIsEmpty(self.__numero)):
            erros.append("Número não pode ser vazio")

        if (validador.stringIsEmpty(self.__bairro)):
            erros.append("Bairro não pode ser vazio")

        if (validador.stringIsEmpty(self.__cidade)):
            erros.append("Cidade não pode ser vazia")

        if (validador.stringIsEmpty(self.__cep)):
            erros.append("CEP não pode ser vazio")

        if (validador.stringIsEmpty(self.__estado)):
            erros.append("Estado não pode ser vazio")
        else:
            if (validador.isValidUF(self.__estado) == False):
                erros.append("Estado inválido")

        if (len(erros) > 0):
            raise Exception(erros)

    def getEnderecoFormatado(self):
        return self.__rua + ", " + self.__numero + " - " + self.__bairro + " - " + self.__cidade + " - " + self.__estado

    def __str__(self) -> str:
        return "rua: " + self.__rua + " numero: " + self.__numero + " bairro: " + self.__bairro + " complemento: " + self.__complemento + " cidade: " + self.__cidade + " cep: " + self.__cep + " estado: " + self.__estado
