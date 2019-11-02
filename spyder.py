#爬虫代码
import requests
from lxml import etree
#获取想要爬取的urls
urls=['http://www.gs5000.cn/gs/huangdi/shanggu/{}.html'.format(i) for  i  in range(23820,23855)]
for url in urls:
    print(url)
#设置保存文本的路径
path = r'D:\python3-workplace\spyder_data\  '
#获取网页内容
def get_text(url):
    r=requests.get(url)
    r.encoding='utf-8'
    selector = etree.HTML(r.text)
    #获取文章标题   
    title = selector.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/h2/text()')
    print(title)
    #获取文章内容
    text = selector.xpath('/html/body/div[3]/div[1]/div[2]/div[3]/table[1]/tbody/tr/td/text()')  
    print(text)
    #print(path+title[0])
    with open( path + title[0],'w',encoding='utf-8') as f:
        for i in text:
            f.write(i)
if __name__=='__main__':
    for url in urls:
        get_text(url)