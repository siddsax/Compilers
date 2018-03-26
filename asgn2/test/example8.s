.section .data
b:
	.int 0
c:
	.int 0
a:
	.int 0
format:
	.ascii "%d\0"
format1:
	.ascii "%d\n\0"
.section .bss
.section .text
.globl main
main:

	#1, =, a, 2, 
	movl (a), %ecx
movl $2, %ecx

	#2, =, b, 5, 
	movl (b), %edx
movl $5, %edx

	#3, +, c, b, a, 
	movl %ecx, a
movl (c), %ecx
movl (a), %ecx
add %edx, %ecx

	#4, print, c, 
### Flushing -----------
	movl %ecx, c
	movl %edx, b
### Flushed ------------
	pushl c
	pushl $format1
	call printf

	#5, exit, 
	call exit
### Flushing -----------
### Flushed ------------

