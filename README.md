# 여행정보 크롤링 Program✨🌏
## _환율과 축제를 중심으로 구성
![python badge](https://img.shields.io/badge/python-v.3.7%2B-blue)
- Python v.3.7
- ✨MinJeongKim's   
- 전세계의 환율 정보와 축제 정보를 한 눈에 보고 여행을 편리하게 계획할 수 있는 라이브러리

## 모듈 설명

- A program to crawling travel information
- Crawling exchange rates and festival information 
- Modules exchange rates : 최근 3개월의 전세계 환율을 측정할 수 있는 모듈입니다.
- Modules festival information : 원하는 날짜에 진행되는 해외 축제 리스트를 한 눈에 볼 수 있는 모듈입니다.
- 사용모듈: datetime, requests, telegram
- Use python 3

## 사이트
1. [NAVER 환율] [https://finance.naver.com/marketindex/?tabSel=exchange#tab_section][df1]
2. [NAVER 해외 축제] [https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%95%B4%EC%99%B8+%EC%B6%95%EC%A0%9C][df1]

> crawler/
  날씨 정보 크롤러. py
  축제 정보 크롤러. py

✨🌏✨🌏✨🌏

## ---__main__---

각 나라의 통화명 및 환율을 알아보는 함수

```sh
def 환율(country =''):
    URL = 'https://finance.naver.com/marketindex/exchangeList.naver'
    response = requests.get(URL)
```

각 나라의 기간별 축제 정보를 받아오는 함수

```sh
def 축제(country, festa_date):
    datetime3 = datetime.strptime(festa_date, '%Y.%m.%d')

    headers= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    BASE_URL = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bk5C&qvt=0'
    parameters = '&query=' + country + ' 축제'
```

## 구성요소


| 패키지 구조 | README |
| ------ | ------ |
| .git | [README.md][PlDb] |
| crawler | [README.md][PlGh] |
| datebase | [README.md][PlGd] |
| rpa | [README.md][PlMe] |
| telegram_utils | [README.md][PlGa] |
| etc | [README.md][PlGa] |

**USE THIS!  THANK YOU!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>


주제: 해외 여행, 언제 갈래? (여행정보 크롤링하는 프로그램)

목적: 나라별, 시즌별 축제 한 눈에 보기
목표: 여행 전 그 나라의 환율 & 축제 & 날씨정보를 알아보고 싶다면?
내 라이브러리를 추천함



1. PART 환율
(1) 환율정보 함수 만들기 [def 함수]
(2) 10년간 국제 시장 환율 변동 측정

2. PART 축제
(1) 축제정보 함수 만들기 [def 축제] -----현재 여기까지 진행중
(2) 나라이름 검색시 해당 나라의 축제 리스트 추출