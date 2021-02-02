// Author: tyros77
// Simple hex dump completed as a school project

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 16

int main(int argc, char **filename)
{
    FILE *openFile;
    char entry[20];
    char temp[17];
    int count = 0, row, index = 0;
 
    openFile = fopen(filename[1], "r");
    if(openFile == NULL)
    {
        fprintf(stderr, "Could not open file %s.\n", filename[1]);
        exit(1);
    }
    printf("Offset\t Hexadecimal data format\t\t\t\t Character Format\n");
    while(fread(temp, 1, 16, openFile) != 0) 
    {
        printf("%05X\t ", count); //prints the offset for each loop through

        for(row = 0; row < SIZE; row++)
        {
            if(temp[row] < 33)
            {
            temp[row] = '.';
            }
        }
        for(row = 0; row < SIZE; row++)
        {
            printf("%X ", temp[row]);
        }
        printf("\t %s\n", temp);
      
        count = count +16; 
        
        for(row = 0; row < SIZE; row++)  
        {                               
            temp[row] = 0;              
        }
    }

    fclose(openFile);

    return 0;
}
