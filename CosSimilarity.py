from collections import Counter
import math
import jieba
class CosSimilarity:
    #构造函数
    def __init__(self, data, userdict=None):
        self.data = data
        self.cutted_data = []                         
        self.userdict = userdict
    #统计每篇的词频
    def analyze(self):
        if self.userdict:
            jieba.load_userdict(self.userdict)
        for article in self.data:                     
            c = Counter()                              
            for word in jieba.cut(article):             
                #stayed_line=""
                c[word] += 1
            self.cutted_data.append(c)               
        for i in self.cutted_data:
           print(i)
    #统计文章的关键字，依据TF * IDF的值排序
    def keywords(self, article, num=5):
        word_counter = Counter()
        for word in jieba.cut(article): 
            word_counter[word] += 1                     
        word_num = sum(word_counter.values())           
        tfidf = []
        for key, value in word_counter.items():
            tf = value / word_num                       
            c = 1                                       
            for article in self.cutted_data:          
                if key in article:
                    c += 1
            idf = math.log(len(self.cutted_data) / c)         
            tfidf.append((key, tf * idf))                       
            tfidf.sort(key=lambda x: x[1], reverse=True)        
        return [x[0] for x in tfidf[:num]]
    #求两个文章的相似程度
    def similarity(self, a, article, similarity):
        similarity = []
        word_counter = Counter()
        for word in jieba.cut(article):
            word_counter[word] += 1
        for i in range(len(self.cutted_data)):                                            
            words = set(word_counter.keys()).union(self.cutted_data[i].keys())            
            numerator, denominator = 0, 0                                                   
            d1, d2 = 0, 0                                      
            for word in words:                                                              
                numerator += word_counter[word] * self.cutted_data[i][word]
                d1 += word_counter[word]**2
                d2 += self.cutted_data[i][word]**2
                denominator = d1 * d2
                denominator = denominator ** 0.5          
            if numerator / denominator > 0:
                similarity.append((a[self.data[i]], numerator / denominator))
            similarity.sort(key=lambda x: x[1], reverse=True)
        return similarity