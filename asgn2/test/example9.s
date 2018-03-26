.section .data
a:
	.int 0
pr:
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

	#1, =, a, 10, 
	movl (a), %ebx
movl $10, %ebx

	#2, scan, b, 
### Flushing -----------
	movl %ebx, a
### Flushed ------------
pushl $b
pushl $format
call scanf
### Flushing -----------
### Flushed ------------

	#3, label, loop, 
loop: 
## loading
movl (pr), %ebx
movl (a), %edx
movl (b), %eax

	#4, +, a, a, b, 
		movl %edx, a
	movl %eax, %edx
add (a) , %edx

	#5, =, pr, 30, 
	movl $30, %ebx

	#6, print, a, 
### Flushing -----------
	movl %ebx, pr
	movl %edx, a
	movl %eax, b
### Flushed ------------
	pushl a
	pushl $format1
	call printf
### Flushing -----------
### Flushed ------------

	#7, conditional_goto, leq, a, 50, loop, 
	movl (a), %ebx
	cmp $50 , %ebx
	jle loop

	#8, exit, 
	call exit
### Flushing -----------
	movl %ebx, a
### Flushed ------------

