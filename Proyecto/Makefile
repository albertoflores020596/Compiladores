 a.out: main.o lex.yy.o ansiC.tab.o
	gcc main.o lex.yy.o ansiC.tab.o -ll

 ansiC.tab.c: ansiC.y
	bison -d ansiC.y
	
 main.o: main.c 
	gcc -c main.c

 lex.yy.o: lex.yy.c
	gcc -c lex.yy.c

 ansiC.tab.o: ansiC.tab.c
	gcc -c ansiC.tab.c

 lex.yy.c: ansiC.l ansiC.tab.c
	flex ansiC.l


 clean:
	rm  -f a.out main.o lexx.yy.o ansiC.tab.o lex.yy.c ansiC.tab.c ansiC.tab.h

 run: a.out
	./a.out test.c
