from Modelos.Apolice import Apolice
from Modelos.Enumns.TipoApolice import TipoApolice
from Modelos.RegrasDeComissao.RegraComissaoFactory import RegraComissao


class RegraComissaoVida(RegraComissao):

    def __init__(self):
        super().__init__(TipoApolice.VIDA)

    def calcula(self, apolice: Apolice):

        valorApolice = apolice.getValorApolice()

        varlorFixo = 100

        if (valorApolice > 850000):
            varlorFixo += 1000

        valorSobreApolice = valorApolice * 0.05

        return varlorFixo + valorSobreApolice
