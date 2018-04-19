############################33333
.section .data
d:
	.int 0
p:
	.int 0
c:
	.int 0
q:
	.int 0
a:
	.int 0
k:
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

	#2, =, a, 4, 
	movl (a), %ebx
movl $4, %ebx

	#3, =, q, 2, 
	movl (q), %edx
movl $2, %edx

	#4, =, b, 2, 
	movl %edx, q
movl (b), %edx
movl $2, %edx

	#5, +, c, a, b, 
	movl (c), %eax
movl %edx, %eax
add %ebx, %eax

	#6, -, k, 2, 3, 
	movl (k), %ecx
movl $1, %ecx

	#7, /, k, 1, k, 
	movl %eax, c
	movl %edx, b
	movl %ecx, k
	movl $0, %edx
	movl (k), %eax
	movl $1, %ecx
	idiv %ecx

	#8, <, p, k, c, 
	movl (p), %edx
movl (c), %edx
cmp  %eax, %edx
movl $1,%edx
jl comparision_lbl_8
movl $0,%edx
comparision_lbl_8:

	#9, array_asgn, arr, a, b, 
	movl %edx, p
movl $arr, %edx
addl a ,%edx
	movl %eax, k
movl (b), %eax
############
movl %eax, (%edx)

	#10, array_access, d, arr, 4, 
	movl $arr, %edx
addl $4 ,%edx
	movl (d), %ecx
movl (%edx), %ecx

	#11, print, a, 
### Flushing -----------
	movl %ebx, a
	movl %eax, b
	movl %ecx, d
### Flushed ------------
	pushl a
	pushl $format1
	call printf

	#12, print, b, 
### Flushing -----------
### Flushed ------------
	pushl b
	pushl $format1
	call printf

	#13, print, d, 
### Flushing -----------
### Flushed ------------
	pushl d
	pushl $format1
	call printf

	#14, exit, 
	call exit
### Flushing -----------
### Flushed ------------

