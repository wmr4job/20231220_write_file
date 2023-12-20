# write file

products = []

while True:
	name = input('請輸入商品名稱(輸入q離開)：')
	if name == 'q': # 輸入q離開(quit)
		break
	price = input('請輸入商品價格：')

	products.append([name, price]) # 存每個品項+價格

for item in products:
	print(item[0], '的價格是', item[1])

with open('products.csv','w') as f: # 打開檔案，如沒有這個檔案就會建立檔案
	for item in products:
		f.write(item[0] + ',' + item[1] + '\n') # f.write將內容寫入，加上','是為了分隔內容
