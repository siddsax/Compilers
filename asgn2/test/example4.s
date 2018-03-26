.section .data
dm:
	.int 0
b:
	.int 0
a:
	.int 0
c:
	.int 0
d:
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

	#3, =, c, 4, 
	movl (c), %ecx
movl $4, %ecx

	#4, =, d, 6, 
	movl (d), %eax
movl $6, %eax

	#5, +, a, a, c, 
		movl %edx, a
	movl %ecx, %edx
add (a) , %edx
### Flushing -----------
	movl %edx, a
	movl %ebx, b
	movl %ecx, c
	movl %eax, d
### Flushed ------------
### Flushing -----------
### Flushed ------------

	#6, fn_call_2, foo, c, 
	call foo
movl %eax, c
## loading
movl (c), %edx

	#7, print, c, 
### Flushing -----------
	movl %edx, c
	movl %eax, c
### Flushed ------------
	pushl c
	pushl $format1
	call printf

	#8, exit, 
	call exit

	#9, fn_def, foo, 
foo:
	pushl %ebp
	movl %esp, %ebp
## loading
movl (dm), %edx

	#10, =, dm, 30, 
	movl $30, %edx
### Flushing -----------
	movl %edx, dm
### Flushed ------------

	#11, return, dm, 
	movl (dm), %eax
	leave
	ret

