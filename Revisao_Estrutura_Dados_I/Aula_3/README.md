Estruturas de Dados Dinâmicas em Python: Referências, Nós e Filas
Repositório com a resolução prática e explicada de exercícios cobrindo manipulação de ponteiros/referências e gerenciamento de filas dinâmicas baseadas em nós.
📌 Conteúdo e Módulos do Código
Exercício 1 — Referências de Memória
Conceito: Atribuição vs. Cópia Rasa (.copy()).
Descrição: Demonstra na prática como variáveis em Python apontam para o mesmo endereço de memória (id()) e como isolar alterações criando instâncias independentes.
Exercício 2 — Construção de Cadeia de Nós
Conceito: Nó Encadeado (NodeSimples).
Descrição: Criação manual de nós sequenciais (A -> B -> C -> None) e travessia da estrutura utilizando um ponteiro auxiliar (atual).
Exercício 3 — Depuração de Loops Infinitos
Conceito: Atualização de Ponteiros.
Descrição: Identificação e correção de loops infinitos causados pela ausência da instrução de avanço atual = atual.proximo.
Exercícios 18 a 25 — Sistema de Atendimento Clínico (Fila de Prioridade)
Conceito: Lista Encadeada Dinâmica com inserção ordenada $O(N)$ / $O(1)$.
Descrição: Implementação da classe FilaAtendimento utilizando ponteiros inicio e fim. Garante que pacientes da categoria "Prioridade" furem a fila em relação aos normais, mantendo a ordem de chegada entre os próprios prioritários.
Exercícios 26 e 27 — Checklist e Reflexão Teórica
Conceito: Abstração e Gerenciamento de Memória RAM.
Descrição: Documentação explicativa e dissertativa sobre as vantagens de estruturas encadeadas frente a arrays estáticos.
