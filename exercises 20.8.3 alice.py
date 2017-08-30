
alice = open('alice_in_wonderland.txt', 'r')


count = {}

for txt in alice:
    for word in txt.split():
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", '')
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')
        word = word.lower()

        if word.isalpha():
            if word in count:
                count[word] += 1
            else:
                count[word] = 1


key = sorted(count.keys())


alicewords = open('alice_words.txt', 'w')

for word in key:
    alicewords.write(word +'   ' + str(count[word]))# Lam the nao de thang hang tung cot ?
    alicewords.write('\n')

noofalice = count['alice']

print("The word 'alice' appears " + str(count['alice']) + " times in the book.")
