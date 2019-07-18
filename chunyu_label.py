import numpy as np

'''
sample_sentences = np.load('sample_sentences.npy')
sample_sentences = sample_sentences.tolist()
for sentence in sample_sentences:
    print(sentence)

with open("chunyu_sample100_sentences.txt", 'w', encoding='UTF-8') as f:
    for sentence in sample_sentences:
        for word in sentence:
            f.write(word)
            f.write('\n')
f.close()
'''

'''
replace_dict = {'O': 'O', 'T-B': 'TREATMENT-B', 'T-I': 'TREATMENT-I', 'B-B': 'BODY-B', 'B-I': 'BODY-I', 'S-B': 'SIGNS-B',
                'S-I': 'SIGNS-I', 'C-B': 'CHECK-B', 'C-I': 'CHECK-I', 'D-B': 'DISEASE-B', 'D-I': 'DISEASE-I'}
word_list = []
label_list = []
with open('chunyu_sample100_sentences.txt', 'r', encoding='UTF-8') as f:
    word_label_list = f.readlines()
    for word_label in word_label_list:
        word = word_label.split('\t')[0]
        label = word_label.split('\t')[1]
        label = label.strip()
        label = replace_dict[label]
        word_list.append(word)
        label_list.append(label)
f.close()

print(len(word_list) == len(label_list))

with open('chunyu_sample100_labeled_sentences.txt', 'w', encoding='UTF-8') as f:
    for i in range(len(word_list)):
        word = word_list[i]
        label = label_list[i]
        f.write(word)
        f.write('\t')
        f.write(label)
        f.write('\n')
f.close()
'''

text = ''
with open('chunyu_sample100_labeled_sentences.txt', 'r', encoding='UTF-8') as f:
    word_label_list = f.readlines()
    for word_label in word_label_list:
        word = word_label[0]
        text += word
f.close()

with open('text.txt', 'w', encoding='UTF-8') as f:
    f.write(text)
f.close()