.section .data
a:
	.int 0
b:
	.int 0
format:
	.ascii "%d\0"
format1:
	.ascii "%d\n\0"
.section .bss
.section .text
.globl main
main:

	#1, scan, a, 
### Flushing -----------
### Flushed ------------
pushl $a
pushl $format
call scanf

	#2, print, a, 
### Flushing -----------
### Flushed ------------
	pushl a
	pushl $format1
	call printf

	#3, scan, b, 
### Flushing -----------
### Flushed ------------
pushl $b
pushl $format
call scanf

	#4, print, b, 
### Flushing -----------
### Flushed ------------
	pushl b
	pushl $format1
	call printf

	#5, exit, 
	call exit
### Flushing -----------
### Flushed ------------

