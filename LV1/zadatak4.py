words = {}
with open('song.txt') as file:
    for line in file:
        line = line.strip().lower()
        for word in line.split():
            words[word] = words.get(word, 0) + 1

count = 0
for word in words:
    if words[word] == 1:
        print(word)
        count += 1

print(f'Broj riječi koji se samo jednom pojavljuje: {count}')
