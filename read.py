data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		# count % 1000 == 0:
			#print(len(data))

#print(len(data))

wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])


while True:
	t = input('請輸入您想找的名詞: ')
	if t == 'q':
		break
	if t in wc:
		print(t, '出現的次數為', wc[t], '次')
	else:
		print('沒有這個字')