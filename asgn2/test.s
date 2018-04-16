.section .data
f:
	.int 0
e:
	.int 0
b:
	.int 0
d:
	.int 0
dm:
	.int 0
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

	#1, =, a, 2, 
	movl (a), %edx
movl $2, %edx

	#2, =, b, 7, 
	movl (b), %eax
movl $7, %eax

	#3, =, c, 4, 
	movl (c), %ebx
movl $4, %ebx

	#4, =, d, 6, 
	movl (d), %ecx
movl $6, %ecx

	#5, +, a, a, 0, 
		movl %edx, a
	movl $0, %edx
add (a) , %edx
### Flushing -----------
	movl %edx, a
	movl %eax, b
	movl %ebx, c
	movl %ecx, d
### Flushed ------------
### Flushing -----------
### Flushed ------------

	#6, fn_call_2, foo, 2, a, b, c, 
	pushl (a)
	pushl (b)
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

	#9, fn_def, foo, 2, e, f, 
foo:
	pushl %ebp
	movl %esp, %ebp
	movl 4(%ebp), e
	movl 8(%ebp), f
## loading
movl (dm), %edx
movl (e), %eax
movl (f), %ebx

	#10, +, dm, e, f, 
	movl %ebx, %edx
add %eax, %edx
### Flushing -----------
	movl %edx, dm
	movl %eax, e
	movl %ebx, f
### Flushed ------------

	#11, return, dm, 
	movl (dm), %eax
	leave
	ret

