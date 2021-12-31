flex flexx.l
bison -vdty yaccc.y
g++ -std=c++11 -o compiler Tree.cpp Praser.cpp InterCode.cpp Assist.cpp lex.yy.c y.tab.c
compiler.exe test/base.cpp
python TransToAssemble.py