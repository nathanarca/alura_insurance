from typing import List
from Modelos.Apolice import Apolice
from Modelos.Enumns.TipoApolice import TipoApolice
from Modelos.RegrasDeComissao.RegraComissao import RegraComissao
from Modelos.RegrasDeComissao.RegraComissaoCarro import RegraComissaoCarro
from Modelos.RegrasDeComissao.RegraComissaoCasa import RegraComissaoCasa
from Modelos.RegrasDeComissao.RegraComissaoViagem import RegraComissaoViagem
from Modelos.RegrasDeComissao.RegraComissaoVida import RegraComissaoVida


class RegraComissaoFactory:

    def __init__(self):

        self.regras = {
            TipoApolice.VIDA: RegraComissaoVida(),
            TipoApolice.CARRO: RegraComissaoCarro(),
            TipoApolice.VIAGEM: RegraComissaoViagem(),
            TipoApolice.CASA: RegraComissaoCasa(),
        }

    def getRegraComissao(self, apolice: Apolice) -> RegraComissao:
        return self.regras[apolice.getTipo()]

    def __str__(self):
        return self.__class__.__name__
