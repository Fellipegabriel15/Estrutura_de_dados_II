# Material do Estudante - Prática de Grafos

**Disciplina:** Estrutura de Dados II\
**Unidade III:** Grafos\
**Professora:** Kadidja Valéria\
**Conteúdo-base:** Capítulo 1 - Conceitos Fundamentais\
**Duração prevista:** atividades distribuídas ao longo da aula de 2
horas

------------------------------------------------------------------------

## 1. Objetivos da prática

Ao final das atividades, você deverá ser capaz de:

-   representar problemas utilizando grafos;
-   identificar vértices e arestas;
-   reconhecer incidência e adjacência;
-   diferenciar grafos não dirigidos e grafos dirigidos;
-   determinar ordem, tamanho e grau de vértices;
-   reconhecer laços e arestas paralelas;
-   analisar isomorfismo e subgrafos;
-   construir e conferir sequências de graus;
-   utilizar ferramentas digitais para representar grafos.

------------------------------------------------------------------------

## 2. Orientações gerais

1.  Leia o enunciado antes de iniciar o desenho.
2.  Quando solicitado, registre primeiro os conjuntos de vértices `V` e
    de arestas `E`.
3.  Utilize círculos ou pontos para representar vértices e linhas/setas
    para representar arestas.
4.  Em grafos dirigidos, a seta deve indicar claramente a origem e o
    destino.
5.  Não entregue somente o desenho: apresente também as respostas e
    justificativas solicitadas.
6.  Quando utilizar uma plataforma digital, registre uma captura de tela
    ou o link da atividade.

------------------------------------------------------------------------

## 3. Atividade 1 - Desenhando um grafo

### Proposta

Considere:

`V = {1, 2, 3, 4, 5}`

`E = {(1,2), (1,4), (1,5), (2,3), (3,4), (4,4)}`

### Faça

1.  Desenhe o grafo.
2.  Identifique o número de vértices = 5
3.  Identifique o número de arestas = 6
4.  Determine a ordem, `|5|`.
5.  Determine o tamanho, `|6|`.
6.  Identifique se existe laço = Sim, no 4
7.  Determine o grau de cada vértice:
   Vertice 1 = 3 
   Vertice 2 = 2
   Vertice 3 = 2
   Vertice 4 = 4
   Vertice 5 = 1

<img width="532" height="492" alt="Diagrama_final" src="https://github.com/user-attachments/assets/3fa85a5e-273c-4331-a382-fa178ab9789a" />


------------------------------------------------------------------------

## 4. Atividade 2 - Incidência e adjacência

Utilize o grafo construído na Atividade 1.

### Faça

1.  Liste os vértices adjacentes a cada vértice. Consta no Registro abaixo.
2.  Informe quais arestas são incidentes em cada vértice. Consta no Registro abaixo.
3.  Escolha dois vértices adjacentes e explique por que são considerados
    vizinhos = O 1 e o 4 são vizinhos ou adjacentes pois possui uma aresta entre eles e que liga eles.
4.  Escolha dois vértices não adjacentes e justifique sua resposta = O 2 e o 5 são Incidentes e não adjacentes, pois, podemos chegar até o 5 partindo do 2 e vice e versa, porém não existe uma aresta que ligue os dois entre si, portanto, Não são adjacentes.

### Registro

  
  Vértices adjacentes
  --------------------------------------------------
  1 = (5, 2 e 4)
  
  2 = (1, 3)
  
  3 = (2, 4) 
  
  4 = (1, 3, 4) 
  
  5 = (1)
  
  
  Arestas incidentes
  --------------------------------------------------
  1 = (2, 3, 4, 5)   
  
  2 = (1, 3, 4, 5) 
  
  3 = (1, 2, 4, 5)   
  
  4 = (1, 2, 3, 4, 5) 
  
  5 = (1, 2, 3, 4)  
  

------------------------------------------------------------------------

## 5. Atividade 3 - Modelagem de uma rede de amizades

Considere quatro pessoas:

**João, Carolina, Maria e Marco.**

### Situação

Crie uma pequena rede de amizades entre essas pessoas.

### Faça

1.  Defina o conjunto de vértices `4`.
2.  Defina o conjunto de arestas `4`.
3.  Desenhe o grafo correspondente. (Consta abaixo) 
4.  Informe se o grafo deve ser dirigido ou não dirigido. O grafo deve ser não dirigido.
5.  Justifique a escolha = Escolhi o grafo não dirigido, pois as conexões são mutuas, logo se conheço uma pessoa, ela também me conhece, uma mão dupla.
6.  Identifique quem possui maior grau no grafo criado = João possui o maior grafo, pois tem conexão com todos os outros.

### Questão para reflexão

**O que os vértices e as arestas representam nesse problema?**
- Os vértices nesse problema representam as pessoas e as arestas a relação que elas possuem entre si.

### Diagrama

<img width="622" height="622" alt="Diagrama sem nome" src="https://github.com/user-attachments/assets/c2f7d76f-22f9-469e-b060-5c34fdc314fe" />

