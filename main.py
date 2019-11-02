import CosSimilarity
import sys
import os
print('----------------------------简易搜索引擎-----------------------------------------')
print('                           计算机16-2班\n                                          ')
print('                            姓名：叶谈\n                                         ')
print('                         学号:1610410219\n                                          ')
print('')
print('')
print('')
print('--------------------------------------------------------------------------------')
print('                         python爬虫所得的各文本目录                        ')
print('********************************************************************************')
print('')
print('')
data=[]
a={}
txt=''
path =  os.listdir('spyder_data')
num = 1
adjust = ''
for file in path:
	fp = 'spyder_data' + '/' + file	
	print(num, ':', file)
	f = open(fp, 'rb');
	txt = f.read();
	data.append(txt)
	a[txt] = file;
	num += 1
print('')
print('**********************************************************************************')
print('按任意键进行词频统计：','\t')
while (1):
	t = input()
	if(t):break
t = CosSimilarity.CosSimilarity(data, userdict=None) 
t.analyze() 
print('')
print('*************************词频统计完成！！！*************************************')
print('')
print('')
while 1:
	print('请输入要搜索的内容（按0退出系统）:')
	article = input();
	if article == '0': break
	print('关键字:', t.keywords(article, num=3)) 
	similarity = 0
	cos = t.similarity(a, article, similarity)
	num = 1
	print('********************************搜索结果************************************')	
	for i in cos:
		print('')
		print(num, ':', i[0],'\t\t','相似度值:', i[1])
		num += 1
		if num == 6: break
	print('********************************搜索完成*************************************')
	print('')
	print('')
	print('')
	print('')
	print('')
print('')
print('**************************感谢您的支持，欢迎下次使用！******************************')