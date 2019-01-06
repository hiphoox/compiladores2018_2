.globl main
main:
	mov $3,%eax
	push %eax
	mov $2,%eax
	pop %ecx
	addl %ecx, %eax
	push %eax
	mov $1,%eax
	pop %ecx
	addl %ecx, %eax
ret