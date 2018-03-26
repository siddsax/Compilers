.section .data
a:
	.int 0
c:
	.int 0
format:
	.ascii "%d\0"
format1:
	.ascii "%d\n\0"
.section .bss
.section .text
.globl main
main:

	#1, =, a, 8, 
	movl (a), %ebx
movl $8, %ebx

	#2, <<, c, 1, a, 
	movl %ebx, a
movl (c), %ebx
movl (a), %ebx
shl $1, %ebx

	#3, print, c, 
### Flushing -----------
	movl %ebx, c
### Flushed ------------
	pushl c
	pushl $format1
	call printf

	#4, exit, 
	call exit
### Flushing -----------
### Flushed ------------

