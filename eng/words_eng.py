import os
from datetime import date

'''get the day'''
today = date.today()
month_day = today.strftime("%m_%d")
path_folder = "words_eng"
path_file = f"/{month_day}.txt"

'''functionality'''
print("hey! new day to learn new words :)")
try:
    while True:
        '''input of the word'''
        word = input("+++ word/phrase: ")
        if len(word) == 0:
            '''empty file'''
            if not os.path.exists(path_folder+path_file):
                print("no words in file.")
                continue
            else:
                '''print the file first'''
                with open(path_folder+path_file, 'r')as f:
                    words = f.readlines()
                for i,word in enumerate(words):
                    word = word.split("\t")[0]
                    print('\t', i, word)
                line_index = input("--- line operaton:")
                '''modify'''
                word = input("--- new word:")
                meaning = input("--- new meaning:")
                words[i] = f"{word}\t{meaning}\n"
                with open(path_folder+path_file, 'w')as f:
                    words = f.writelines(words)
        else:
            '''input of the meaning'''
            meaning = input("+++ meaning: ")
            words = (word, meaning)
            '''write'''
            output = "\t".join(map(str,words))
            if not os.path.exists(path_folder):
                os.makedirs(path_folder)
            with open(path_folder+path_file,'a') as f:
                f.write(output+"\n")
except KeyboardInterrupt:
    print("see ya.")