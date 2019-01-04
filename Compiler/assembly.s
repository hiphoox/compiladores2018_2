.globl main
main:
	mov $2,%eax
	push %eax
	pop %ecx
	imul %ecx, %eax
ret