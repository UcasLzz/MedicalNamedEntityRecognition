
with open("data/train.txt", 'r', encoding='UTF-8') as f:
    word_list = f.readlines()
    text_list = []
    for word in word_list:
        text_list.append(word[0])
    text = ''.join(text_list)
print(text)
f.close()
sentence_list = text.split('。')
print(sentence_list)
for sentence in sentence_list:
    if '心电图' in sentence:
        print(sentence)