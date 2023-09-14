#include <stdio.h>
#include <string.h>

void strong_encryption(char *array)
{
    char secret[8] = { 22, 53, 44, 71, 66, 177, 253, 122 };
    for(int i = 0; i < 7; i++)
        array[i] ^= secret[i];
}

int main(int argc, char *argv[]) {
    char buffer [8]; 
    char password[8] = "deez";
    
    printf("Enter the password: \n");
    scanf("%s", buffer); 
    strong_encryption(buffer);
    printf("%s\n", buffer);
    printf("%p\n", buffer);
    printf("%p\n", password);
    printf("%s\n", password);
    if (strncmp(buffer, password, 4) == 0) {
      printf("Success!\n");
    }
    else {
      printf("FAIL!\n");
    }
}