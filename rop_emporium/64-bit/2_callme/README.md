# callme 64-bit
===
This challenge teaches you to use the SysV calling convention (calling convention for 64-bit assembly).

First step: Get the 3 required arguments into the three registers RDI RSI and RDX by using the `pop rdi; pop rsi; pop rdx; ret;` instruction.
Second step: Call the function and it will recognise the three registers as the three function arguments.

