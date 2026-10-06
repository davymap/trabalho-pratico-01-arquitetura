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
    def __init__(self, nome, matricula, rua, numero, cidade):
        self.nome = nome
        self.matricula = matricula
        # composição: o endereço é criado junto com o aluno
        self.endereco = Endereco(rua, numero, cidade)

    def mostrar_info(self):
        return f"{self.nome} - Matrícula: {self.matricula}"

    def remover(self):
        # o endereço não some junto com o aluno, ele é devolvido
        # para poder ser usado em outro lugar (ex: relatórios)
        endereco = self.endereco
        self.endereco = None
        return endereco


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.salas = []
        self.professores = []

    def adicionar_sala(self, numero, capacidade):
        # composição: a própria escola cria a sala
        sala = SalaAula(numero, capacidade)
        self.salas.append(sala)

    def adicionar_professor(self, professor):
        # agregação: o professor já existe, a escola só recebe ele
        if professor not in self.professores:
            self.professores.append(professor)
            professor.adicionar_escola(self)

    def fechar(self):
        # as salas deixam de existir, mas os professores continuam
        self.salas.clear()
        for professor in self.professores:
            professor.escolas.remove(self)
        self.professores.clear()
        print(f"A escola {self.nome} fechou.")

    def mostrar_info(self):
        return f"Escola: {self.nome}"


# ---------- teste ----------
escola = Escola("Escola Municipal Central")

escola.adicionar_sala(1, 30)
escola.adicionar_sala(2, 25)

professor = Professor("Carlos Silva", "Matemática")
escola.adicionar_professor(professor)

aluno = Aluno("João Santos", "2026001", "Rua Principal", 100, "Viçosa do Ceará")

print(escola.mostrar_info())

for sala in escola.salas:
    print(sala.mostrar_info())

print(professor.mostrar_info())
print(aluno.mostrar_info())
print(aluno.endereco.mostrar_endereco())

print()
escola.fechar()
print("Salas depois de fechar:", len(escola.salas))
print("Professor continua existindo:", professor.mostrar_info())
print("Escolas do professor:", len(professor.escolas))

print()
endereco_sobrando = aluno.remover()
print("Endereço que sobrou:", endereco_sobrando.mostrar_endereco())