#include <stdio.h>
#include <string.h>

void encodeFunction(char userString[], char layout[]) {
    for (int i = 0; i < strlen(userString); i++) {
        char *p = strchr(layout, userString[i]);
        if (p != NULL) {
            int idx = p - layout;
            if (idx + 1 < 26) {
                userString[i] = layout[idx+1];
            }
            else {
                userString[i] = layout[0];
            }
        }
    }
    printf("Encrypted string: %s\n", userString);
}

void decodeFunction(char userString[], char layout[]) {
    for (int i = 0; i < strlen(userString); i++) {
        char *p = strchr(layout, userString[i]);
        if (p != NULL) {
            int idx = p - layout;
            if (idx + 1 < 26) {
                userString[i] = layout[idx-1];
            }
            else {
                userString[i] = layout[26];
            }
        }
    }
    printf("Decrypted string: %s\n", userString);
}
int main() {

    char layout[] = "qwertyuiopasdfghjklzxcvbnm";
    char userString[100];
    char userChoice;

    while (1) {

        printf("\n=== HYPERSECUREENCRYPTION ===\ne) encode\nd) decode\nq) quit\nEnter your choice: ");
        scanf(" %c", &userChoice);

        switch (userChoice) {
            case 'q':
                return 0;
            case 'e':
                printf("Enter vanilla string: ");
                scanf(" %[^\n]", userString);
                encodeFunction(userString, layout);
                break;
            case 'd':
                printf("Enter encrypted string: ");
                scanf(" %[^\n]", userString);
                decodeFunction(userString, layout);
                break;
        }
    }
}
