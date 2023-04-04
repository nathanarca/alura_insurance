from datetime import datetime
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

endereco = Endereco('Rua 1', '123', 'Centro', 'casa', 'São Paulo', '12345678', "SP")

contato = Contato('11111111111', '1234567890', '1234567890', "teste@teste.com")

beneficiario = Beneficiario(TipoRelacaoSegurado.AMIGO, 'João', 'Silva','162.711.077.10', '1234567890', datetime(2015,7,19), 'M', endereco, contato)

segurado = Segurado('João', 'Silva', '162.711.077.10', '1234567890',datetime(1995,7,19), 'M', endereco, contato, beneficiario)

corretor = Corretor("15414614151917181", "João", "Silva", '162.711.077.10',"1234567890",datetime(1995,7,19), "M", endereco, contato)

segurado.addBeneficiario(Beneficiario(TipoRelacaoSegurado.AMIGO, 'Pedro', 'Paulo','764.271.590-03', '1234567890', datetime(1995,7,19), 'M', endereco, contato))
segurado.addBeneficiario(Beneficiario(TipoRelacaoSegurado.AMIGO, 'Pedro', 'Paulo','479.442.640-22', '1234567890', datetime(1995,7,19), 'M', endereco, contato))
segurado.addBeneficiario(Beneficiario(TipoRelacaoSegurado.AMIGO, 'Pedro', 'Paulo','784.716.890-14', '1234567890', datetime(1995,7,19), 'M', endereco, contato))
segurado.addBeneficiario(Beneficiario(TipoRelacaoSegurado.AMIGO, 'Pedro', 'Paulo','473.583.640-31', '1234567890', datetime(1995,7,19), 'M', endereco, contato))
segurado.addBeneficiario(Beneficiario(TipoRelacaoSegurado.AMIGO, 'Pedro', 'Paulo','603.947.690-74', '1234567890', datetime(1995,7,19), 'M', endereco, contato))
segurado.addBeneficiario(Beneficiario(TipoRelacaoSegurado.AMIGO, 'Pedro', 'Paulo','621.273.750-92', '1234567890', datetime(1995,7,19), 'M', endereco, contato))
segurado.addBeneficiario(Beneficiario(TipoRelacaoSegurado.AMIGO, 'Pedro', 'Paulo','014.199.950-06', '1234567890', datetime(1995,7,19), 'M', endereco, contato))
segurado.addBeneficiario(Beneficiario(TipoRelacaoSegurado.AMIGO, 'Pedro', 'Paulo','893.695.780-56', '1234567890', datetime(1995,7,19), 'M', endereco, contato))
segurado.addBeneficiario(Beneficiario(TipoRelacaoSegurado.AMIGO, 'Pedro', 'Paulo','536.726.000-40', '1234567890', datetime(1995,7,19), 'M', endereco, contato))
# segurado.addBeneficiario(Beneficiario(TipoRelacaoSegurado.AMIGO, 'Pedro', 'Paulo','737.257.080-88', '1234567890', datetime(1995,7,19), 'M', endereco, contato))


apolice1 = Apolice(TipoApolice.VIDA, 15.50, 895000, segurado, datetime(2024,1,1), datetime(2020,1,1), StatusApolice.ATIVA)
apolice2 = Apolice(TipoApolice.VIDA, 150.50, 60000, segurado, datetime(2024,1,1), datetime(2020,1,1), StatusApolice.ATIVA)
apolice3 = Apolice(TipoApolice.VIDA, 15.50, 25000, segurado, datetime(2024,1,1), datetime(2020,1,1), StatusApolice.ATIVA)
apolice3 = Apolice(TipoApolice.VIDA, 15.50, 25000, segurado, datetime(2024,1,1), datetime(2020,1,1), StatusApolice.ATIVA)

corretor.adicionarApolice(apolice1)
corretor.adicionarApolice(apolice2)
corretor.adicionarApolice(apolice3)

comissao = corretor.calcularComissao()

print(comissao)