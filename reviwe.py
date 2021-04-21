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

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('字數小於100的資料共有', len(new), '筆')