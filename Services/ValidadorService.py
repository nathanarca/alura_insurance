import re


class ValidadorService:

    def isCpf(self, cpf):
        # validar se o cpf é válido - SALVE CHATGPT!
        cpf = cpf.replace('.', '').replace('-', '')  # remover pontos e hífen
        if len(cpf) != 11 or not cpf.isdigit():
            return False
        # Calcular o primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = 11 - soma % 11
        if resto == 10 or resto == 11:
            resto = 0
        if resto != int(cpf[9]):
            return False
        # Calcular o segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = 11 - soma % 11
        if resto == 10 or resto == 11:
            resto = 0
        if resto != int(cpf[10]):
            return False
        return True

    def stringIsEmpty(self, string):
        return not string or not string.strip()

    def isValidUF(self, uf):
        ufsValidas = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
                      'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        return uf in ufsValidas

    def isCelular(self, celular):
        celular = celular.replace('(', '').replace(
            ')', '').replace('-', '').replace(' ', '')
        if len(celular) != 11 or not celular.isdigit():
            return False
        return True

    def isEmail(self, email):
        padrao = r'^([a-zA-Z0-9]+[_\.\-]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[\.\-]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
        return re.match(padrao, email) is not None
