#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char * get_pwd(){
    char* buffer = malloc(8);
    FILE *fptr = fopen("password.txt", "r");
    for (int i = 0; i < 8; i++){
      char c = fgetc(fptr);
      if (c == EOF){
        buffer[i] = 0;
        break;
      }
      buffer[i] = c;
    }
    return buffer;
}

void test()
{
    char* password = get_pwd();
    printf("%s", password);
    free(password);
}

int main(int argc, char *argv[]) {
    char buffer [8]; 
    char* password = get_pwd();
    
    printf("Enter the password: \n");
    scanf("%s", buffer); 
  //   printf("%s\n", buffer);
  // printf("%p\n", buffer);
  // printf("%p\n", password);
  // printf("%s\n", password);
    if (strncmp(buffer, password, 4) == 0) {
      printf("Success!\n");
    }
    else {
      printf("FAIL!\n");
    }
    free(password);
}