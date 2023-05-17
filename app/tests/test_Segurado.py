from Modelos.Segurado import Segurado

class test_Segurado:
    def test_deve_retornar_nome_completo_segurado(self):
        
        segurado = Segurado("João", "Silva", "12345678910")

        assert segurado.nome_completo() == "João Silva"