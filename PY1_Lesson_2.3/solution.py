import json
import chardet


def code_detecter(filename):
    with open(filename, 'rb') as codefile:
        data = codefile.read()
    
    return chardet.detect(data)['encoding']

def ten_words_from_news(country_news):

    Words = {}
    
    with open(country_news, encoding=code_detecter(country_news)) as news:
    
        for news in json.load(news)['rss']['channel']['item']:
            
            if country_news == 'newsit.json':
                news_list = news['description'].split()
            else:
                news_list = news['description']['__cdata'].split()
    
            for word in news_list:
    
                f = True
    
                for letter in word:
    
                    if letter in '<>/.,' :
    
                        f = False
    
                if f == True and len(word)>5:
    
                    if word in Words.keys():
    
                        Words[word] += 1
    
                    else:
    
                        Words[word] = 1
    
    Words = sorted(Words.items(), key=lambda x:x[1], reverse = True)
    
    
    for top_word in Words[:10]:
    
        print(top_word[0], top_word[1])

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
