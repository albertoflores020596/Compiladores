%{ /* definiciones de lenguaje C */
  #include<stdio.h>

%}
D		    	[0-9]
L			    [a-zA-Z_]
H			    [a-fA-F0-9]
E			    [Ee][+-]?{D}+
FS			  (f|F|l|L)
IS			  (u|U|l|L)*


%%
"/*"		   	{ printf("<Comentario>"); }

"auto"			{ printf("<palabra reservada>"); }
"break"			{ printf("<palabra reservada>"); }
"case"			{ printf("<palabra reservada>"); }
"char"			{ printf("<palabra reservada>"); }
"const"			{ printf("<palabra reservada>"); }
"continue"	{ printf("<palabra reservada>"); }
"default"		{ printf("<palabra reservada>"); }
"do"			  { printf("<palabra reservada>"); }
"double"		{ printf("<palabra reservada>"); }
"else"			{ printf("<palabra reservada>"); }
"enum"			{ printf("<palabra reservada>"); }
"extern"		{ printf("<palabra reservada>"); }
"float"			{ printf("<palabra reservada>"); }
"for"			  { printf("<palabra reservada>"); }
"goto"			{ printf("<palabra reservada>"); }
"if"			  { printf("<palabra reservada>"); }
"int"			  { printf("<palabra reservada>"); }
"long"			{ printf("<palabra reservada>"); }
"register"	{ printf("<palabra reservada>"); }
"return"		{ printf("<palabra reservada>"); }
"short"			{ printf("<palabra reservada>"); }
"signed"		{ printf("<palabra reservada>"); }
"sizeof"		{ printf("<palabra reservada>"); }
"static"		{ printf("<palabra reservada>"); }
"struct"		{ printf("<palabra reservada>"); }
"switch"		{ printf("<palabra reservada>"); }
"typedef"		{ printf("<palabra reservada>"); }
"union"			{ printf("<palabra reservada>"); }
"unsigned"	{ printf("<palabra reservada>"); }
"void"			{ printf("<palabra reservada>"); }
"volatile"	{ printf("<palabra reservada>"); }
"while"			{ printf("<palabra reservada>"); }

{L}({L}|{D})*		        { printf("<Variable>"); }

0[xX]{H}+{IS}?		      { printf("<Cte>"); }
0{D}+{IS}?	    	      { printf("<Cte>"); }
{D}+{IS}?		            { printf("<Cte>"); }
L?'(\\.|[^\\'])+'	      { printf("<Cte>"); }

{D}+{E}{FS}?		        { printf("<Cte entera>"); }
{D}*"."{D}+({E})?{FS}?	{ printf("<Cte flotante>"); }
{D}+"."{D}*({E})?{FS}?	{ printf("<Cte long>"); }

L?\"(\\.|[^\\"])*\"	    { printf("<Cadena>"); }

"..."		  { printf("<Operador Asignación>"); }
">>="			{ printf("<Operador Asignación>"); }
"<<="	  	{ printf("<Operador Asignación>"); }
"+="			{ printf("<Operador Asignación>"); }
"-="			{ printf("<Operador Asignación>"); }
"*="			{ printf("<Operador Asignación>"); }
"/="			{ printf("<Operador Asignación>"); }
"%="			{ printf("<Operador Asignación>"); }
"&="			{ printf("<Operador Lógico>"); }
"^="			{ printf("<Operador Lógico>"); }
"|="			{ printf("<Operador Lógico>"); }
">>"			{ printf("<Operador Relacional>"); }
"<<"			{ printf("<Operador Relacional>"); }
"++"			{ printf("<Operador Asignación>"); }
"--"			{ printf("<Operador Asignación>"); }
"->"			{ printf("<Operador Asignación>"); }
"&&"			{ printf("<Operador Lógico>"); }
"||"			{ printf("<Operador Lógico>"); }
"<="			{ printf("<Operador Relacional>"); }
">="			{ printf("<Operador Relacional>"); }
"=="			{ printf("<Operador Relacional>"); }
"!="			{ printf("<Operador Relacional>"); }
";"		  	{ printf("<fin comando>"); }
("{"|"<%")		{ printf("<Agrupador>"); }
("}"|"%>")		{ printf("<Agrupador>"); }
","		  	{ printf("<Operador>"); }
":"			  { printf("<Operador>"); }
"="			  { printf("<Operador>"); }
"("			  { printf("<Operador>"); }
")"			  { printf("<Operador>"); }
("["|"<:")		{ printf("<Agrupacion>"); }
("]"|":>")		{ printf("<Agrupacion>"); }
"."		  	{ printf("<Operador>"); }
"&"		  	{ printf("<Operador>"); }
"!"			  { printf("<Operador>"); }
"~"			  { printf("<Operador>"); }
"-"			  { printf("<Operador Arimetico>"); }
"+"			  { printf("<Operador Arimetico>"); }
"*"			  { printf("<Operador Arimetico>"); }
"/"			  { printf("<Operador Arimetico>"); }
"%"			  { printf("<Operador Arimetico>"); }
"<"			  { printf("<Operador>"); }
">"			  { printf("<Operador>"); }
"^"			  { printf("<Operador>"); }
"|"			  { printf("<Operador>"); }
"?"			  { printf("<Operador>"); }
[ \t\v\n\f]		{ printf("<tab>"); }


%% 


