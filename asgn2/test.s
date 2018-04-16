.section .data
c:
	.int 0
f:
	.int 0
b:
	.int 0
e:
	.int 0
d:
	.int 0
dm:
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

	#2, =, b, 7, 
	movl (b), %ebx
movl $7, %ebx

	#3, =, c, 4, 
	movl (c), %edx
movl $4, %edx

	#4, =, d, 6, 
	movl (d), %eax
movl $6, %eax

	#5, +, a, a, 0, 
		movl %ecx, a
	movl $0, %ecx
add (a) , %ecx
### Flushing -----------
	movl %ecx, a
	movl %ebx, b
	movl %edx, c
	movl %eax, d
### Flushed ------------
### Flushing -----------
### Flushed ------------

	#6, fn_call_2, foo, 2, a, b, c, 
	pushl (a)
	pushl (b)
	call foo
movl %eax, c
## loading
movl (c), %ecx

	#7, print, c, 
### Flushing -----------
	movl %ecx, c
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
movl (e), %ecx
	movl 4(%ebp), %ecx
movl (f), %ebx
	movl 8(%ebp), %ebx
## loading
movl (dm), %ecx
movl (f), %ebx
movl (e), %edx

	#10, +, dm, e, f, 
	movl %ebx, %ecx
add %edx, %ecx
### Flushing -----------
	movl %ecx, dm
	movl %ebx, f
	movl %edx, e
### Flushed ------------

	#11, return, dm, 
	movl (dm), %eax
	leave
	ret

