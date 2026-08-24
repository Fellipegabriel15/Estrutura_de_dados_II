Aula de Revisão — Estrutura de Dados I
Data: 21/08/2026 Tema: Arrays, Matrizes e Structs

Objetivo
Revisar conceitos relacionados à representação dos dados na memória e aplicar estruturas de dados na resolução de problemas computacionais.

Conteúdo
Arrays (Vetores)
Matrizes
Structs
Representação dos dados na memória
Arrays de Structs
Modelagem de dados
Abstração
Atividade
Implementação prática utilizando C/C++, ou a linguagem de preferência

Competências
Modelagem de dados
Abstração
Organização de informações
Escolha adequada de estruturas de dados
Implementação de soluções computacionais
1. Representação dos dados na memória
Antes de estudar as estruturas de dados, é importante compreender que as variáveis ocupam espaços na memória do computador.

Por exemplo:

int idade = 20;
float nota = 8.5;
char letra = 'A';
Podemos representar a memória de forma simplificada:

+----------+------------+
| Endereço |  Conteúdo  |
+----------+------------+
|   1000   |     20     |
|   1004   |    8.5     |
|   1008   |    'A'     |
+----------+------------+
Importante: o tamanho ocupado por cada tipo depende da linguagem, do compilador e da arquitetura utilizada.

Uma estrutura de dados é uma forma de organizar informações na memória para que elas possam ser utilizadas de maneira eficiente.

2. Arrays — Vetores
Um array é uma coleção de elementos do mesmo tipo, armazenados de maneira organizada.

Exemplo
int notas[5];
Podemos imaginar o vetor da seguinte forma:

Índice:    0    1    2    3    4
          +----+----+----+----+----+
notas:    | 7  | 8  | 6  | 9  | 10 |
          +----+----+----+----+----+
Em C/C++, o primeiro índice de um array é 0.

Inicialização
int notas[5] = {7, 8, 6, 9, 10};
Acessando elementos
Para acessar o primeiro elemento:

printf("%d", notas[0]);
Saída:

7
Para acessar o quarto elemento:

printf("%d", notas[3]);
Saída:

9
Percorrendo um array
Uma das operações mais utilizadas é percorrer todos os elementos com um laço for:

int notas[5] = {7, 8, 6, 9, 10};

for (int i = 0; i < 5; i++) {
    printf("%d\n", notas[i]);
}
Saída:

7
8
6
9
10
Exemplo: cálculo da média
int notas[5] = {7, 8, 6, 9, 10};
int soma = 0;

for (int i = 0; i < 5; i++) {
    soma += notas[i];
}

float media = soma / 5.0;

printf("Media = %.2f\n", media);
Saída:

Media = 8.00
3. Matrizes
Uma matriz é uma estrutura de dados organizada em linhas e colunas.

Exemplo de uma matriz 3 x 3:

          Colunas
             0   1   2
           +---+---+---+
Linha 0    | 1 | 2 | 3 |
           +---+---+---+
Linha 1    | 4 | 5 | 6 |
           +---+---+---+
Linha 2    | 7 | 8 | 9 |
           +---+---+---+
Em C:

int matriz[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
Acessando um elemento
Para acessar o número 5:

printf("%d", matriz[1][1]);
Saída:

5
A primeira posição representa a linha e a segunda representa a coluna:

matriz[linha][coluna]
Percorrendo uma matriz
Para percorrer uma matriz, normalmente utilizamos dois laços for:

for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        printf("%d ", matriz[i][j]);
    }

    printf("\n");
}
Saída:

1 2 3
4 5 6
7 8 9
Convenção utilizada
i → controla as linhas
j → controla as colunas
4. Structs
Enquanto um array normalmente armazena vários elementos do mesmo tipo, uma struct permite agrupar informações de tipos diferentes.

Imagine que precisamos representar um aluno:

Aluno
 ├── nome
 ├── idade
 └── nota
Podemos criar uma estrutura:

