# 讀取檔案
with open('input.txt', 'r', encoding='utf-8-sig') as f:
	text = []
	for line in f:
		words = line.strip()
		text.append(words)
for x in text:
	if 'Allen' in x or 'Tom' in x:
		name = x
	else:
		print(name, ':', x)