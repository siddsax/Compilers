.section .data
a:
	.int 0
d:
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

	#1, =, a, 7, 
	movl (a), %edx
movl $7, %edx

	#2, =, d, 1, 
	movl (d), %ebx
movl $1, %ebx

	#3, =, b, 2, 
	movl (b), %eax
movl $2, %eax

	#4, *, b, b, a, 
	movl %eax, b
	movl %edx, a
	movl (b), %eax
	movl (a), %edx
	imul %edx

	#5, print, b, 
### Flushing -----------
	movl %ebx, d
	movl %eax, b
### Flushed ------------
	pushl b
	pushl $format1
	call printf
### Flushing -----------
### Flushed ------------

	#6, return, 
	call exit

