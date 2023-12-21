# read & write file

products = []

#讀取上次的檔案
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		
		# way1
		# row = line.strip().split(',') 		
		# name = row[0] # 清單中第一個值是商品名稱
		# price = row[1] # 清單中第二個值是商品價格

		# Way2
		# strip()去除空隔空行； split()以逗號分割；用row儲存分割後的內容，row為清單list
		name, price = line.strip().split(',')
		
		products.append([name, price])

print(products)


while True:
	name = input('請輸入商品名稱(輸入q離開)：')
	if name == 'q': # 輸入q離開(quit)
		break
	price = input('請輸入商品價格：')

	products.append([name, price]) # 存每個品項+價格

for item in products:
	print(item[0], '的價格是', item[1])

with open('products.csv', 'w', encoding = 'utf-8') as f: # 打開檔案，並使用UTF-8的編碼
	f.write('商品,價格\n') # 增加標題列
	for item in products:
		f.write(item[0] + ',' + item[1] + '\n') # f.write將內容寫入，加上','是為了分隔內容
