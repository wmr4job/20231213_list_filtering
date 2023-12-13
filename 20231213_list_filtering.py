#清單篩選→進階語法

data = [] #存放每筆留言
data_len = [] #每筆留言長度
sum_len = 0 #留言長度總和

with open('C:\\Users\\dgw\\Desktop\\github\\20231211_reviews_analytics\\reviews.txt', 'r') as f: #讀取reviews檔
	for line in f:
		data.append(line) #將每筆留言放進data的清單中
		data_len.append(len(line))
		sum_len += len(line)

average = sum_len / len(data_len)

print('每筆留言平均長度：', average)


#篩選留言字串長度小於100的留言
filtering =[]
for d in data:
	if len(d) < 100:
		filtering.append(d)

print('共有', len(filtering), '筆資料長度小於100')


#篩選有good的留言
good = []
for d in data:
	if 'good' in d: 
		good.append(d)

print('共有', len(good), '筆資料中有good')