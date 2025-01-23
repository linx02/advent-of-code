#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../utils.h"

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define WHITESPACE_COUNT 3
#define DIGITS_PER_NUMBER 5

void to_arrays(int *left, int *right, char *input);
size_t count_lines(char *input);
int ascending(const void *num1, const void *num2);
int sum_array(int *arr, size_t length);

int main() {

    char *input = read_input("day_1.txt");
    size_t line_count = count_lines(input);

    int left[line_count], right[line_count];

    to_arrays(left, right, input);

    qsort(left, line_count, sizeof(int), ascending);
    qsort(right, line_count, sizeof(int), ascending);

    int distances[line_count];

    for (size_t i = 0; i < line_count; i++) {
        distances[i] = MAX(abs(left[i] - right[i]), abs(right[i] - left[i]));
    }

    int sum = sum_array(distances, line_count);

    int similarity_score = 0;
    int c = 0;

    for (size_t i = 0; i < line_count; i++){
        c = 0;
        for(;;){
            if (c == line_count) {
                break;
            }
            if (left[i] == right[c]){
                similarity_score += left[i];
            }
            c++;
        }
    }

    printf("Day 1\n");
    printf("Part 1: %d\n", sum);
    printf("Part 1: %d\n", similarity_score);

    return 0;
}

void to_arrays(int *left, int *right, char *input) {
    size_t length = strlen(input);

    size_t pointer = 0;
    size_t index = 0;
    for (;;){
        if (pointer >= length){
            break;
        }
        left[index] = atoi(&input[pointer]);
        pointer += DIGITS_PER_NUMBER;
        pointer += WHITESPACE_COUNT;
        right[index] = atoi(&input[pointer]);
        pointer += DIGITS_PER_NUMBER;
        pointer += 1;
        index++;
    }
}

size_t count_lines(char *input) {
    int count = 0;
    int length = strlen(input);
    for (size_t i = 0; i < length; i++){
        if (input[i] == '\n') {
            count++;
        }
    }
    return count + 1;
}

int ascending(const void *num1, const void *num2){
    int int_num1 = *(const int *)num1;
    int int_num2 = *(const int *)num2;
    return (int_num1 - int_num2);
}

int sum_array(int *arr, size_t length){
    int sum = 0;
    for (size_t i = 0; i < length; i++){
        sum += arr[i];
    }
    return sum;
}