
#   Assembly

#T# assembly comments start with the hash #

#T# if the assembly code defines _start, it must not be compiled with the C Runtime Library (CRT). Compile with the -nostdlib flag of gcc,
# gcc -nostdlib assemblyFile.s -o execFile

#T# assembly directives start with a period, they don't generate machine code, but serve to organize the assembly. Segments also start with a period, mainly for data and code sections

#T# .file for the name of the file
	.file	"S2_02_GCC_compiler.c"

#T# the .text segment is for dividing sections of code instructions
	.text

#T# the .data segment is for static variables (i.e. global vars and static local vars, e.g. int a1 = 5;)
#	.data

#T# the .rodata segment if for read only static constants
#	.rodata
	.section	.rodata

#T# the .bss segment is for uninitialized data (e.g int i1;)
#	.bss 

#T# labels end with a colon, like .LC0:, or main: labels are used to jump to that code if called
.LC0:

#T# .string places a "string" into the program
	.string	"Hello, world!"
	.text

#T# .globl label1 declares label1 to be global, i.e. seen by the linker
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	endbr32
	leal	4(%esp), %ecx
	.cfi_def_cfa 1, 0
	andl	$-16, %esp
	pushl	-4(%ecx)
	pushl	%ebp
	.cfi_escape 0x10,0x5,0x2,0x75,0
	movl	%esp, %ebp
	pushl	%ebx
	pushl	%ecx
	.cfi_escape 0xf,0x3,0x75,0x78,0x6
	.cfi_escape 0x10,0x3,0x2,0x75,0x7c
	call	__x86.get_pc_thunk.ax
	addl	$_GLOBAL_OFFSET_TABLE_, %eax
	subl	$12, %esp
	leal	.LC0@GOTOFF(%eax), %edx
	pushl	%edx
	movl	%eax, %ebx
	call	puts@PLT
	addl	$16, %esp
	movl	$0, %eax
	leal	-8(%ebp), %esp
	popl	%ecx
	.cfi_restore 1
	.cfi_def_cfa 1, 0
	popl	%ebx
	.cfi_restore 3
	popl	%ebp
	.cfi_restore 5
	leal	-4(%ecx), %esp
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.section	.text.__x86.get_pc_thunk.ax,"axG",@progbits,__x86.get_pc_thunk.ax,comdat
	.globl	__x86.get_pc_thunk.ax
	.hidden	__x86.get_pc_thunk.ax
	.type	__x86.get_pc_thunk.ax, @function
__x86.get_pc_thunk.ax:
.LFB1:
	.cfi_startproc
	movl	(%esp), %eax
	ret
	.cfi_endproc
.LFE1:
	.ident	"GCC: (Ubuntu 9.2.1-21ubuntu1) 9.2.1 20191130"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 4
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 4
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 4
4:
