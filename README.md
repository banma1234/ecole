# 🍎 Ecole Project Repository

에꼴프로젝트서 하는 모든 작업을 업로드 하는 레포지 입니다.

+ 주차별로 프로젝트 내용이 다릅니다.

<hr/>

## Used fucntion
+ Library & Frameworks

none.

+ with

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)


<hr/>

## Project members

#### `banma1234(박범수)`


<hr/>

### 1주차
* #### python 문제풀이
`python` 언어를 사용해 백준 문제풀이를 진행하였습니다.

### 2주차
* #### html & css를 활용한 자기소개 페이지
순수 `html`과 `css`만을 사용해 자신을 소개하는 간단한 페이지를 만들었습니다.

### 4주차
* #### Twitter 웹 크롤링 및 word 마이닝
`snscrape`, `wordCloud` 모듈을 사용하여 `twitter`에서 `특정 키워드`가 본문에 포함된 트윗을 크롤링, 핵심 키워드와 `함께 언급된 관련 단어`들을 분석, 해당 단어의 언급 빈도수에 따라 `시각화된 자료`를 생성하는 프로그램을 작성했습니다.

<hr/>

## 📌 4주차 : Web Crawling
### 🚗현대인을 위한 3줄요약.
>  `snscrape`, `wordCloud` 모듈을 사용하여 `twitter`에서 `특정 키워드`가 본문에 포함된 트윗을 크롤링, 핵심 키워드와 `함께 언급된 관련 단어`들을 분석, 해당 단어의 언급 빈도수에 따라 `시각화된 자료`를 생성하는 프로그램을 작성했습니다.

* ### 사용된 모듈
```python
# 데이터 처리 모듈
import pandas as pd

# 웹크롤링 관련모듈
import snscrape.modules.twitter as sntwitter
import itertools
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# wordCloud 모듈
from wordcloud import WordCloud
import matplotlib.pyplot as plt
```

<hr/>

### 👉 트윗 긁어오기
트윗을 긁어오기 위한 query 작성에는 다음과 같은 속성이 필요하다.
* 검색할 키워드, 
* 검색할 날짜 범위

각각 `search_word`, `start_day`, `end_day`에 저장한 후 쿼리를 작성한다.
```python
#검색하고 싶은 단어
search_word = "안녕"

#검색하는 기간
start_day = "2022-10-01"
end_day = "2022-10-14"

search_query = search_word + ' since:' + start_day + ' until:' + end_day 
```
이후 작성한 query문을 `scraped`모듈을 통해 처리해준다. 

`sliced_scrapped_tweets`의 파라미터로 트윗을 긁어올 명령과 긁어올 트윗의 개수를 전달한다.
```python
#지정한 기간에서 검색하고 싶은 단어를 포함한 tweet를 취득
scraped_tweets = sntwitter.TwitterSearchScraper(search_query).get_items()
#처음부터 1000개의 tweets를 취득
sliced_scraped_tweets = itertools.islice(scraped_tweets, 1000)
```

<hr/>

### 👉 데이터 전처리 & 정리
이제 긁어온 데이터를 사용하기 쉽게 정돈할 차례이다. `pandas DataFrame` 모듈을 이용해 긁어온 데이터를 `pandas` 형식으로 정리한다. 

그리고 해쉬태그/닉네임이 아닌 `본문`에 단어가 등록된 경우만을 위해 트윗의 `content` 라벨에 포함되어 있어야만 긁어오도록 하였다.

```python
#pandas DataFrame으로 변환
df = pd.DataFrame(sliced_scraped_tweets)
df = df[df['content'].str.contains('안녕|하이|반가워|안녕하세요')]
```
또한 트윗을 긁어올 때 필요없는 데이터는 미리 제거하기 위해 `stop_words`. 즉 `불용어`를 설정했다. 

