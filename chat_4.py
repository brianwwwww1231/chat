# 目標是要把對話紀錄的時間跟人名切開

# 先讀取資料後，把對話紀錄一行一行存進一個清單裡
lines = [] # 我們要把紀錄存進lines，要先宣告一個變數來裝，不然會報錯
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

# 接下來把對話紀錄給切割，用'( 空白鍵 )'
new = []
name = None
for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	text = ''
	for msg in s[1:]:
		text += msg
	print(text)
	if name:
		new.append(time + ' ' + name + ': ' + text)
print(new)	

with open('3_output.txt', 'w', encoding='utf-8-sig') as f:
	for line in new:
		f.write(line + '\n')