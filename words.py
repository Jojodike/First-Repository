# list of words from the dictionary 
words = []
with open('/usr/share/dict/words') as f:
    for line in f:
        words.append(line.strip())