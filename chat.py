# 讀取檔案
def read_file(filename):
	with open(filename, 'r', encoding='utf-8-sig') as f:
		lines = []
		for line in f:
			lines.append(line.strip())
	return lines

# 對話紀錄重新編輯
def convert(lines):
	person = None 
	new = []
	for line in lines:
		if line == 'Allen':
			person = line
			continue # 跳到下一個迴圈的意思
					 # 不是「繼續進行下一個判定」喔！
		elif line == 'Tom':
			person = line
			continue
		if person: # 有沒有想過，在lines中的第一個line不是人名呢(以這個例子來說，就是不是'Allen'或'Tom')
				   # 以這個例子來說，如果刪掉Allen，第一個line就會是'哈囉'
				   # 前面兩個if都判定為false之後，會進入下面這個new.append(person + ': ' + line)
				   # 可是前面的兩個if都判定為false，就不會有認和東西指派給person，就代表person是沒有辦宣告過的變數，程式就會報錯
				   # 所以很簡單就在func最開頭，直接做一個宣告，我宣告person為「無(None)」，一樣有宣告只是是虛無
				   # 這邊的if 就是說，如果person有值(True)，就會執行下面的new.append(person + ': ' + line)
			new.append(person + ': ' + line)
	return new

# 寫入新的檔案
def write(filename, lines):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

# 設立程式的主要進入點 main
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write('output.txt', lines)

main()