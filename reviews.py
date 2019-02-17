data = []
count = 0
with open('amazonreviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 100000 == 0:
			print(len(data)) #隨時顯示讀取進度

print ('檔案讀取完了,總共有: ', len(data), '筆資料')

print (data[0])
print ('------------------') #視覺分隔線
print (data[1])

#以下算留言平均長度

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('每筆留言平均長度是', sum_len / len(data))

#以下是作篩選

new = [] #新清單，篩選出長度短於100字的留言
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),'筆資料字數短於100')