영어의 경우 기본적인 불용어들이 제공되지만 한글은 그렇지 않으므로 본인이 직접 지정해줘야 한다. 
```python
stop_words = " ~~~한글 불용어들~~~ "
stop_words=stop_words.split(' ')
```
불용어 지정이 끝났다면 실제로 트윗에서 불용어들을 삭제해주는 함수를 작성할 차례이다.
```python
# 트위터분석을 위한 기본적인 텍스트 cleaning 함수
def CleanText(readData, Num=True, Eng=True):
    # Remove Retweets
    text = re.sub('RT @[\w_]+: ', '', readData)
    # Remove Mentions
    text = re.sub('@[\w_]+', '', text)
    # Remove or Replace URL
    text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", ' ',
                  text)  # http로 시작되는 url
    text = re.sub(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{2,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", ' ',
                  text)  # http로 시작되지 않는 url
    # Remove only hashtag simbol "#" because hashtag contains huge information
    text = re.sub(r'#', ' ', text)
    # Remove Garbage Words (ex. &lt, &gt, etc)
    text = re.sub('[&]+[a-z]+', ' ', text)
    # Remove Special Characters
    text = re.sub('[^0-9a-zA-Zㄱ-ㅎ가-힣]', ' ', text)
    # Remove 출처 by yamada
    text = re.sub(r"(출처.*)", ' ', text)
    # Remove newline
    text = text.replace('\n', ' ')

    if Num is True:
        # Remove Numbers
        text = re.sub(r'\d+', ' ', text)

    if Eng is True:
        # Remove English
        text = re.sub('[a-zA-Z]', ' ', text)

    # Remove multi spacing & Reform sentence
    text = ' '.join(text.split())

    return text
```
보면 알겠지만 온갖 정규표현식으로 짬뽕이 되 무척이나 알아보기 힘들다. 대충 다음과 같은 역할을 한다고 알고만 있으면 되겠다.
* `리트윗`, `멘션` 삭제
* `해쉬태그`, `URL` 삭제
* `쓰레기값`, `특수문자` 삭제
* `줄바꿈`, `출처` 삭제

또한 파라미터로 전달받은 `Num`, `Eng`이 `True`라면 해당하는 값(숫자, 알파벳)을 삭제해준다. 
```python
for tweet in df.content:
  cleaned_tweet = []
  # 한글 불용어 처리를 위해 Eng에 False값을 준다
  cleaned_tweet_string = CleanText(tweet, Num=True, Eng=False)
  tweet_tokens = word_tokenize(cleaned_tweet_string)
  for token in tweet_tokens:
    if token.lower() not in stop_words:
      cleaned_tweet.append(token)

  cleaned_tweets_all.append(cleaned_tweet)
```
마지막으로 트윗 하나하나를 다 불러와 불용어 제거 함수에 대입해준 후 시각화 자료 생성을 위해 `한줄의 string`으로 만들어 준다.

한글 단어를 분석할 예정이니 `Num`은 `True`, `Eng`은 `False`를 전달해준다.

이러한 과정들을 통틀어 `전처리 과정`이라고 한다.

<hr/>

### 👉 데이터 시각화
`데이터 시각화`란 JSON, pandas와 같이 한눈에 파악하기 힘든 형태의 데이터를 한눈에 알아보기 쉽게 가공하는 것을 뜻한다.

다양한 방법이 있지만 이번에는 `wordCloud` 모듈을 사용해 시각화 자료를 생성해보도록 하자.
```python
all_words = []
for cleaned_tweet in cleaned_tweets_all:
  for word in cleaned_tweet:
    all_words.append(word)

all_words_str = ' '.join(all_words)
```
`wordCloud`를 사용하기 위해서는 한줄로 묶은 데이터를에 띄워쓰기를 추가해 다시 가공해주어야 한다. 

띄워쓰기가 있어야 모듈이 단어를 구분하기 때문이다.
```python
def generate_wordcloud(text): 
    wordcloud = WordCloud(
                          width=800, height=400,
                          relative_scaling = 1.0,
                          # 로컬환경에서 실행시 폰트를 지정해줘야 한다
                          font_path='malgun',
                          # 마찬가지로 제거하고 싶은 단어를 여기에 추가 입력
                          stopwords = {'to', 'of'}
                          ).generate(text)
```
이후 시각화 자료를 생성하는 함수를 작성한다. `WordCloud`의 속성값에 이미지의 특성값을 전달해준다. 

이때 한글 데이터를 출력하기 위해선 반드시 `폰트지정`을 해주어야 한다.

로컬환경에서 구동시 본인 pc의 `Font` 폴더에 있는 한글 폰트의 이름을 지정해주면 된다. 따로 폴더의 주소가 필요하진 않다.
```python
    fig = plt.figure(1, figsize=(8, 4))
    plt.axis('off')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
```
이후 모듈을 실행할 코드를 작성하면 된다. 위와 같이 코드를 작성하면 실행 즉시 사진이 출력된다.
```python
cloud.to_file('파일명')
```
파일의 형태로 저장하고 싶다면 해당 코드를 삽입하면 된다.

