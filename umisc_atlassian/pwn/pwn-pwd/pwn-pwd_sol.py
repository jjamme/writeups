from pwn import *

#context.log_level = "debug"
remote_conn = True

IP = "ctfo.2pmc.net"
PORT = "10001"
FILENAME = "./pwn-pwd"

#libc = ELF("")
#ld = ELF("")

if remote_conn:
    p = remote(IP, PORT)
    elf = ELF(FILENAME)
else:
    #p = process([ld.path, elf.path], env={"LD_PRELOAD": libc.path})
    p = process(FILENAME)
    elf = p.elf

p.sendlineafter(b"Enter the password:", b"supe\x07r_s3cret")

p.interactive()
