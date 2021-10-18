import count_letters as cl
#from count_letters import *

if __name__ == '__main__':
    sentence = input("Irj be egy mondatot: ")
    counts = cl.count_letters(sentence)
    for letter in counts:
        print(letter, 'x'*counts[letter])
