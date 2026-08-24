"""
==============================================================================
ESTRUTURAS DE DADOS EM PYTHON: NÓS, LISTAS ENCADEADAS E FILAS
==============================================================================
Este arquivo contém a resolução completa, comentada e executável de todas
as atividades e exercícios propostos.
"""

# ============================================================================
# EXERCÍCIO 1 — Referências
# ============================================================================

def exercicio_1():
    """
    EXERCÍCIO 1 — REFERÊNCIAS
    
    Perguntas e Respostas:
    -----------------------
    1. Qual será a saída?
       - a: [10, 20, 30, 40]
       - b: [10, 20, 30, 40]
       - id(a): <endereço de memória X>
       - id(b): <endereço de memória X> (exatamente igual ao id de a)

    2. a e b representam o mesmo objeto?
       - SIM. Ambas as variáveis apontam para a mesma região de memória.

    3. Por quê?
       - Em Python, a atribuição `b = a` não cria uma cópia da lista. Ela apenas
         cria um novo apelido (referência) para o mesmo objeto já existente.

    4. O que aconteceria com b = a.copy()?
       - Seria alocada uma NOVA área de memória com uma cópia rasa dos elementos.
         As alterações em `b` não afetariam `a`, e `id(a)` seria diferente de `id(b)`.
    """
    print("=" * 60)
    print("EXERCÍCIO 1 — DEMONSTRAÇÃO DE REFERÊNCIAS")
    print("=" * 60)
    
    a = [10, 20, 30]
    b = a
    b.append(40)
    
    print("a:", a)
    print("b:", b)
    print("id(a):", id(a))
    print("id(b):", id(b))
    print("a e b são o mesmo objeto em memória?", id(a) == id(b))
    
    # Demonstração do comportamento com .copy()
    c = a.copy()
    c.append(50)
    print("
--- Teste com .copy() ---")
    print("a (inalterado):", a)
    print("c (com novo elemento):", c)
    print("id(a) == id(c)?", id(a) == id(c))
    print()


# ============================================================================
# EXERCÍCIO 2 — Construindo uma cadeia
# ============================================================================

class NodeSimples:
    """Estrutura básica de um Nó para listas encadeadas."""
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


def exercicio_2():
    """
    EXERCÍCIO 2 — CONSTRUINDO UMA CADEIA
    
    Objetivo: Criar nós "A", "B", "C", encadeá-los (A -> B -> C -> None)
    e percorrer a estrutura imprimindo os valores.
    """
    print("=" * 60)
    print("EXERCÍCIO 2 — CADEIA DE NÓS (A -> B -> C)")
    print("=" * 60)
    
    # Criando os nós
    n1 = NodeSimples("A")
    n2 = NodeSimples("B")
    n3 = NodeSimples("C")

    # Conectando a cadeia: A -> B -> C -> None
    n1.proximo = n2
    n2.proximo = n3

    # Percorrendo a estrutura
    atual = n1
    while atual is not None:
        print(atual.valor)
        atual = atual.proximo
    print()


# ============================================================================
# EXERCÍCIO 3 — Depuração
# ============================================================================

def exercicio_3():
    """
    EXERCÍCIO 3 — DEPURAÇÃO
    
    Perguntas e Respostas:
    -----------------------
    1. Qual é o problema?
       - Falta atualizar a variável de controle (`atual`) dentro do laço `while`.

    2. Por que o programa não termina?
       - A variável `atual` fica presa no nó `n1`. A condição `atual is not None`
         permanece verdadeira infinitamente, imprimindo `10` em um loop infinito.

    3. Qual linha deve ser acrescentada?
       - `atual = atual.proximo` (dentro do bloco do `while`).

    4. Qual será a saída depois da correção?
       - 10
       - 20
       - 30
    """
    print("=" * 60)
    print("EXERCÍCIO 3 — CÓDIGO CORRIGIDO (DEPURAÇÃO)")
    print("=" * 60)
    
    n1 = NodeSimples(10)
    n2 = NodeSimples(20)
    n3 = NodeSimples(30)

    n1.proximo = n2
    n2.proximo = n3

    atual = n1
    while atual is not None:
        print(atual.valor)
        atual = atual.proximo  # LINHA CORRIGIDA: Avança o ponteiro
    print()


# ============================================================================
# EXERCÍCIOS 18 A 25 — SISTEMA DE ATENDIMENTO DE UMA CLÍNICA
# ============================================================================

class Paciente:
    """Modelagem do Paciente para o sistema da clínica."""
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade  # "Normal" ou "Prioridade"

    def __repr__(self):
        return f"{self.nome} ({self.idade} anos) [{self.prioridade}]"


class NodePaciente:
    """Nó que armazena um Paciente e o ponteiro para o próximo nó."""
    def __init__(self, paciente):
        self.paciente = paciente
        self.proximo = None


class FilaAtendimento:
    """
    Fila de Atendimento baseada em Lista Encadeada com Suporte a Prioridade.
    
    Representação:
    inicio                         fim
      ↓                             ↓
    Ana  →  Bruno  →  Carlos  →  None
    """
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return self.inicio is None

    def tamanho(self):
        """Retorna a quantidade de pacientes na fila."""
        return self._tamanho

    def adicionar(self, paciente):
        """
        Adiciona um paciente à fila.
        Desafio 23: Pacientes com prioridade entram antes dos normais,
        mantendo a ordem de chegada entre os prioritários.
        """
        novo_no = NodePaciente(paciente)
        self._tamanho += 1

        # Caso 1: Fila Vazia
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
            return

        # Caso 2: Inserção de Paciente PRIORITÁRIO
        if paciente.prioridade == "Prioridade":
            # Subcaso 2.1: Se até o primeiro da fila for Normal, o prioritário fura a fila no início
            if self.inicio.paciente.prioridade == "Normal":
                novo_no.proximo = self.inicio
                self.inicio = novo_no
            else:
                # Subcaso 2.2: Avança até encontrar o ÚLTIMO paciente que é Prioridade
                atual = self.inicio
                while atual.proximo and atual.proximo.paciente.prioridade == "Prioridade":
                    atual = atual.proximo
                
                # Insere o novo nó logo após o último prioritário encontrado
                novo_no.proximo = atual.proximo
                atual.proximo = novo_no
                
                # Se foi inserido no final de tudo, atualiza o ponteiro 'fim'
                if novo_no.proximo is None:
                    self.fim = novo_no
        else:
            # Caso 3: Paciente NORMAL vai sempre para o final da fila
            self.fim.proximo = novo_no
            self.fim = novo_no

    def atender(self):
        """Remove e retorna o primeiro paciente da fila (FIFO)."""
        if self.esta_vazia():
            print("Nenhum paciente na fila para atender.")
            return None

        paciente_atendido = self.inicio.paciente
        self.inicio = self.inicio.proximo
        self._tamanho -= 1

        # Se a fila esvaziou completamente
        if self.inicio is None:
            self.fim = None

        return paciente_atendido

    def listar(self):
        """Exibe todos os pacientes da fila em ordem."""
        if self.esta_vazia():
            print("Fila vazia.")
            return

        atual = self.inicio
        posicao = 1
        while atual:
            print(f"  {posicao}. {atual.paciente}")
            atual = atual.proximo
            posicao += 1


def exercicio_clinica():
    """Demonstração prática e testes do Sistema de Atendimento da Clínica."""
    print("=" * 60)
    print("EXERCÍCIOS 18–25 — SISTEMA DE ATENDIMENTO DA CLÍNICA")
    print("=" * 60)
    
    fila = FilaAtendimento()

    # Adicionando pacientes de teste
    print("Adicionando pacientes:")
    print("- Ana (Normal)")
    print("- Bruno (Normal)")
    print("- Carlos (Prioridade)")
    print("- Daniela (Normal)")
    print("- Eduardo (Prioridade)
")

    fila.adicionar(Paciente("Ana", 32, "Normal"))
    fila.adicionar(Paciente("Bruno", 70, "Normal"))
    fila.adicionar(Paciente("Carlos", 45, "Prioridade"))  # Deve ir para antes da Ana
    fila.adicionar(Paciente("Daniela", 28, "Normal"))
    fila.adicionar(Paciente("Eduardo", 68, "Prioridade")) # Deve ir para depois do Carlos e antes da Ana

    print("--- Fila Organizada por Prioridade ---")
    fila.listar()
    print(f"Total na fila: {fila.tamanho()} pacientes
")

    print("--- Atendimento dos Pacientes ---")
    p1 = fila.atender()
    print("Atendendo 1º paciente:", p1)
    p2 = fila.atender()
    print("Atendendo 2º paciente:", p2)
    print()

    print("--- Fila Restante ---")
    fila.listar()
    print(f"Total restante: {fila.tamanho()} pacientes
")


# ============================================================================
# EXERCÍCIOS 26 E 27 — CHECKLIST DE APRENDIZAGEM E REFLEXÃO FINAL
# ============================================================================

def reflexao_final():
    """
    EXERCÍCIO 27 — REFLEXÃO FINAL (RESPOSTAS DISSERTATIVAS)
    --------------------------------------------------------------------------
    1. O que é uma referência em Python?
       R: Uma referência é um valor numérico interno (endereço de memória) que
          indica onde um determinado objeto está armazenado na memória RAM.
          Variáveis em Python funcionam como ponteiros/etiquetas para esses objetos.

    2. Qual a diferença entre b = a e b = a.copy()?
       R: `b = a` apenas cria um segundo ponteiro (apelido) apontando para a
          MESMA estrutura na memória. Alterações em `b` afetam `a`.
          `b = a.copy()` reserva uma NOVA região de memória e copia os elementos,
          gerando duas coleções totalmente independentes.

    3. Por que uma estrutura encadeada precisa de referências?
       R: Porque os nós de uma lista encadeada não ficam em posições contíguas
          (sequenciais) da memória RAM, ao contrário de vetores/arrays.
          A única maneira de conectar os elementos e navegar entre eles é
          armazenando no nó atual o endereço (referência) do próximo nó.

    4. Qual erro você encontrou durante a depuração?
       R: O erro de loop infinito no Exercício 3, causado por esquecer de
          atualizar o ponteiro de navegação (`atual = atual.proximo`) no laço.

    5. Como referências ajudam a compreender estruturas dinâmicas?
       R: Elas mostram como é possível construir coleções de dados flexíveis que
          crescem ou diminuem sem limite pré-definido, ajustando ponteiros em
          tempo constante O(1) sem necessidade de realocar toda a memória.
    """
    print("=" * 60)
    print("EXERCÍCIO 27 — RESUMO DAS REFLEXÕES")
    print("=" * 60)
    print(reflexao_final.__doc__)


# ============================================================================
# BLOCO PRINCIPAL DE EXECUÇÃO
# ============================================================================

if __name__ == "__main__":
    exercicio_1()
    exercicio_2()
    exercicio_3()
    exercicio_clinica()
    reflexao_final()
