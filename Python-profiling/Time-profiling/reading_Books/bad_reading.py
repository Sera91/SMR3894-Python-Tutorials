#!/bin/python
import cProfile

def read_file(name: str) -> list:
    with open(name,'r') as file:
        titles = file.readlines()
    
    new_titles = []
    # casting off \n from end of titles
    for title in titles:
        new_titles.append(title.removesuffix('\n'))
    
    return new_titles


def ignore_duplicates(titles: list) -> list:
    new_titles = []
    for title in titles:
        if title in new_titles:
            continue
        else:
            new_titles.append(title)
    
    return new_titles

def main() -> None:
    original_titles = read_file('list_files.txt')
    safe_titles = ignore_duplicates(original_titles)
    print(safe_titles)

if __name__ == '__main__':
    cProfile.run('main()', sort='ncalls')

