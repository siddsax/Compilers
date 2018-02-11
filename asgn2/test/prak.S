.data

a:
	.int	0
b:
	.int	0
c:
	.int	0

.text

.global _start

_start:

	call main
	jmp exit


main:

	pushl %ebp
	movl %esp, %ebp
	# 1, =, a, 2
	movl $2, a
	# 2, =, b, 7
	movl $7, b
	# 3, <, a, a, b
	movl (a), %eax
	movl (a), %eax
	subl $1, %eax
	cmp (b), %eax
	setle  %al
	movzbl %al, %eax
	# 3, ifgoto, a, zoo
	cmp $0, %eax
	jne zoo
	movl %eax, a
	# 4, label, koo

koo:

	# 4, --, b
	decl b
	# 4, =, c, 6
	movl $6, c
	# 5, callint, c, foo
	call foo
	movl %eax, c
	# 6, +, c, a, b
	movl (c), %eax
	movl (a), %eax
	addl (b), %eax
	movl %eax, c
	# 5, retvoid
	leave
	ret
	# 7, label, foo

foo:

	pushl %ebp
	movl %esp,  %ebp
	# 8, +=, c, 4
	addl $4, %eax
	# 9, retint, c
	movl (c), %eax
	leave
	ret
	# 10, label, zoo

zoo:

	# 11, =, a, 96
	movl $96, a
	# 12, goto, koo
	jmp koo

exit:

	movl $0, %ebx
	movl $1, %eax
	int $0x80
