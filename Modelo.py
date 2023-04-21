class Programa:

    def __init__(self,nome,ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes +=1
    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome.title()

    def imprime(self):
        print(f'{self._nome}  - {self.ano} - {self._likes} ')


class Filme(Programa):
    def __init__(self,nome , ano, duracao,):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
      return f'{self._nome}  - {self.ano} - {self.duracao} min - {self._likes} '



class Serie(Programa):
    def __init__(self,nome , ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return  f'{self._nome}  - {self.ano} - {self.temporadas} temporadas - {self._likes} '



vingadores = Filme('vigadores',2023,100)

atalanta = Serie('atlanta',2023,10)

vingadores.dar_like()
#print(f' Nome : {vingadores.nome}  - Ano: {vingadores.ano} - Duração : {vingadores.duracao} - likes {vingadores.likes}')

filmes_e_series = [vingadores,atalanta]

for lits in filmes_e_series:
    print(lits)