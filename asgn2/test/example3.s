.section .data
a:
	.int 0
b:
	.int 0
format:
	.ascii "%d\n\0"
.section .bss
.section .text
.globl main
main:

	#1, =, a, 5, 
	movl $5, %edx

	#2, +, a, a, 100, 
	add $100, %edx

	#3, =, b, 10, 
	movl $10, %eax

	#4, print, a, 
	pushl %edx
	pushl $format
	call printf

	#5, exit, 
	call exit

