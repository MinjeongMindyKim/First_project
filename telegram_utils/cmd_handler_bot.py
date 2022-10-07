

import requests
import telegram

# (1) 환율정보 함수 만들기 [def 함수]

from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/marketindex/exchangeList.naver'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
results = soup.select('tbody > tr')
country_dic = {}
for result in results:
    title = result.select_one('.tit').text.strip().split(' ')
    country_dic.setdefault(title[0],title[1])

    
def 환율(country =''):
    URL = 'https://finance.naver.com/marketindex/exchangeList.naver'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.select('tbody > tr')
    final_result = {}
    result1 = soup.select('.tit')
    result2 = soup.select('.sale')

    for result in results:
        #tbody > tr 검색한 것이 통화량 환율 등 한 행이니까 반복문을 돌리고 있음
        #한 행별로 tit sale을 검색한다.(select_one 사용)
        title = result.select_one('.tit').text.strip()
        sale = result.select_one('.sale').text.strip()

        temp = {
            '통화명': title.split(),
            '환율': sale
        }

        final_result.setdefault(title.split()[0], sale) #딕셔너리로 만들어라!!! 키는 타이틀 스플릿해서 앞에것만 가져오라, 밸류는 sale 넣어라 (split)
        # {미국 : 1393.00, 유럽연합 : 1389.87} #정리한 다음에 미국, 유럽연합으로 함수의 인자(파라미터)를 받아라
    if country == '':
        return final_result
    else:
        return final_result[country]

from datetime import datetime
def url(country):
    url1 ='https://ssl.pstatic.net/imgfinance/chart/marketindex/area/month3/FX_'
    url2 = 'KRW.png?'
    today = datetime.today()
    sidcode= int(today.strftime('%Y%m%d'))

    img_url = url1 +country_dic[country] +url2+str(sidcode) ##datetime
    # chat_id = telegram_config['chatId']

    return img_url #텔레그램 이미지(그래프) 보내주는 코드다

# (2) 축제정보 함수 만들기 [def 함수]

def 축제(country, festa_date):
    datetime3 = datetime.strptime(festa_date, '%Y.%m.%d')

    headers= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    BASE_URL = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bk5C&qvt=0'
    parameters = '&query=' + country + ' 축제'

    URL = BASE_URL + parameters
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    final_result2 = []
    
    #행을 나누기
    festival = soup.select('.scroll tr')
    festival_list = festival[1:]
    # print(festival_list)
    for result in festival_list:
        result_title = result.select('td')[0].text
        result_time = result.select('td')[1].text
        result_place = result.select('td')[2].text

        temp = {
            '축제명': result_title,
            '기간(현지기준)': result_time,
            '장소' : result_place
        }
    
        try:
            travel_list2 = result_time.split('~')
            temp2 = travel_list2[0].split('.')[0].strip() + '.' + travel_list2[1].strip()
            start_date = datetime.strptime(travel_list2[0].strip(), '%Y.%m.%d.')
            final_date = datetime.strptime(temp2.strip(), '%Y.%m.%d.')
            result_time =travel_list2[0] + '~ ' + temp2

            if start_date < datetime3 < final_date:
                print('축제기간 맞음')
                final_result2.append(temp)

            # print(start_date)
            # print(final_date)
        except:
            pass

    message = ''
    for i in final_result2: #딕셔너리i
        # print(i['축제명'])
        # print(i['기간(현지기준)'])
        # print(i['장소'])
        
        message += i['축제명'] + i['기간(현지기준)'] + i['장소'] + '\n'
    
        #딕셔너리에서 축제명, 기간, 장소로 (key)로 접근해서 값을 가져와라.
    
    return message

#cmd_handler_bot.py
from telegram.ext import Updater
from telegram.ext import CommandHandler
 
BOT_TOKEN='5782216675:AAH9FsDNrxOtRcsj-2ux63aoeQ55tbCwl0Q'
 
updater = Updater( token=BOT_TOKEN, use_context=True )
dispatcher = updater.dispatcher
 

def 나라_환율(update, context):
    country = 환율(context.args[0])
    url_cou = url(context.args[0])
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=url_cou, caption="[{}] 현재 환율: ".format( context.args[0] ) + country, reply_markup={
        "inline_keyboard": [
                            [
                                {"text": "더 자세한 환율정보를 보시려면 클릭", "url" : 'https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_'+country_dic[context.args[0]]+'KRW#' }
                            ]
                        ]})

 
def 나라_축제(update, context):
    message = 축제(context.args[0], context.args[1])
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
 
    
 
money_handler = CommandHandler('money', 나라_환율)
festa_handler = CommandHandler('festa', 나라_축제)
 
dispatcher.add_handler(money_handler)
dispatcher.add_handler(festa_handler)
 
updater.start_polling()
updater.idle()