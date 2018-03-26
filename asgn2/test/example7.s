.section .data
dst:
	.int 0
a:
	.int 0
b:
	.int 0
chutiya:
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
movl (a), %ecx

	#3, =, b, 15, 
	movl $15, %eax

	#4, +, a, a, b, 
		movl %ecx, a
	movl %eax, %ecx
add (a) , %ecx

	#5, print, a, 
### Flushing -----------
	movl %eax, b
	movl %ecx, a
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

	#7, fn_call_1, blue, 
	call blue
### Flushing -----------
### Flushed ------------

	#8, fn_call_2, foo, dst, 
	call foo
movl %eax, dst
## loading
movl (dst), %eax

	#9, print, dst, 
### Flushing -----------
	movl %eax, dst
### Flushed ------------
	pushl dst
	pushl $format1
	call printf

	#10, =, dst, 0, 
	movl (dst), %eax
movl $0, %eax

	#11, exit, 
	call exit

	#12, fn_def, foo, 
foo:
	pushl %ebp
	movl %esp, %ebp
## loading
movl (chutiya), %eax
movl (b), %ecx
movl (a), %ebx

	#13, =, chutiya, b, 
	movl %ecx, %eax

	#14, +, a, a, b, 
		movl %ebx, a
	movl %ecx, %ebx
add (a) , %ebx
### Flushing -----------
	movl %eax, chutiya
	movl %ecx, b
	movl %ebx, a
### Flushed ------------

	#15, return, a, 
	movl (a), %eax
	leave
	ret

	#16, fn_def, blue, 
blue:
	pushl %ebp
	movl %esp, %ebp
## loading

	#17, print, 100, 
### Flushing -----------
### Flushed ------------
	pushl $100
	pushl $format1
	call printf
### Flushing -----------
### Flushed ------------

	#18, return, 
	leave
	ret

