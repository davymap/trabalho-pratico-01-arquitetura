class SalaAula:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

    def mostrar_info(self):
        return f"Sala {self.numero} - Capacidade: {self.capacidade}"


class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina
        self.escolas = []

    def adicionar_escola(self, escola):
        self.escolas.append(escola)

    def mostrar_info(self):
        return f"{self.nome} - {self.disciplina}"


class Endereco:
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

    def mostrar_endereco(self):
        return f"{self.rua}, {self.numero} - {self.cidade}"


class Aluno:
    def __init__(self, nome, matricula, endereco):
        self.nome = nome
        self.matricula = matricula
        self.endereco = endereco

    def mostrar_info(self):
        return f"{self.nome} - Matrícula: {self.matricula}"


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.salas = []
        self.professores = []

    def adicionar_sala(self, numero, capacidade):
        sala = SalaAula(numero, capacidade)
        self.salas.append(sala)

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def mostrar_info(self):
        return f"Escola: {self.nome}"


escola = Escola("Escola Municipal Central")

escola.adicionar_sala(1, 30)
escola.adicionar_sala(2, 25)

professor = Professor("Carlos Silva", "Matemática")
escola.adicionar_professor(professor)
professor.adicionar_escola(escola)

endereco = Endereco("Rua Principal", 100, "Viçosa do Ceará")
aluno = Aluno("João Santos", "2026001", endereco)

print(escola.mostrar_info())

for sala in escola.salas:
    print(sala.mostrar_info())

print(professor.mostrar_info())
print(aluno.mostrar_info())
print(aluno.endereco.mostrar_endereco())