#include "ansiC.tab.h"
#include <stdlib.h>
#include <stdio.h>

extern char *yytext;
extern int  yyleng;
extern int yyparse();
extern FILE *yyin;
FILE *fich;
int main(int argc, char *argv[]) {
	FILE *fich = fopen(argv[1],"r");
	if (fich == 0) {
		printf("No se puede abrir %s\n",argv[1]);
		exit(1);
	}
	yyin = fich;
	yyparse();
	fclose(fich);
}
