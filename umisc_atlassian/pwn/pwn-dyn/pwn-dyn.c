// gcc pwn-dyn.c -o pwn-dyn -fno-stack-protector

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void printFlag(void) {
	printf("The flag is: xxxxxxxxxxxxxxxxxx\n");
	fflush(stdout);
}

char* generatePassword() {
	unsigned char* password = (unsigned char*)malloc(20 * sizeof(char));

	password[0] = 13;
	password[1] = 37;

	int i = 0;
	for (i = 2; i < 19; i++) {
		password[i] = password[i-1] * password[i-2];  
	}

	for (i = 0; i < 19; i++) {
		password[i] = (password[i] % 26) + 'a';
	}
	password[19] = '\x00';

	return password;
}

void printName() {
	char buf[20];

	char *password = generatePassword();
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

	printName();

	printf("Hit <Enter> to close.\n");
	fflush(stdout);

  	return 0;
}
