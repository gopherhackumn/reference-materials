#include <stdio.h>
#include <string.h>
 
int main(int argc, char *argv[]) {
    char buffer [8]; 
    char password[8] = "deez";
    
    printf("Enter the password: \n");
    scanf("%s", buffer); 
  
    if (strcmp(buffer, password) == 0) {
      printf("Success!\n");
    }
    else {
      printf("FAIL!\n");
    }
  
}