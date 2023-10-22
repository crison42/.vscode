score = {'001': 96, '002': 98, '003': 92, '004': 93, '005': 94}
print(score)
score['006'] = 100
print(score)
score['002'] = 99
print(score)
del (score['001'])
print(score)
print(score['004'])
index=0
for i in score:
    if score[i]>index:
        index=score[i]
print(index)
for j in score:
        if score[j]<index:
            index=score[j]
print(index)
sum=0
for k in score:
        sum+=int(score[k])
print(sum/score.__len__())