class Contato:

    def __init__(self,celular,telefoneResidencial,telefoneComercial,email):

        self.__celular = celular
        self.__telefoneResidencial  = telefoneResidencial
        self.__telefoneComercial  = telefoneComercial
        self.__email = email

    def __str__(self) -> str:
        return "celular: " + self.__celular + " telefoneResidencial: " + self.__telefoneResidencial + " telefoneComercial: " + self.__telefoneComercial + " email: " + self.__email