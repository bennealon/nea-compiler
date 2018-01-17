# nea-compiler

following this...
https://norasandler.com/2017/11/29/Write-a-Compiler.html

Compile using:

> gcc -S -O3 -fno-asynchronous-unwind-tables return_2.c

link using:

> gcc -m64 return_2.s -o return_2