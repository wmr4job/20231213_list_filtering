#清單篩選→進階語法

data = []
sum_len = 0

with open('C:\\Users\\dgw\\Desktop\\github\\20231211_reviews_analytics\\reviews.txt', 'r') as f: #讀取reviews檔
	for line in f:
		data.append(len(line))
		sum_len += len(line)

average = sum_len / len(data)

print('每筆留言平均長度：', average)


#篩選留言字串長度小於100的留言
filtering =[]
for d in data:
	if len(d) < 100:
		filtering.append(d)

# filtering = [d for d in data if len(d) < 100]

print('共有', len(filtering), '筆資料長度小於100')


#篩選有good的留言
good = []
for d in data:
	if 'good' in d: 
		good.append(d)

# good =[d for d in data if 'good' in d]

print('共有', len(good), '筆資料中有good')