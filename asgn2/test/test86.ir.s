############################33333
.section .data
D1750:
	.int 0
D1746:
	.int 0
D1745:
	.int 0
a7:
	.int 0
c:
	.int 0
D1737:
	.int 0
D1748:
	.int 0
D1740:
	.int 0
d:
	.int 0
a5:
	.int 0
a0:
	.int 0
a6:
	.int 0
b0:
	.int 0
b:
	.int 0
D1749:
	.int 0
a4:
	.int 0
D1741:
	.int 0
a3:
	.int 0
D1747:
	.int 0
D1738:
	.int 0
D1742:
	.int 0
D1739:
	.int 0
a1:
	.int 0
b1:
	.int 0
a2:
	.int 0
format:
	.ascii "%d\0"
format1:
	.ascii "%d\n\0"
arr:  .fill 10, 4, 0 
.section .bss
.section .text
.globl main
main:

	#1, =, c, 1, 
	movl (c), %ecx
movl $1, %ecx

	#2, =, a0, 1, 
	movl (a0), %eax
movl $1, %eax

	#3, =, a1, 1, 
	movl (a1), %edx
movl $1, %edx

	#4, =, a2, 1, 
	movl (a2), %ebx
movl $1, %ebx

	#5, =, a3, 2, 
	movl $2, a3

	#6, =, a4, 0, 
	movl $0, a4

	#7, =, a5, 1, 
	movl $1, a5

	#8, =, a6, 0, 
	movl $0, a6

	#9, =, a7, 1, 
	movl $1, a7
### Flushing -----------
	movl %ecx, c
	movl %eax, a0
	movl %edx, a1
	movl %ebx, a2
### Flushed ------------

	#10, conditional_goto, ge, c, 0, D1735, 
	movl (c), %ecx
	cmp $0 , %ecx
	jg D1735
### Flushing -----------
	movl %ecx, c
### Flushed ------------

	#11, goto, D1736, 
	jmp D1736
### Flushing -----------
### Flushed ------------

	#12, label, D1735, 
D1735: 
## loading
movl (D1739), %ecx
movl (D1738), %eax
movl (D1742), %edx
movl (b0), %ebx

	#13, +, D1737, a0, a1, 
	movl %ecx, D1739
movl (a1), %ecx
add (a0), %ecx

	#14, =, arr, arr_init, 10, 

	#15, array_asgn, arr, 0, D1737, 
	movl %ecx, (arr+0)

	#16, +, D1738, D1737, a2, 
	movl (a2), %eax
add %ecx, %eax

	#17, array_asgn, arr, 1, D1738, 
	movl %eax, (arr+1)

	#18, array_access, d, arr, 0, 
	movl %ecx, D1737
movl (arr+0), %ecx

	#19, print, d, 
### Flushing -----------
	movl %ecx, d
	movl %eax, D1738
	movl %edx, D1742
	movl %ebx, b0
### Flushed ------------
	pushl d
	pushl $format1
	call printf

	#20, array_access, d, arr, 1, 
	movl (d), %ecx
movl (arr+1), %ecx

	#21, print, d, 
### Flushing -----------
	movl %ecx, d
### Flushed ------------
	pushl d
	pushl $format1
	call printf

	#22, +, D1739, D1738, a3, 
	movl (D1739), %ecx
movl (a3), %ecx
add (D1738), %ecx

	#23, +, D1740, D1739, a4, 
	movl (D1740), %eax
movl (a4), %eax
add %ecx, %eax

	#24, +, D1741, D1740, a5, 
	movl (D1741), %edx
movl (a5), %edx
add %eax, %edx

	#25, +, D1742, D1741, a6, 
	movl (D1742), %ebx
movl (a6), %ebx
add %edx, %ebx

	#26, +, b0, D1742, a7, 
	movl %ecx, D1739
movl (a7), %ecx
add %ebx, %ecx

	#27, =, b, b0, 
	movl %ecx, b0
movl (b), %ecx
movl (b0), %ecx
### Flushing -----------
	movl %ecx, b
	movl %eax, D1740
	movl %edx, D1741
	movl %ebx, D1742
### Flushed ------------

	#28, goto, D1744, 
	jmp D1744
### Flushing -----------
### Flushed ------------

	#29, label, D1736, 
D1736: 
## loading
movl (D1750), %ecx
movl (D1747), %eax
movl (D1745), %edx
movl (D1748), %ebx

	#30, -, D1745, a1, a0, 
	movl (a0), %edx
sub (a1), %edx

	#31, +, D1746, D1745, a2, 
	movl %edx, D1745
movl (a2), %edx
add (D1745), %edx

	#32, +, D1747, D1746, a3, 
	movl (a3), %eax
add %edx, %eax

	#33, +, D1748, D1747, a4, 
	movl (a4), %ebx
add %eax, %ebx

	#34, +, D1749, D1748, a5, 
	movl %eax, D1747
movl (a5), %eax
add %ebx, %eax

	#35, +, D1750, D1749, a6, 
	movl (a6), %ecx
add %eax, %ecx

	#36, +, b1, D1750, a7, 
	movl %ecx, D1750
movl (a7), %ecx
add (D1750), %ecx

	#37, =, b, b1, 
	movl %ecx, b1
movl (b), %ecx
movl (b1), %ecx
### Flushing -----------
	movl %ecx, b
	movl %eax, D1749
	movl %edx, D1746
	movl %ebx, D1748
### Flushed ------------

	#38, label, D1744, 
D1744: 
## loading
movl (d), %ecx
movl (b), %eax

	#39, print, b, 
### Flushing -----------
	movl %ecx, d
	movl %eax, b
### Flushed ------------
	pushl b
	pushl $format1
	call printf

	#40, array_access, d, arr, 0, 
	movl (d), %ecx
movl (arr+0), %ecx

	#41, print, d, 
### Flushing -----------
	movl %ecx, d
### Flushed ------------
	pushl d
	pushl $format1
	call printf

	#42, array_access, d, arr, 1, 
	movl (d), %ecx
movl (arr+1), %ecx

	#43, print, d, 
### Flushing -----------
	movl %ecx, d
### Flushed ------------
	pushl d
	pushl $format1
	call printf

	#44, exit, 
	call exit

