data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完畢,共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
avg_len = sum_len / len(data)
print('每筆留言平均長度為', avg_len)

new = [d for d in data if len(d) > 100]
print('字數小於100的資料共有', len(new), '筆')

good = [d for d in data if 'good' in d]
print('好評筆數共有', len(good))

#文字計數
wc = {} #word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增key

for word in wc:
	if wc[word] > 100000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請輸入關鍵字:')
	if word = 'q':
		break
	if word in wc:
		print(word, '的出現次數為:', wc[word])
	else:
		print('沒有這個字')


print('感謝查詢')





