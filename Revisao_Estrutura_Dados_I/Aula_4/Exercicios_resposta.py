#----------------------------Exercicio 1----------------------------


class EditorDeTexto:
    def __init__(self):
        self.pilha_acoes = []  # Armazena as ações (LIFO)

    def executar_acao(self, acao):
        """Adiciona uma nova ação à pilha."""
        self.pilha_acoes.append(acao)
        print(f"Ação realizada: '{acao}'")

    def desfazer(self):
        """Remove e reverte o último comando inserido."""
        if self.pilha_acoes:
            ultima_acao = self.pilha_acoes.pop()
            print(f"Desfazendo ação: '{ultima_acao}'")
        else:
            print("Nenhuma ação para desfazer.")

# --- Teste do Exercício 1 ---
editor = EditorDeTexto()
editor.executar_acao("digitar 'Olá'")
editor.executar_acao("apagar 'a'")
editor.executar_acao("substituir 'Ol' por 'Oi'")

print("\n--- Testando o Desfazer ---")
print(editor.pilha_acoes)
editor.desfazer()  # Reverte a substituição
print(editor.pilha_acoes)
editor.desfazer()  # Reverte o apagar 


#----------------------------Exercicio 2----------------------------

from collections import deque

class SpoolerImpressora:
    def __init__(self):
        self.fila_impressao = deque()  # Armazena os documentos (FIFO)

    def adicionar_documento(self, documento):
        """Enfileira um novo documento."""
        self.fila_impressao.append(documento)
        print(f"Documento '{documento}' adicionado à fila.")

    def imprimir(self):
        """Imprime o documento mais antigo da fila."""
        if self.fila_impressao:
            doc_impresso = self.fila_impressao.popleft()
            print(f"Imprimindo: '{doc_impresso}'")
        else:
            print("Nenhum documento na fila para imprimir.")

# --- Teste do Exercício 2 ---
impressora = SpoolerImpressora()
impressora.adicionar_documento("Relatorio.pdf")
impressora.adicionar_documento("Trabalho_Escolar.docx")
impressora.adicionar_documento("Boleto.pdf")

print("\n--- Testando a Impressão ---")
impressora.imprimir()  # Imprime 'Relatorio.pdf' (o mais antigo)
impressora.imprimir()  # Imprime 'Trabalho_Escolar.docx'
