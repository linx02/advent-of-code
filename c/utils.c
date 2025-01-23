#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utils.h"

#define MAX_PATH 1024

char* read_input(const char *file_name){
    char file_path[MAX_PATH];
    snprintf(file_path, sizeof(file_path), "../../input/%s", file_name);

    FILE *file = fopen(file_path, "r");
    if (file == NULL){
        perror("Error opening file");
        return NULL;
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    rewind(file);

    char *buffer = malloc(file_size + 1);
    if (buffer == NULL) {
        perror("Error allocating buffer");
        fclose(file);
        return NULL;
    }

    fread(buffer, 1, file_size, file);
    buffer[file_size] = '\0';

    fclose(file);

    return buffer;
}