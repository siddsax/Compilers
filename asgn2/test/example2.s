.section .data
a:
	.int 0
d:
	.int 0
b:
	.int 0
c:
	.int 0
e:
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
	movl (a), %edx
movl $2, %edx

	#2, =, b, 7, 
	movl (b), %ebx
movl $7, %ebx

	#3, =, c, 10, 
	movl (c), %ecx
movl $10, %ecx

	#4, =, d, 20, 
	movl (d), %eax
movl $20, %eax

	#5, +, a, a, b, 
		movl %edx, a
	movl %ebx, %edx
add (a) , %edx

	#6, /, c, c, b, 
	movl %eax, d
	movl %edx, a
	movl %ecx, c
	movl $0, %edx
	movl %ebx, %eax
	movl (c), %ecx
	idiv %ecx

	#7, /, d, a, b, 
	movl %eax, c
	movl $0, %edx
	movl %ebx, %eax
	movl (a), %ecx
	idiv %ecx

	#8, +, e, b, d, 
	movl (e), %edx
movl %eax, %edx
add %ebx, %edx

	#9, print, c, 
### Flushing -----------
	movl %edx, e
	movl %ebx, b
	movl %eax, d
### Flushed ------------
	pushl c
	pushl $format1
	call printf

	#10, exit, 
	call exit
### Flushing -----------
### Flushed ------------

