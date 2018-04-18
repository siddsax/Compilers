############################33333
.section .data
D1747:
	.int 0
b1:
	.int 0
D1748:
	.int 0
a1:
	.int 0
D1750:
	.int 0
D1749:
	.int 0
a7:
	.int 0
D1741:
	.int 0
c:
	.int 0
D1737:
	.int 0
a5:
	.int 0
a6:
	.int 0
D1739:
	.int 0
D1740:
	.int 0
a2:
	.int 0
a4:
	.int 0
D1742:
	.int 0
a0:
	.int 0
D1738:
	.int 0
D1745:
	.int 0
D1746:
	.int 0
b0:
	.int 0
d:
	.int 0
b:
	.int 0
a3:
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
	movl (a1), %ebx
movl $1, %ebx

	#4, =, a2, 1, 
	movl (a2), %edx
movl $1, %edx

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
	movl %ebx, a1
	movl %edx, a2
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
movl (D1742), %ecx
movl (D1737), %eax
movl (D1738), %ebx
movl (D1739), %edx

	#13, +, D1737, a0, a1, 
	movl (a1), %eax
add (a0), %eax

	#14, =, arr, arr_init, 10, 

	#15, array_asgn, arr, 0, D1737, 
	movl %eax, (arr+0)

	#16, +, D1738, D1737, a2, 
	movl (a2), %ebx
add %eax, %ebx

	#17, array_asgn, arr, 4, D1738, 
	movl %ebx, (arr+4)

	#18, array_access, d, arr, 0, 
	movl %eax, D1737
movl (arr+0), %eax

	#19, print, d, 
### Flushing -----------
	movl %ecx, D1742
	movl %eax, d
	movl %ebx, D1738
	movl %edx, D1739
### Flushed ------------
	pushl d
	pushl $format1
	call printf

	#20, array_access, d, arr, 4, 
	movl (d), %ecx
movl (arr+4), %ecx

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
	movl (D1741), %ebx
movl (a5), %ebx
add %eax, %ebx

	#25, +, D1742, D1741, a6, 
	movl (D1742), %edx
movl (a6), %edx
add %ebx, %edx

	#26, +, b0, D1742, a7, 
	movl %ecx, D1739
movl (a7), %ecx
add %edx, %ecx

	#27, =, b, b0, 
	movl %ecx, b0
movl (b), %ecx
movl (b0), %ecx
### Flushing -----------
	movl %ecx, b
	movl %eax, D1740
	movl %ebx, D1741
	movl %edx, D1742
### Flushed ------------

	#28, goto, D1744, 
	jmp D1744
### Flushing -----------
### Flushed ------------

	#29, label, D1736, 
D1736: 
## loading
movl (D1747), %ecx
movl (b1), %eax
movl (D1748), %ebx
movl (D1750), %edx

	#30, -, D1745, a1, a0, 
	movl %ecx, D1747
movl (a0), %ecx
sub (a1), %ecx

	#31, +, D1746, D1745, a2, 
	movl %ecx, D1745
movl (a2), %ecx
add (D1745), %ecx

	#32, +, D1747, D1746, a3, 
	movl %ecx, D1746
movl (a3), %ecx
add (D1746), %ecx

	#33, +, D1748, D1747, a4, 
	movl (a4), %ebx
add %ecx, %ebx

	#34, +, D1749, D1748, a5, 
	movl %ecx, D1747
movl (a5), %ecx
add %ebx, %ecx

	#35, +, D1750, D1749, a6, 
	movl (a6), %edx
add %ecx, %edx

	#36, +, b1, D1750, a7, 
	movl (a7), %eax
add %edx, %eax

	#37, =, b, b1, 
	movl %eax, b1
movl (b), %eax
movl (b1), %eax
### Flushing -----------
	movl %ecx, D1749
	movl %eax, b
	movl %ebx, D1748
	movl %edx, D1750
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

	#42, array_access, d, arr, 4, 
	movl (d), %ecx
movl (arr+4), %ecx

	#43, print, d, 
### Flushing -----------
	movl %ecx, d
### Flushed ------------
	pushl d
	pushl $format1
	call printf

	#44, exit, 
	call exit

