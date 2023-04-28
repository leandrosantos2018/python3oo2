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


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def __getitem__(self, item):
        return self.programas[item]

    def tamanho(self):
        return len(self.programas)

    @property
    def litstagem(self):
        return self._programas


    @property
    def tamanho(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita',2018,160)

tmep = Filme('todo mndo em panico',2007,100)

demolido = Serie('demolidor',2015,2)

vingadores.dar_like()
demolido.dar_like()
demolido.dar_like()
demolido.dar_like()
demolido.dar_like()
tmep.dar_like()

atlanta = Serie('atlanta',2018,2)
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolido ,tmep]

fim_de_Semana = Playlist()

for program in fim_de_Semana:
     print(program)

