# author @15331094 https://github.com/15331094/wxImage
# @Jiamin learned and commented on 2017-03-19

import itchat
import os

import PIL.Image as Image
from os import listdir
import math

itchat.auto_login(enableCmdQR=2) #生成二维码 login 

friends = itchat.get_friends(update=True)[0:] #获取好友列表

user = friends[0]["UserName"] #本人

print(user)

os.mkdir(user) #新建文件夹

num = 0

for i in friends: #遍历每一个好友
	img = itchat.get_head_img(userName=i["UserName"]) #得到头像
	fileImage = open(user + "/" + str(num) + ".jpg",'wb') #新建
	fileImage.write(img) #写入
	fileImage.close()
	num += 1

pics = listdir(user) #returns a list containing the names of all files and directories in the given path "folder 'user' ".

numPic = len(pics)

print(numPic)

eachsize = int(math.sqrt(float(640 * 640) / numPic)) #计算每一张图片的边长（为最后生成640*640的图片）

print(eachsize)

numline = int(640 / eachsize) #行数

toImage = Image.new('RGBA', (640, 640)) #新建image


print(numline)

x = 0
y = 0

for i in pics:
	try:
		#打开图片
		img = Image.open(user + "/" + i)
	except IOError:
		print("Error: 没有找到文件或读取文件失败")
	else:
		#缩小图片
		img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
		#拼接图片
		toImage.paste(img, (x * eachsize, y * eachsize))
		x += 1
		if x == numline:
			x = 0
			y += 1


toImage.save(user + ".jpg")


itchat.send_image(user + ".jpg", 'filehelper') #发送给自己