------------------------------------------------------------------------

## 6. Atividade 4 - Modelagem de ruas de mão única

### Situação

Considere um pequeno sistema urbano formado por cruzamentos e ruas de
mão única.

### Faça

1.  Represente cada cruzamento ou ponto relevante por um vértice.
2.  Represente cada rua por uma aresta dirigida.
3.  Utilize setas para indicar o sentido permitido.
4.  Defina os conjuntos `V` e `E`.
5.  Escolha um vértice e determine (Vertice 5):
    -   seu grau de entrada = Grau 2;
    -   seu grau de saída = Grau 1.
6.  Explique por que um grafo não dirigido não representa adequadamente
    essa situação = Pois, existem regras que devem ser seguidas quanto a direção, portanto, se faz necessária a direção, deixar ambíguo a decrição, compromete o gráfico como um todo.

### Diagrama

<img width="601" height="572" alt="Diagrama sem nome (1)" src="https://github.com/user-attachments/assets/3744b6eb-b686-4c5a-b754-a3579619b01b" />


------------------------------------------------------------------------

## 7. Atividade 5 - Desafio de isomorfismo

A professora apresentará dois grafos para comparação.

### Faça

1.  Compare a quantidade de vértices = Ambos possuem 4 vértices.
2.  Compare a quantidade de arestas = Ambos possuem 4 arestas
3.  Observe os graus dos vértices = Cada Vértice possui exatamente 2 graus em cada Grafo
4.  Procure uma correspondência entre os vértices dos dois grafos:  1 = a, 2 = c, 3 = b e 4 = d.

Podemos considerar que os grafos são isomórficos, pois possuem a mesma quantidade de arestas e vértices (4), além das adjacência serem preservadas de forma igual entre os dois (2), tendo em vista o mapeamento, as comparações e as evidencias apresentadas, podemos concluir que ambos os grafos são isomorficos.

### Grafo

<img width="992" height="432" alt="Grafos-Página-3" src="https://github.com/user-attachments/assets/51056dd9-7581-468e-9d16-410401f4151e" />


------------------------------------------------------------------------

## 8. Atividade 6 - Construindo subgrafos

A partir do grafo `G` indicado pela professora, construa **dois
subgrafos diferentes**.

### Para cada subgrafo

1.  informe o conjunto de vértices;
2.  informe o conjunto de arestas;
3.  desenhe o subgrafo;
4.  confirme que seus vértices e arestas pertencem ao grafo original.

### Registro

**Subgrafo G1**

`V1 = { 1, 4, 3 }`

`E1 = { (4,1) e (3,4) }`

**Subgrafo G2**

`V2 = { 4, 3, 2 }`

`E2 = { (2,3) e (3,4) }`

### Grafo

<img width="992" height="432" alt="Grafos-Página-3 (1)" src="https://github.com/user-attachments/assets/386e63b9-4ace-4c17-84d1-cae10712e6be" />

------------------------------------------------------------------------

## 9. Atividade 7 - Desafio da sequência de graus

Construa um **grafo simples** de acordo com a sequência de graus
indicada pela professora.

### Grafo

<img width="682" height="862" alt="Grafos-Página-2" src="https://github.com/user-attachments/assets/ce670b5f-9365-4a6b-b87e-553dafc28591" />


### Registro

  |  Vértice   |  Grau  |      Vizinho       |
  | ------------ | ------------ | ------------ |
  |     A      |    1   |  H                 |
  |     B      |    1   |  H                 |
  |     C      |    2   |  G, H              |
  |     D      |    3   |  E, F, H           |
  |     E      |    3   |  D, F, G           |
  |     F      |    4   |  D, E, G, H        |
  |     G      |    4   |  C, E, F, H        |
  |     H      |    6   |  A, B, C, D, F, G  |


| Vértice | Grau | Vizinho |
| - | - | - |
| A | 1 | H |
| B | 1 | H |
| C | 2 | G, H |
| D | 3 | E, F, H |
| E | 3 | D, F, G |
| F | 4 | D, E, G, H |
| G | 4 | C, E, F, H |
| H | 6 | A, B, C, D, F, G |

**Sequência final de graus:** `( 1, 1, 2, 3, 3, 4, 4, 6)`

------------------------------------------------------------------------

## 10. Plataforma Utilizada:

- https://app.diagrams.net/

------------------------------------------------------------------------


## 11. Checklist de revisão

-   [X] Identifiquei corretamente vértices e arestas.
-   [X] Diferenciei grafo dirigido e não dirigido.
-   [X] Identifiquei incidência e adjacência.
-   [X] Calculei os graus quando solicitado.
-   [X] Considerei o laço corretamente no cálculo do grau.
-   [X] Utilizei setas nos grafos dirigidos.
-   [X] Justifiquei a análise de isomorfismo.
-   [X] Identifiquei corretamente os subgrafos.
-   [X] Conferi a sequência de graus.
-   [X] Revisei os desenhos e as justificativas.
-   [X] Registrei a plataforma utilizada.

------------------------------------------------------------------------
