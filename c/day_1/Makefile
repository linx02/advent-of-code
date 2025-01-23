# Compiler and flags
CC = gcc
CFLAGS = -Wall -g

# Paths
UTIL = ../utils.c
UTIL_H = ../utils.h

# Targets
TARGET = day_1
SRCS = day_1.c $(UTIL)

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRCS)

clean:
	rm -f $(TARGET)