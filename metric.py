import numpy as np

predict = np.load('predict.npy')
predict_list = predict.tolist()
#print(len(predict_list))
#print(predict_list)

label_list = []
with open('chunyu_sample100_labeled_sentences.txt', 'r', encoding='UTF-8') as f:
    string_list = f.readlines()
    for string in string_list:
        word = string.split('\t')[0]
        label = string.split('\t')[1].strip()
        label_list.append([word, label])
f.close()
label_list[0][0] = label_list[0][0][-1:]

predict_list = predict_list[1:]
label_list = label_list[:len(predict_list)]
print(predict_list)
print(label_list)


count = 0
label_count = 0
predict_count = 0

for label in label_list:
    if 'B' in label[1]:
        label_count += 1
print('标注出的实体共有', label_count, '个')
for predict in predict_list:
    if 'B' in predict[1]:
        predict_count += 1
print('预测出的实体共有', predict_count, '个')
for i in range(len(predict_list)):
    if label_list[i] == predict_list[i]:
        count += 1
print('一共100句话，共', len(label_list), '个字')
print('accuracy =', count / len(label_list))

new_label_list = []
for label in label_list:
    new_label_list.append(label[1])
new_predict_list = []
for predict in predict_list:
    new_predict_list.append(predict[1])


print(new_label_list)
print(new_predict_list)
new_label_list
new_predict_list
i = 0
correct_count = 0
while(i < len(new_label_list)):
    if 'B' in new_label_list[i]:
        start = i
        i += 1
        while('I' in new_label_list[i]):
            i += 1
        end = i
        if new_label_list[start: end] == new_predict_list[start: end]:
            #print(new_label_list[start: end])
            #print(label_list[start: end])
            #print(new_predict_list[start: end])
            correct_count += 1
    else:
        i += 1
print(correct_count)
Precision = correct_count / predict_count
Recall = correct_count / label_count
F1 = Precision * Recall * 2 / ( Precision + Recall)
print('Precision =', Precision)
print('Recall =', Recall)
print('F1 = ', F1)




