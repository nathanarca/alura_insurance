import decimal
from Modelos.Apolice import Apolice
from Modelos.Enumns.TipoApolice import TipoApolice
from Modelos.RegrasDeComissao.RegraComissaoFactory import RegraComissao


class RegraComissaoCarro(RegraComissao):

    def __init__(self):
        super().__init__(TipoApolice.CARRO)

    def calcula(self, apolice: Apolice) -> decimal:

        valorApolice = apolice.getValorApolice()

        varlorFixo = 75.50

        valorSobreApolice = valorApolice * 0.035

        return varlorFixo + valorSobreApolice