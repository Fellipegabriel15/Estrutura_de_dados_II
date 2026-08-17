#include <stdio.h>
/* Escreva um algoritmo que solicite Nome, Sexo, idade e três notas de N alunos em uma turma e ao final apresente:
   	1) Total de Alunos cadastrados........................................ ok
   	2) A media das idades dos alunos da turma............................. ok
   	3) Quantidade de alunos aprovados..................................... ok
	3.1) Quantidade reprovados.............................................. ok
   	4) Percentual de aprovacao por sexo (Masculinos e Femininos) ......... 
	5) Relatorio de alunos aprovados e reprovados 
	6) Permitir ao usuario configurar Quantidade de provas e Media aprovacao
	*/
// A seguir estamos definindo uma ESTRUTURA de dados na memoria
struct Aluno {
	char Nome[30];
	char Sexo;
	int Idade;
	float Notas[10];
	float Media;
	bool Aprovado;
};

// A seguir temos a FUNCAO principal do programa
int main () {
  int QtdAlunos, QtdProvas, QtdAprovados=0, AprovadosM=0, ReprovadosM=0; // Variavel que controlara o total de alunos da turma
	float soma, MedAprovacao, somaIdades=0, somaIdadesF=0;
	struct Aluno Alunos[100]; // Estamos declarando um vetor chamado Alunos, com cem posicoes do tipo struct de Aluno
	
	printf(" Informe a quantidade de alunos da turma: ");
	scanf("%i", &QtdAlunos);
	printf(" Informe quantas provas: ");
	scanf("%i", &QtdProvas);
	printf(" Informe a media de aprovacao? ");
	scanf("%f", &MedAprovacao);

	// Vamos percorrer os N alunos para solicitar seus dados.
	for (int i=1; i<=QtdAlunos; i++) {
		printf(" Informe o nome do %i. aluno: ", i);
		scanf("%s", &Alunos[i].Nome);
		
		printf(" Informe a idade de %s: ", Alunos[i].Nome);
		scanf("%i", &Alunos[i].Idade);
		somaIdades = somaIdades + Alunos[i].Idade;
		
		printf(" Informe o sexo de %s [M/F]: ", Alunos[i].Nome);
		scanf("%s", &Alunos[i].Sexo);
		if (Alunos[i].Sexo == 'F' or Alunos[i].Sexo == 'f')
		  somaIdadesF = somaIdadesF+1;
		  
		soma = 0;
		for (int n=1; n<=QtdProvas; n++) {   
		  printf("   Informe a %i nota: ", n);
		  scanf("%f", &Alunos[i].Notas[n]);
		  soma = soma + Alunos[i].Notas[n];
		}
    // Calculo da aprovacao/reprovacao do aluno
    Alunos[i].Media = soma / QtdProvas;
		if (Alunos[i].Media >= MedAprovacao) { 
      Alunos[i].Aprovado = true;
      QtdAprovados = QtdAprovados + 1;
			if (Alunos[i].Sexo == 'M' or Alunos[i].Sexo == 'm')
				AprovadosM = AprovadosM + 1;
	    }
    else {
      Alunos[i].Aprovado = false;
			if (Alunos[i].Sexo == 'M' || Alunos[i].Sexo == 'm')
				ReprovadosM = ReprovadosM + 1;
    }
	}

	printf("\n Total de Alunos cadastrados: %i", QtdAlunos ); //01 mostra a quantidade de alunos
	float mediaIdade = somaIdades / QtdAlunos; // faz o calculo da media de idade dos alunoos e imprime o valor na linha abaixo 02
	printf("\n A media de idade dos alunos da turma é de %.2f\n", mediaIdade);
	
	printf("\n Alunos aprovados: %i", QtdAprovados);  // 03 imprime a quantidade de alunoos aprovados atraves de uma variavel que adciona um valor por aluno aprovado atraves do loop na linha 62
	printf("\n Alunos reprovados: %i", QtdAlunos-QtdAprovados);  
	

}