<hr/>

### 👉 결과화면

* 2018년 10. 01 ~ 10. 14
![](https://velog.velcdn.com/images/banma1234/post/5fd18059-fc39-493e-97fe-66af0074d50d/image.png)

* 2022년 10. 01 ~ 10. 14
![](https://velog.velcdn.com/images/banma1234/post/d2171aeb-e5b8-45d9-89e7-b5a4d3c07bf9/image.png)

<hr/>


### 👉 전체코드
```python
import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# wordCloud 모듈
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#=================================================================

# reference : Dr. 야마다 아키히코
# https://colab.research.google.com/drive/14D9Zu4RN_fGABf-VRGooneIdsW16QqxP?hl=ko#scrollTo=8qfKxmWS2TCL

#=================================================================

# 트위터분석을 위한 기본적인 텍스트 cleaning 함수
def CleanText(readData, Num=True, Eng=True):
    # Remove Retweets
    text = re.sub('RT @[\w_]+: ', '', readData)
    # Remove Mentions
    text = re.sub('@[\w_]+', '', text)
    # Remove or Replace URL
    text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", ' ',
                  text)  # http로 시작되는 url
    text = re.sub(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{2,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", ' ',
                  text)  # http로 시작되지 않는 url
    # Remove only hashtag simbol "#" because hashtag contains huge information
    text = re.sub(r'#', ' ', text)
    # Remove Garbage Words (ex. &lt, &gt, etc)
    text = re.sub('[&]+[a-z]+', ' ', text)
    # Remove Special Characters
    text = re.sub('[^0-9a-zA-Zㄱ-ㅎ가-힣]', ' ', text)
    # Remove 출처 by yamada
    text = re.sub(r"(출처.*)", ' ', text)
    # Remove newline
    text = text.replace('\n', ' ')

    if Num is True:
        # Remove Numbers
        text = re.sub(r'\d+', ' ', text)

    if Eng is True:
        # Remove English
        text = re.sub('[a-zA-Z]', ' ', text)

    # Remove multi spacing & Reform sentence
    text = ' '.join(text.split())

    return text

#=================================================================


#검색하고 싶은 단어
search_word = "안녕"

#검색하는 기간
start_day = "2022-10-01"
end_day = "2022-10-14"

search_query = search_word + ' since:' + start_day + ' until:' + end_day 

#지정한 기간에서 검색하고 싶은 단어를 포함한 tweet를 취득
scraped_tweets = sntwitter.TwitterSearchScraper(search_query).get_items()

#처음부터 1000개의 tweets를 취득
sliced_scraped_tweets = itertools.islice(scraped_tweets, 1000)

#pandas DataFrame으로 변환
df = pd.DataFrame(sliced_scraped_tweets)
df = df[df['content'].str.contains('안녕|하이|반가워|안녕하세요')]

stop_words = " ~~~한글 불용어~~~"
stop_words=stop_words.split(' ')

# tweet 하나하나 불러오고 stopwords 제거
cleaned_tweets_all = []

for tweet in df.content:
  cleaned_tweet = []
  # 한글 불용어 처리를 위해 Eng에 False값을 준다
  cleaned_tweet_string = CleanText(tweet, Num=True, Eng=False)
  tweet_tokens = word_tokenize(cleaned_tweet_string)
  for token in tweet_tokens:
    if token.lower() not in stop_words:
      cleaned_tweet.append(token)

  cleaned_tweets_all.append(cleaned_tweet)

# print(cleaned_tweet)


#===============================================================

# wordCloud 생성
def generate_wordcloud(text): 
    wordcloud = WordCloud(
                          width=800, height=400,
                          relative_scaling = 1.0,
                          font_path='malgun', # coLab이 아닌 로컬환경에서 실행시 폰트를 지정해줘야 한다
                          stopwords = {'to', 'of'} #제거하고 싶은 단어를 여기에 입력
                          ).generate(text)
    
    fig = plt.figure(1, figsize=(8, 4))
    plt.axis('off')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

all_words = []
for cleaned_tweet in cleaned_tweets_all:
  for word in cleaned_tweet:
    all_words.append(word)

all_words_str = ' '.join(all_words)

generate_wordcloud(all_words_str)
```

<hr/>

>* #### Reference By....
### Dr. 야마다 아키히코
https://colab.research.google.com/drive/14D9Zu4RN_fGABf-VRGooneIdsW16QqxP?hl=ko#scrollTo=8qfKxmWS2TCL
