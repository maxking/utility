import sys
from sys import argv

def main():
    dct = open('DictionaryE.txt')
    dict_lines = dct.readlines()
    dict_words = []
    for dict_line in dict_lines:
        dict_words.extend(dict_line.split())
    f = open(sys.argv[1])
    lines = f.readlines()
    words = []
    for line in lines:
        words.extend(line.split())
    for word in words:
        word = word.lower()
        word = ''.join(w for w in word if w.isalpha() )
        for dict_word in dict_words:
            if(word == dict_word):
                break
            if(word != dict_word):
                pass
        
        if(word != dict_word):
            print word


if __name__ == '__main__':
    main()

