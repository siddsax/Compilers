############################33333
.section .data
a:
	.int 0
b:
	.int 0
d:
	.int 0
k:
	.int 0
q:
	.int 0
p:
	.int 0
c:
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
	movl (a), %eax
movl $4, %eax

	#3, =, q, 2, 
	movl (q), %edx
movl $2, %edx

	#4, =, b, 2, 
	movl %edx, q
movl (b), %edx
movl $2, %edx

	#5, +, c, a, b, 
	movl (c), %ebx
movl %edx, %ebx
add %eax, %ebx

	#6, -, k, 2, 3, 
	movl (k), %ecx
movl $1, %ecx

	#7, /, k, 1, k, 
	movl %eax, a
	movl %edx, b
	movl %ecx, k
	movl $0, %edx
	movl (k), %eax
	movl $1, %ecx
	idiv %ecx

	#8, <, p, k, c, 
	movl (p), %edx
movl %ebx, %edx
cmp  %eax, %edx
movl $1,%edx
jl comparision_lbl_8
movl $0,%edx
comparision_lbl_8:

	#9, array_asgn, arr, a, b, 
	movl %eax, k
movl $arr, %eax
add a ,%eax
	movl %edx, p
movl (b), %edx
############
movl %edx, (%eax)

	#10, array_access, d, arr, 4, 
	movl $arr, %eax
add $4 ,%eax
	movl %ebx, c
movl (d), %ebx
movl (%eax), %ebx

	#11, print, a, 
### Flushing -----------
	movl %edx, b
	movl %ebx, d
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

