from Modelos.Enumns.TipoRelacaoSegurado import TipoRelacaoSegurado;
from Modelos.Contato import Contato;
from Modelos.Endereco import Endereco;
from Modelos.Segurado import Segurado;
from Modelos.Beneficiario import Beneficiario;

from Services.Repositorios.RepositorioSegurado import RepositorioSegurado

repositorio_segurado = RepositorioSegurado()

endereco = Endereco('Rua 1', '123', 'Centro', 'casa', 'São Paulo', '12345678',"SP")

contato = Contato('1234567890', '1234567890', '1234567890',"teste@teste.com")

beneficiario = Beneficiario(TipoRelacaoSegurado.AMIGO,'João', 'Silva','123.456.789-00', '1234567890','1995-07-19','M',endereco,contato)

segurado = Segurado('João', 'Silva','123.456.789-00', '1234567890','1995-07-19','M',endereco,contato,beneficiario)

repositorio_segurado.inserir(segurado)

primeiroSegurado = repositorio_segurado.listar()[0]

print(primeiroSegurado.getNomeCompleto())