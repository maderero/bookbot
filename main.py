import sys
import os
from pathlib import Path


def read_book(pth):
    with open(pth) as f:
        file_contents = f.read()

    return file_contents

def word_count(countable):
    count = len(countable.split())
    return count

def char_count(countable):
    count = {}
    for char in countable:
        char = char.lower()
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count        

def report(pth):
    short_path = '/'.join(pth.parts[-2:])
    print(f'--- Begin report of {short_path} ---')
    content = read_book(pth)
    count = word_count(content)
    print(f'{count} words found in the document\n')
    counts = char_count(content)
    counts = sort_dict(counts)
    for char, count in counts.items():
        message = f'''The {repr(char)} character was found {count} times'''
        print(message)
    print('--- End report ---')

def sort_dict(d):
    res = {key: d[key] for key in sorted(d, key=lambda key: d[key], reverse=True)}
    return res

def main():
    parent_pth = Path(__file__).parent
    book_pth = parent_pth / 'books' / 'frankenstein.txt'
    report(book_pth)


if __name__ == '__main__':
    main()