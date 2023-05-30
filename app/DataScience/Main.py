import numpy as np

size = 500000


masculino = 0
feminino = 1

casado = 1
solteiro = 2
divorciado = 3
viuvo = 4

ids = np.arange(1, size + 1)

idades = np.random.randint(18, 82, size=size)

sexos = np.random.choice([masculino, feminino], size=size)

estados_civis = np.random.choice([solteiro, casado, divorciado, viuvo], size=size)

sinistros = np.random.randint(0, 50, size=size)

premios = np.random.uniform(10000, 200000, size=size)

dados = np.column_stack((ids, idades, sexos, estados_civis, sinistros, premios))

clientesMaioresDe30 = dados[dados[:, 1] > 30]

clientesSemSinistro = dados[dados[:, 4] == 0]

clientesSemSinistroCOmPremioMaiorQue1000 =  clientesSemSinistro = clientesSemSinistro[clientesSemSinistro[:, 5] > 1000]

print(clientesSemSinistroCOmPremioMaiorQue1000.size)