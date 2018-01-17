#!/bin/bash

gcc -S -O3 -fno-asynchronous-unwind-tables return_2.c
gcc -m64 return_2.s -o return_2