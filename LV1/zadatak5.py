ham_count = 0
ham_words = 0
spam_count = 0
spam_words = 0
exclamation_count = 0

with open('SMSSpamCollection.txt') as file:
    for line in file:
        line = line.rstrip()
        words = line.strip().split()
        if words[0] == 'ham':
            ham_count += 1
            ham_words += len(words) - 1
        else:
            spam_count += 1
            spam_words += len(words) - 1
            if line.endswith("!"):
                exclamation_count += 1


print(f"Prosječan broj riječi u porukama koje su tipa ham: {ham_words/ham_count}")
print(f"Prosječan broj riječi u porukama koje su tipa spam: {spam_words/spam_count}")
print(f"Od {spam_count} SMS poruka koje su tipa spam, {exclamation_count} završava uskličnikom.")
