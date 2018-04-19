############################33333
.section .data
k:
	.int 0
q:
	.int 0
b:
	.int 0
p:
	.int 0
d:
	.int 0
a:
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

	#2, =, a, 5, 
	movl (a), %ebx
movl $5, %ebx

	#3, =, q, 2, 
	movl (q), %eax
movl $2, %eax

	#4, =, b, 2, 
	movl (b), %ecx
movl $2, %ecx

	#5, +, c, a, b, 
	movl (c), %edx
###-/--
movl %ecx, %edx
add %ebx, %edx

	#6, -, k, 2, 3, 
	movl %eax, q
movl $1, %eax

	#7, /, k, a, k, 
	movl %eax, k
	movl %edx, c
	movl %ecx, b
	movl $0, %edx
	movl (k), %eax
	movl %ebx, %ecx
	idiv %ecx

	#8, <, p, k, c, 
	movl (p), %ecx
###-/--
movl (c), %ecx
cmp  %eax, %ecx
movl $1,%ecx
jl comparision_lbl_8
movl $0,%ecx
comparision_lbl_8:

	#9, array_asgn, arr, a, b, 
	movl $arr, %edx
###-/--
add a ,%edx
	###----
############
movl b, (%edx)

	#10, array_access, d, arr, k, 
	movl %eax, k
movl $arr, %eax
###-/--
add (k) ,%eax
	movl (d), %edx
###-/--
movl (%eax), %edx

	#11, print, d, 
### Flushing -----------
	movl %ebx, a
	movl %ecx, p
	movl %edx, d
### Flushed ------------
	pushl d
	pushl $format1
	call printf

	#12, exit, 
	call exit
### Flushing -----------
### Flushed ------------

