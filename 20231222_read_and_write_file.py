# read & write file
import os # 載入作業系統

# 讀取檔案
products = []
if os.path.isfile('products.csv'): # 檢查檔案是否存在
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續，跳過這一次的迴圈
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案！')

# 輸入商品,價格清單
while True:
	name = input('請輸入商品名稱(輸入q離開)：')
	if name == 'q': # 輸入q離開(quit)
		break
	price = input('請輸入商品價格：')
	products.append([name, price]) # 存每個品項+價格

# 印出商品價格
for item in products:
	print(item[0], '的價格是', item[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: # 打開檔案，並使用UTF-8的編碼
	f.write('商品,價格\n') # 增加標題列
	for item in products:
		f.write(item[0] + ',' + item[1] + '\n') # f.write將內容寫入，加上','是為了分隔內容
