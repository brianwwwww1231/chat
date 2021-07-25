# 讀取檔案
def read_file(filename):
	with open(filename, 'r', encoding='utf-8-sig') as f:
		lines = []
		for line in f:
			lines.append(line.strip())
	return lines


# 對話紀錄字數、圖片、貼圖計算
def convert(lines):
	person = None 
	allen_word_count = 0
	allen_sticker_count = 0
	allen_picture_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_picture_count = 0

	for line in lines:
		s = line.split(' ')
		# new.append(line.strip(' ')) vs. s = line.strip(' ')
		# new我們宣告他是個list[] -> new.append(line.strip(' ')) -> [ [], [], [] ]
		# s呢？ -> for迴圈裡把line(時間+人名+對話內容)重lines一行一行抓出來 -> 並且print出來 -> 進入下一個迴圈
		time = s[0] # s[0]都是時間，把他抓出來存著
		name = s[1] # s[1]都是人名，把他抓出來存著
					# 最容易卡的地方就是這邊，要做什麼事情，要記得創(宣告)一個變數來乘載
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_picture_count += 1
			else:
				for msg in s[2:]:
					allen_word_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_picture_count += 1
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)
	print('Allen說了', allen_word_count, '個字')
	print('Allen用了', allen_sticker_count, '張貼圖')
	print('Allen用了', allen_picture_count, '張圖片')
	print('Viki說了', viki_word_count, '個字')
	print('Viki用了', viki_sticker_count, '張貼圖')
	print('Viki用了', viki_picture_count, '張圖片')


# 寫入新的檔案
def write(filename, lines):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

# 設立程式的主要進入點 main
def main():
	lines = read_file('LINE-Viki.txt')
	convert(lines)
	# write('output.txt', lines)

main()