struct Aluno {
    char nome[50];
    int idade;
    float nota;
};
Agora podemos declarar uma variável desse tipo:

struct Aluno aluno1;
Atribuindo valores
strcpy(aluno1.nome, "Carlos");

aluno1.idade = 20;
aluno1.nota = 8.5;
Para acessar os dados:

printf("Nome: %s\n", aluno1.nome);
printf("Idade: %d\n", aluno1.idade);
printf("Nota: %.2f\n", aluno1.nota);
Saída:

Nome: Carlos
Idade: 20
Nota: 8.50
Para utilizar strcpy, inclua a biblioteca <string.h>.

5. Array de Structs
Uma combinação muito importante é utilizar arrays de structs.

Por exemplo, para armazenar os dados de cinco alunos:

struct Aluno {
    char nome[50];
    int idade;
    float nota;
};

struct Aluno turma[5];
Podemos imaginar:

turma
│
├── aluno 0
│   ├── nome
│   ├── idade
│   └── nota
│
├── aluno 1
│   ├── nome
│   ├── idade
│   └── nota
│
├── aluno 2
│   ├── nome
│   ├── idade
│   └── nota
│
└── ...
Podemos percorrer o array:

for (int i = 0; i < 5; i++) {
    printf("Aluno: %s\n", turma[i].nome);
    printf("Nota: %.2f\n", turma[i].nota);
}
6. Comparando as estruturas
Estrutura	Organização	Exemplo
Array	Vários dados do mesmo tipo	Notas de alunos
Matriz	Dados do mesmo tipo em linhas e colunas	Tabela de notas
Struct	Dados relacionados de tipos diferentes	Cadastro de aluno
Array de Structs	Várias entidades com diferentes atributos	Turma de alunos
Qual estrutura utilizar?
Situação 1
Precisamos armazenar 10 temperaturas.

Resposta: Array.

float temperaturas[10];
Situação 2
Precisamos representar um tabuleiro de jogo.

Resposta: Matriz.

char tabuleiro[8][8];
Situação 3
Precisamos representar um funcionário, contendo nome, idade e salário.

Resposta: Struct.

struct Funcionario {
    char nome[50];
    int idade;
    float salario;
};
Situação 4
Precisamos representar 50 funcionários.

Resposta: Array de Structs.

struct Funcionario funcionarios[50];
Essa escolha é um exercício de modelagem de dados.

7. Atividade Prática
📝 Desafio — Cadastro de Alunos
Crie um programa que:

Crie uma struct Aluno.

A struct deve possuir:

nome;
idade;
três notas.
Crie um array para armazenar cinco alunos.

Leia os dados dos cinco alunos.

Calcule a média de cada aluno.

Mostre o nome e a média de cada aluno.

Informe qual aluno possui a maior média.

Estrutura sugerida
struct Aluno {
    char nome[50];
    int idade;
    float notas[3];
};
Observe que temos uma combinação de estruturas:

Struct Aluno
│
├── nome
├── idade
└── notas
    ├── nota 0
    ├── nota 1
    └── nota 2
Nesse exemplo temos:

uma struct;
um array dentro da struct;
possibilidade de criar um array de structs.
8. Lista de Exercícios — Revisão
Exercício 1 — Soma de um vetor
Crie um programa que leia 10 números inteiros e armazene-os em um array.

Ao final, apresente:

todos os números;
a soma dos elementos;
a média dos valores.
Exercício 2 — Maior e menor
Leia 10 números inteiros utilizando um array.

Determine:

o maior valor;
o menor valor;
as posições em que eles aparecem.
Exercício 3 — Números pares
Leia 20 números inteiros e armazene-os em um array.

Depois:

mostre somente os números pares;
conte quantos números pares existem;
calcule a soma dos números pares.
Exercício 4 — Inversão de vetor
Leia 10 números e armazene-os em um array.

Mostre o vetor original e o vetor invertido.

Exemplo
Vetor original:
1 2 3 4 5 6 7 8 9 10

