# Написать программу, которая считывает текст из файла и определяет, сколько в нем слов, состоящих из не менее чем семи букв.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_long_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            long_words_count = sum(1 for word in words if len(word) >= 7)
            return long_words_count
    except FileNotFoundError:
        print("Файл не найден.")


if __name__ == "__main__":
    filename = input("Введите имя файла: ")
    count = count_long_words(filename)
    if count is not None:
        print(f"Количество слов из более чем семи букв: {count}")
