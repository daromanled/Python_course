import json
import chardet
import re

def code_detecter(filename):
    with open(filename, 'rb') as codefile:
        data = codefile.read()
    
    return chardet.detect(data)['encoding']

def ten_words_from_news(country_news):

    Words = {}
    
    with open(country_news, encoding=code_detecter(country_news)) as news:
        for news in json.load(news)['rss']['channel']['item']:
            
            if country_news == 'newsit.json':
                news_list = re.sub(r'<[^>]+>', '', news['description']) 
            else:
                news_list = re.sub(r'<[^>]+>', '', news['description']['__cdata']) 
            
            news_list = re.split(r'\W+', news_list)
    
            for word in news_list:               
                if len(word)>5:
    
                    if word in Words.keys():
                        Words[word] += 1
                    else:
                        Words[word] = 1
        print_words(Words)
    
def print_words(Words):    
    Words = sorted(Words.items(), key=lambda x:x[1], reverse = True)
    
    for top_word in Words[:10]:
        print(top_word[0], top_word[1])
        
def input_country():

    country = input('Введите страну, топ слов из новостей которой вам нужен:')
    
    if country == 'France' or country == 'Франция':
        ten_words_from_news('newsfr.json')
    elif country == 'Cypr' or country == 'Кипр':
        ten_words_from_news('newscy.json')
    elif country == 'Italy' or country == 'Италия':
        ten_words_from_news('newsit.json')
    elif country == 'Africa' or country == 'Африка':
        ten_words_from_news('newsafr.json')
    else:
        print('Sorry, we have not got any information about this country')
        
input_country()