Vetor invertido:
10 9 8 7 6 5 4 3 2 1
Desafio: não utilize outro array para realizar a inversão.

Exercício 5 — Matriz 3 × 3
Crie uma matriz 3 x 3 de números inteiros.

O programa deverá:

ler os valores;
mostrar a matriz;
calcular a soma de todos os elementos;
mostrar o maior valor.
Exercício 6 — Diagonal principal
Leia uma matriz 4 x 4.

Mostre os elementos da diagonal principal e calcule sua soma.

Exemplo
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16
Diagonal principal:

1 6 11 16
Soma:

34
Exercício 7 — Matriz de notas
Uma turma possui 4 alunos e 3 avaliações.

Crie uma matriz para armazenar as notas:

          P1   P2   P3
Aluno 1
Aluno 2
Aluno 3
Aluno 4
Calcule e apresente a média de cada aluno.

Exercício 8 — Struct Produto
Crie uma struct Produto contendo:

nome
codigo
preco
quantidade
Cadastre cinco produtos.

Depois:

mostre todos os produtos;
calcule o valor total de cada produto;
informe o produto com maior valor em estoque.
Fórmula
valor em estoque = preço × quantidade
Exercício 9 — Struct Aluno
Crie uma struct Aluno contendo:

nome
idade
nota1
nota2
nota3
Cadastre cinco alunos.

Calcule a média de cada aluno e classifique:

Média >= 7,0 → Aprovado
Média < 7,0  → Reprovado
Ao final, informe:

quantidade de aprovados;
quantidade de reprovados;
aluno com maior média.
Exercício 10 — Sistema Integrado
Crie um pequeno sistema para cadastro de 10 funcionários.

Utilize uma struct contendo:

nome
idade
cargo
salario
O programa deverá permitir:

Cadastrar os funcionários.
Listar todos os funcionários.
Mostrar o funcionário com maior salário.
Calcular a média salarial.
Mostrar os funcionários com salário acima da média.
Desafio extra
Crie um menu:

=================================
       SISTEMA DE FUNCIONÁRIOS
=================================

1 - Cadastrar funcionários
2 - Listar funcionários
3 - Maior salário
4 - Média salarial
5 - Salários acima da média
0 - Sair

Escolha uma opção:
9. Revisão Final
Ao final da aula, responda:

1. Array
Quando temos vários dados do mesmo tipo, qual estrutura podemos utilizar?

Resposta: Array.

2. Matriz
Quando precisamos representar dados organizados em linhas e colunas, qual estrutura é adequada?

Resposta: Matriz.

3. Struct
Quando precisamos representar uma entidade com diferentes tipos de informação, qual estrutura podemos utilizar?

Resposta: Struct.

Conceito Central
Estrutura de dados é uma forma de organizar e representar informações para que um problema possa ser modelado e resolvido de maneira adequada.

A programação não consiste apenas em escrever código.

É necessário entender o problema, identificar os dados envolvidos e escolher uma representação adequada.

Isso está diretamente relacionado às competências de:

Modelagem de dados
Abstração
Organização
Representação dos dados
Resolução de problemas
Resumo
                    ESTRUTURAS DE DADOS
                           │
          ┌────────────────┼────────────────┐
          │                │                │
        ARRAY            MATRIZ           STRUCT
          │                │                │
      1 dimensão       2 dimensões      Tipos diferentes
          │                │                │
       [0..n]          [linha][coluna]   campos
          │                │                │
          └────────────────┼────────────────┘
                           │
                    MODELAGEM DE DADOS
                           │
                       ABSTRAÇÃO
Próximo passo
Utilize os 10 exercícios para praticar a implementação em C/C++, Python, Java, ou a linguagem de sua preferência.

A recomendação é tentar resolver cada problema sem consultar a solução inicialmente, identificando primeiro:

Quais são os dados?
Como esses dados devem ser representados?
Qual estrutura de dados é mais adequada?
Quais operações serão realizadas?
Como implementar a solução?
