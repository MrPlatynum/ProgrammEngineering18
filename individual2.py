#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
import string


def clean_text(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")
    words = text.lower().split()
    return words


def most_common_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = clean_text(text)
            word_counts = Counter(words)
            most_common = word_counts.most_common(1)
            return most_common
    except FileNotFoundError:
        print("Файл не найден.")


if __name__ == "__main__":
    filename = input("Введите имя файла: ")
    most_common_word = most_common_words(filename)
    if most_common_word:
        print(f"Самое часто встречающееся слово: {most_common_word[0][0]}")
    else:
        print("В файле нет текста.")
