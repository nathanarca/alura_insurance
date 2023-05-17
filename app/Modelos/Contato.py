from Services.ValidadorService import ValidadorService


class Contato:

    def __init__(self, celular, telefoneResidencial, telefoneComercial, email):

        self.__celular = celular
        self.__telefoneResidencial = telefoneResidencial
        self.__telefoneComercial = telefoneComercial
        self.__email = email

        self.__validar()

    def __validar(self):
        self.__validarCelular()
        self.__validarEmail()

    def __validarCelular(self):
        if (ValidadorService().isCelular(self.__celular) == False):
            raise Exception("Celular Inválido")
        
    def __validarEmail(self):
        if (ValidadorService().isEmail(self.__email) == False):
            raise Exception("Email Inválido")

    def __str__(self) -> str:
        return "celular: " + self.__celular + " telefoneResidencial: " + self.__telefoneResidencial + " telefoneComercial: " + self.__telefoneComercial + " email: " + self.__email
