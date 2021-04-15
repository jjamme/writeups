// gcc pwn-pwd.c -o pwn-pwd -fno-stack-protector

#include <stdio.h>
#include <string.h>

void printFlag(void) {
	printf("The flag is: XXXXXXXXXXXXXXXX\n");
	fflush(stdout);
}

void checkPassword() {
	char buf[20];
	char *password = "supe\x07r_s3cret"; //add a \x07 so they have to write code to solve, suckaaaaaa

	printf("Enter the password: ");
	fflush(stdout);

	gets(buf);

	if (strcmp(password, buf) == 0) {
		printFlag();
	} else {
		printf("FAIL!");
		fflush(stdout);
	}
}

int main(void) {
	printf("The address of printFlag %p.\n", printFlag);
	fflush(stdout);

	checkPassword();

	printf("Hit <Enter> to close.\n");
	fflush(stdout);

  	return 0;
}
