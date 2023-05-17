from Modelos.Apolice import Apolice
from Modelos.Enumns.TipoApolice import TipoApolice
from Modelos.RegrasDeComissao.RegraComissaoFactory import RegraComissao


class RegraComissaoCasa(RegraComissao):

    def __init__(self):
        super().__init__(TipoApolice.CASA)

    def calcula(self, apolice: Apolice):

        return 200
