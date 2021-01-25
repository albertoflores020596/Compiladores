%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
extern int yylex(void);
extern char *yytext;
extern int lineas;
extern FILE * yyin;

void yyerror(char *mensaje){
    printf(" ERROR:%s\n",mensaje);
    exit(0);
	}
%}

%union
{
	char *valor;
}

%token <valor> TIPODATO VARIABLE OPRELACIONAL OPARITMETICO OPINCREMENTO OPLOGICO C_CICLOS PT_COM COMA 2PTO IGUAL PA_A PA_C CO_A CO_C DIGITO
%type <valor> argumentos
%type <valor> declaracion
%type <valor> id
%type <valor> conte
%type <valor> return
%type <valor> asignacion
%type <valor> valores
%type <valor> constantes
%start funciones
%%

funciones :	funciones funcion|
		funcion;

funcion :	TIPOSDATO ID PA_A argumentos PA_C CO_A conte CO_C  
		

argumentos:	TIPODATO ID    

conte:	elementos conte	{$$=$2;}|
	return	{$$=$1;}|{$$="";};

elementos:	declaracion|operacion|estructuras;


declaracion:	TIPODATO id PT_COM		
		TIPODATO id PT_COM declaracion	

id: VARIABLE{$$=$1;}|
	VARIABLE PT_COM id	

operaciones:	asignacion 	{}|
		operArit PT_COM	{}|
		operacion asignacion PT_COM {}|
		operacion operArit PT_COM	 {};

asignacion:	TIPODATO IGUAL  ID	

operArit:VARIABLE OPARITMETICO VARIABLE			|
		VARIABLE IGUAL  VARIABLE  	|
		VARIABLE OPINCREMENTO				


return:		C_CICLOS  VARIABLE	PT_COM		
		C_CICLOS  PA_A VARIABLE PA_C PT_COM	
		
ciclos:	 estructuraAlgoritmo
         | estructurasCiclo	                


estructuraAlgoritmo:	Ewhile|Eif;



Ewhile:		C_CICLOS PA_A valores OPRELACIONAL valores PA_C CO_C contEstructura CO_C
	

Eif:		C_CICLOS PA_A valores OPRELACIONAL valores PA_C CO_A contEstructura CO_C



valores:	TIPODATO{$$=$1;}|
		

contEstructura:	operacion|ciclo;

%%