#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../utils.h"

int test_safe(const int *arr, size_t length);
void get_file_size(const char *input, size_t *max_int_count, size_t *line_count);
void to_numbers(const char *input, int **output, size_t *row_lengths);

int main() {
    const char *input = read_input("day_2.txt");

    size_t line_count = 0;
    size_t max_int_count = 0;

    get_file_size(input, &max_int_count, &line_count);

    int **numbers = (int **)malloc(line_count * sizeof(int *));
    if (numbers == NULL) {
        fprintf(stderr, "Memory allocation failed for row pointers.\n");
        return 1;
    }
    for (size_t i = 0; i < line_count; i++) {
        numbers[i] = (int *)malloc(max_int_count * sizeof(int));
        if (numbers[i] == NULL) {
            fprintf(stderr, "Memory allocation failed for row %zu.\n", i);
            return 1;
        }
    }

    size_t row_lengths[line_count];
    to_numbers(input, numbers, row_lengths);

    size_t safe_reports_part1 = 0;
    size_t safe_reports_part2 = 0;

    for (size_t i = 0; i < line_count; i++) {
        if (test_safe(numbers[i], row_lengths[i]) == 0) {
            safe_reports_part1++;
            safe_reports_part2++;
            continue;
        }

        for (size_t j = 0; j < row_lengths[i]; j++) {
            int *expanded = (int *)malloc((row_lengths[i] - 1) * sizeof(int));
            if (expanded == NULL) {
                fprintf(stderr, "Memory allocation failed for expanded array.\n");
                return 1;
            }

            size_t index = 0;
            for (size_t k = 0; k < row_lengths[i]; k++) {
                if (k != j) {
                    expanded[index++] = numbers[i][k];
                }
            }

            if (test_safe(expanded, row_lengths[i] - 1) == 0) {
                safe_reports_part2++;
                free(expanded);
                break;
            }

            free(expanded);
        }
    }

    for (size_t i = 0; i < line_count; i++) {
        free(numbers[i]);
    }
    free(numbers);

    printf("Day 2\n");
    printf("Part 1: %zu\n", safe_reports_part1);
    printf("Part 2: %zu\n", safe_reports_part2);

    return 0;
}

void get_file_size(const char *input, size_t *max_int_count, size_t *line_count) {
    size_t i = 0;
    size_t cur_max_int = 0;

    while (1) {
        if (input[i] == '\0') {
            cur_max_int++;
            if (cur_max_int > *max_int_count) {
                *max_int_count = cur_max_int;
            }
            if (cur_max_int > 0) {
                (*line_count)++;
            }
            break;
        }

        if (input[i] == '\n') {
            cur_max_int++;
            if (cur_max_int > *max_int_count) {
                *max_int_count = cur_max_int;
            }
            cur_max_int = 0;
            (*line_count)++;
        }
        if (input[i] == ' ') {
            cur_max_int++;
        }

        i++;
    }
}

void to_numbers(const char *input, int **output, size_t *row_lengths) {
    size_t i = 0;
    size_t j = 0;
    size_t k = 0;

    while (input[i] != '\0') {
        if (input[i] == '\n') {
            row_lengths[j] = k;
            j++;
            k = 0;
        } else if (input[i] != ' ') {
            output[j][k] = atoi(&input[i]);
            k++;

            while (input[i] != ' ' && input[i] != '\n' && input[i] != '\0') {
                i++;
            }
            continue;
        }
        i++;
    }

    if (k > 0) {
        row_lengths[j] = k;
    }
}

int test_safe(const int *arr, size_t length) {
    int direction = (arr[0] < arr[1]) ? 1 : -1;

    for (size_t i = 0; i < length - 1; i++) {
        if (direction == 1) {
            if (arr[i] >= arr[i + 1] || arr[i + 1] - arr[i] > 3) {
                return -1;
            }
        } else {
            if (arr[i] <= arr[i + 1] || arr[i] - arr[i + 1] > 3) {
                return -1;
            }
        }
    }

    return 0;
}