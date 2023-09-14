#include <stdio.h>
#include <string.h>
 
int main(int argc, char *argv[]) {
    char buffer [8]; 
    char shifted_password[8] = "deez";
    
    printf("Enter the password: \n");
    scanf("%s", buffer); 
    for (int i = 0; i < 4; i++){
      buffer[i] -= 1;
    }
    if (strcmp(buffer, shifted_password) == 0) {
      printf("Success!\n");
    }
    else {
      printf("FAIL!\n");
    }
  
}