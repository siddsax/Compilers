.section .data
a:
.int 0
b:
.int 0
.section .bss
.section .text
.globl main
main:
	#8, fn_def, foo, 
foo:
	#9, print, a, 
	#10, return, 
	leave
	ret
	#1, =, a, 2, 
		mov $2, %ebx
	#2, label, kshit, 
kshit: 
	#3, =, b, 7, 
		mov $7, %edx
	#4, +, a, a, b, 
		add %edx, %ebx
	#5, conditional_goto, leq, a, 50, kshit, 
	cmp $50 , %ebx
	jle kshit
	#6, fn_call_1, foo, 
	call foo
	#7, return, 
	leave
	ret

