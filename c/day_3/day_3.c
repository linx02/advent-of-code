#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../utils.h"

size_t numlen(int num);

int main (){

    char *input = read_input("day_3.txt");
    int part1 = 0;
    int part2 = 0;

    size_t i = 0;
    size_t input_length = strlen(input);

    int do_ = 0;

    while(i < input_length){
        if (input_length - i > 7){
            char buffer_do[5];
            char buffer_dont[8];
            for(size_t j = 0; j < 4; j++) buffer_do[j] = input[i + j];
            for(size_t j = 0; j < 7; j++) buffer_dont[j] = input[i + j];

            if (strcmp(buffer_do, "do()") == 0){
                do_ = 0;
            }
            if (strcmp(buffer_dont, "don't()") == 0){
                do_ = -1;
            }
        }
        if (input[i] == ','){
            if (i > 3){
                size_t next_p_l = 0;
                size_t j = i;

                while (1){
                    if (i - j > 4) break;
                    if (input[j] == '('){
                        next_p_l = i - j;
                        break;
                    }
                    j--;
                }

                if (next_p_l != 0){
                    int left = atoi(&input[i - next_p_l + 1]);
                    int right = atoi(&input[i + 1]);

                    size_t len_l = numlen(left);
                    size_t len_r = numlen(right);

                    if (
                        input[i + len_r + 1] == ')' &&
                        input[i - len_l - 1] == '(' &&
                        input[i - len_l - 2] == 'l' &&
                        input[i - len_l - 3] == 'u' &&
                        input[i - len_l - 4] == 'm'
                    ) {
                        part1 += left * right;
                        if (do_ == 0) part2 += left * right;
                    }

                }
            }
        }
        i++;
    }

    printf("Day 3\n");
    printf("Part 1: %d\n", part1);
    printf("Part 2: %d\n", part2);

    return 0;
}

size_t numlen(int num){
    char buffer[10];
    snprintf(buffer, sizeof(buffer), "%d", num);
    return strlen(buffer);
}