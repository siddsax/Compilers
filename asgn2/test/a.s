.section .data
a:
.int 0
b:
.int 0
c:
.int 0
.section .bss
.section .text
.globl main
main:

	#1, =, a, 2, 
	movl $2, %ebx

	#2, =, b, 7, 
	movl $7, %eax

	#3, *, a, b, a, 
	movl %eax, $b
	movl $b, %eax
	movl %ebx, %edx
	imul %edx

	#3, conditional_goto, leq, b, a, zoo, 
	cmp %edx , $b
	jle zoo

	#4, label, koo, 
koo: 

	#4, --, b, 

	#4, =, c, 6, 
	movl $6, %ecx

	#5, fn_call_2, c, foo, 
	call c

	#6, +, c, a, b, 
	movl $b, %ebx
	add %edx, %ebx

	#5, return, 
	leave
	ret

	#7, label, foo, 
foo: 

	#8, +=, c, 4, 

