import json
import numpy as np
count = 0

sentence_list = []
sen_len_dis = {}
with open('all_labeled_dialogs.json', 'r', encoding='UTF-8') as f:
    text = json.load(f)
    for dialog in text:
        for document in dialog:
            sentence = document['utterance']
            length = len(sentence)
            if length in sen_len_dis:
                sen_len_dis[length] += 1
            else:
                sen_len_dis[length] = 1
            sentence_list.append(sentence)
            count += 1
f.close()

np.save('all_sentences.npy', sentence_list)

#print(sen_len_dis)
dist = sorted(sen_len_dis.items(), key=lambda sentence_length_distribution:sentence_length_distribution[1], reverse=True)
#print(dist)
#print(count)

with open("chunyu_sentence_length_distribution.txt", 'w', encoding='UTF-8') as f:
    f.write('句子长度')
    f.write('\t')
    f.write('句子个数')
    f.write('\t')
    f.write('所占比例')
    f.write('\n')
    for item in dist:
        f.write(str(item[0]))
        f.write('\t')
        f.write(str(item[1]))
        f.write('\t')
        f.write(str(item[1] / count))
        f.write('\n')
f.close()
