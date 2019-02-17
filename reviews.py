data = []
count = 0
with open('amazonreviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 100000 == 0:
			print(len(data)) #隨時顯示讀取進度

print (len(data))

print (data[136453])
print ('------------------') #視覺分隔線
print (data[234])
