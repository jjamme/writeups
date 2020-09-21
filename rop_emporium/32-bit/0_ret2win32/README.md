# ret2win
In this challenge you have to overflow a 40 byte and then the 4 byte base pointer to reach the return address where you can start writing where you want it to jump to after execution.
| 40 bytes | ebp | esp |
| :---: | :--: | :--: |
| AAAA...AAAA | BBBB | `ret2win` |
In the exploit script I fill the original buffer with 40 A's and then the ebp with B's, after this I write the address of the function `ret2win` over what used to be in esp so that the program will enter that function after exiting the current function.