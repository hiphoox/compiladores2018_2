    .golbl _main
    _main:
     ret
     cmpl $1, %eax
     movl $99, %eax
    sete %al