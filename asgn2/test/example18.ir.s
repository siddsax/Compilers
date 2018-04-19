############################33333
.section .data
a:
	.int 0
c:
	.int 0
d:
	.int 0
b:
	.int 0
format:
	.ascii "%d\0"
format1:
	.ascii "%d\n\0"
format2:
	.ascii "%c\n\0"
arr:  .fill 10, 4, 0 
.section .bss
.section .text
.globl main
main:

	#1, =, arr, arr_init, 10, 

	#2, =, a, 5, 
	movl (a), %eax
movl $5, %eax

	#3, =, b, 2, 
	movl (b), %ebx
movl $2, %ebx

	#4, +, c, a, b, 
	movl %ebx, b
movl (c), %ebx
movl (b), %ebx
add %eax, %ebx

	#5, array_asgn, arr, 0, c, 
	movl %ebx, (arr+0)

	#6, array_access, d, arr, 0, 
	movl (d), %edx
	movl (0), %ecx
movl (arr+ $0), %edx

	#7, print, d, 
### Flushing -----------
	movl %eax, a
	movl %ebx, c
	movl %edx, d
	movl %ecx, 0
### Flushed ------------
	pushl d
	pushl $format1
	call printf

	#8, exit, 
	call exit
### Flushing -----------
### Flushed ------------

