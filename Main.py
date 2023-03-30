from Modelos.Apolice import Apolice
from Modelos.Corretor import Corretor
from Modelos.Enumns.StatusApolice import StatusApolice
from Modelos.Enumns.TipoApolice import TipoApolice
from Modelos.Enumns.TipoRelacaoSegurado import TipoRelacaoSegurado
from Modelos.Contato import Contato
from Modelos.Endereco import Endereco
from Modelos.Segurado import Segurado
from Modelos.Beneficiario import Beneficiario

from Repositorios.RepositorioSegurado import RepositorioSegurado

repositorio_segurado = RepositorioSegurado()

endereco = Endereco('Rua 1', '123', 'Centro', 'casa',
                    'São Paulo', '12345678', "SP")

contato = Contato('1234567890', '1234567890', '1234567890', "teste@teste.com")

beneficiario = Beneficiario(TipoRelacaoSegurado.AMIGO, 'João', 'Silva','123.456.789-00', '1234567890', '1995-07-19', 'M', endereco, contato)

segurado = Segurado('João', 'Silva', '123.456.789-00', '1234567890',     '1995-07-19', 'M', endereco, contato, beneficiario)

corretor = Corretor("123456", "João", "Silva", "123.456.789-00","1234567890", "1995-07-19", "M", endereco, contato)

apolice1 = Apolice(123, TipoApolice.VIDA, 15.50, 895000, segurado, "2020-01-01", "2020-01-01", StatusApolice.ATIVA)
apolice2 = Apolice(123, TipoApolice.CARRO, 150.50, 60000, segurado, "2020-01-01", "2020-01-01", StatusApolice.ATIVA)
apolice3 = Apolice(123, TipoApolice.CASA, 15.50, 25000, segurado, "2020-01-01", "2020-01-01", StatusApolice.ATIVA)
apolice3 = Apolice(123, TipoApolice.VIAGEM, 15.50, 25000, segurado, "2020-01-01", "2020-01-01", StatusApolice.ATIVA)

corretor.adicionarApolice(apolice1)
corretor.adicionarApolice(apolice2)
corretor.adicionarApolice(apolice3)

comissao = corretor.calcularComissao()

print(comissao)