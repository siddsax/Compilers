.section .data
k:
	.int 0
b:
	.int 0
a:
	.int 0
dst:
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
	movl (a), %eax
movl $10, %eax
### Flushing -----------
	movl %eax, a
### Flushed ------------

	#2, label, kshit, 
kshit: 
## loading
movl (b), %eax
movl (a), %ebx

	#3, =, b, 7, 
	movl $7, %eax

	#4, +, a, a, b, 
		movl %ebx, a
	movl %eax, %ebx
add (a) , %ebx

	#5, print, a, 
### Flushing -----------
	movl %eax, b
	movl %ebx, a
### Flushed ------------
	pushl a
	pushl $format1
	call printf
### Flushing -----------
### Flushed ------------

	#6, conditional_goto, leq, a, 50, kshit, 
	movl (a), %eax
	cmp $50 , %eax
	jle kshit
### Flushing -----------
	movl %eax, a
### Flushed ------------

	#7, fn_call_2, foo, dst, 
	call foo
movl %eax, dst
## loading
movl (dst), %eax

	#8, print, dst, 
### Flushing -----------
	movl %eax, dst
### Flushed ------------
	pushl dst
	pushl $format1
	call printf

	#9, exit, 
	call exit

	#10, fn_def, foo, 
foo:
	pushl %ebp
	movl %esp, %ebp
## loading
movl (k), %eax

	#11, =, k, 200, 
	movl $200, %eax
### Flushing -----------
	movl %eax, k
### Flushed ------------

	#12, return, k, 
	movl (k), %eax
	leave
	ret

