%{
	#include <stdio.h>
	#include <stdlib.h>
	#include "ansiC.tab.h"

%}
letra [a-zA-Z_]
DIGITO [0-9]

%%


"char"|"int"|"long"|"short"|"float"|"double"|"void"   {yylval.valor = strdup(yytext); return(TIPODATO);}
([a-zA-Z]|"_")([a-zA-Z0-9]|"_")*                      {yylval.valor = strdup(yytext); return(VARIABLE);}
"<"|">"|">="|"<="|"!="|"=="                           {yylval.valor = strdup(yytext); return(OPRELACIONAL);}
"+"|"-"|"*"|"/"                                       {yylval.valor = strdup(yytext); return(OPARITMETICO);}
"++"|"--"                                             {yylval.valor = strdup(yytext); return(OPINCREMENTO);}
 "&&"|"||"                                            {yylval.valor = strdup(yytext); return(OPLOGICO);}

"else"|"switch"|"case"|"for"|"while"|"do"|"if"|"return"|"break"  {yylval.valor = strdup(yytext); return(C_CICLOS);}

";"                     {yylval.valor = strdup(yytext); return(PT_COM);}
","		              	{yylval.valor = strdup(yytext); return(COMA);}
":"			            {yylval.valor = strdup(yytext); return(2PTO);}
"="                     {yylval.valor = strdup(yytext); return(IGUAL);}
"("                     {yylval.valor = strdup(yytext); return(PA_A);}
")"                     {yylval.valor = strdup(yytext); return(PA_C);}
"{"                     {yylval.valor = strdup(yytext); return(CO_A);}
"}"                     {yylval.valor = strdup(yytext); return(CO_C);}
%%