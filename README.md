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

### 5주차
* #### Vm 위에서 Ubuntu Linux 실행
`Virtual Box`위에 `Ubuntu(Linux)`를 올린 후 서버 구동에 유용한 `Cockpit`, `Cloud panel`등을 설치해 서버를 제어했습니다.

<hr/>

## 📌 5주차 : Ubuntu 서버 세팅

### 🚗현대인을 위한 3줄요약.
>  Window 환경에서 별다른 조작 없이 Virtual Box(가상머신)를 이용해 가상환경에서 ubuntu 리눅스를 설치, 각종 task를 수행할 수 있다.

***

## **📌 설치 및 정보**

우선 실습에 필요한 것들(Vm, Ubuntu)를 설치하고 또 알아보도록 한다.

***

### 👉 Virtual Box
Virtua Box가 무엇인지 알기 전에 `가상머신`이란 무엇인가 먼저 알 필요가 있다.

`가상머신(Virtual Machine)`은 실제 하드웨어와 아무런 관련이 없는 가상의 컴퓨터로 하드웨어를 소프트웨어로 구현해 작동하게끔 한 것이다.

가상머신을 사용하는 가장 큰 이유는 다음과 같다.

* 다른 운영체제를 사용하는 경우( Windows >> Linux )
* 독립된 작업공간이 필요한 경우( 보안상의 이유 )

***

>Virtual Box 설치링크 : https://www.virtualbox.org/

`Virtual Box(가상머신)`는 오라클에서 만든 가상머신 솔루션으로 무료로 제공되는 오픈소스이다.

링크를 타고 가면 세상 크게 `Download` 버튼이 있기 때문에 문제없이 설치파일을 받을 수 있다.

![](https://velog.velcdn.com/images/banma1234/post/6d7cc76e-c2b7-4c9a-ae0a-ae95245f447e/image.png)

설치파일을 실행한 후 설치가 완료될때 까지 `Yes/Next`를 계속 눌러준다.

***

### 👉 Ubuntu Linux 설치
먼저 굳이 가상머신을 설치하면서까지 리눅스를 사용하는 이유를 알아보자.
`리눅스(Linux)`는 리누스 토발즈가 `유닉스(Unix)` OS를 기반으로 만든 OS이다.

유닉스를 기반으로 만들어졌기 때문에 다중 사용자, 다중 쓰레드, 멀티태스킹 등을 지원하는 `네트워크 운영체제(NOS)`이며 다음과 같은 특징을 가지고 있다.

* 다중사용자, 다중작업을 지원하기 때문에 `서버`를 운영하기 가장 적합하다.
* `오픈소스`이기 때문에 커뮤니티가 방대하다.
* 기본적으로 `무료`이다.

***

> Ubuntu 설치 링크 : https://ubuntu.com/download/server

리눅스에 대해 알았다면 우분투를 설치할 차례이다.

![](https://velog.velcdn.com/images/banma1234/post/8b594a5c-77cb-4a0f-a506-e4abcb2a2ef6/image.png)

링크를 타고 가면 여러 버전의 설치파일이 있을텐데 반드시 `22.04.1 LTS`버전을 다운받아야 한다.

작성일 기준 최신버전 바로 아래단계인데 최신버전이 릴리즈된지 얼마 되지 않아 주변 프로그램이 호환되지 않는 이슈가 있기 때문이다.



***

## **📌 실습환경 설정**

다운받은 Vm 위에서 안정적으로 ubuntu와 각종 서비스를 이용하기 위해 실습환경을 설정하도록 한다.

***

### 👉 Virtual Box에 ubuntu 올리기

다음은 설치한 Vm에 `Ubuntu` OS를 올려보도록 하자.

![](https://velog.velcdn.com/images/banma1234/post/ccb11d2f-957e-44d2-b068-c1636d3d1f0d/image.png)

 `Virtual Box`를 처음 실행하면 다음과 같은 화면이 출력된다. 여기서 `새로 만들기(N)`를 클릭한 후 `전문가 모드`로 들어가 다음 옵션들을 제어한다.
 
 * Name and Operating System
 * Hardware
 
![](https://velog.velcdn.com/images/banma1234/post/7a3a16fb-24ef-4b2f-9204-8d6b8913cc19/image.png)


먼저 `Name and Operating System`에 들어가 설치한 ubuntu `iso 파일`을 그림에 표시된 영역에서 등록해준다.

![](https://velog.velcdn.com/images/banma1234/post/18e31040-1c8c-46a0-9d48-22fcd25cd061/image.png)

다음은 `하드웨어 성능` 차례이다.

하드웨어 성능은 상황에 맞게 본인이 설정하면 되는데 대체로 `램 4GB`에 `4코어`정도면 왠만한 프로젝트를 무리없이 굴릴 수 있다.

이후 실행된 터미널에 다음과 같은 코드를 입력해 ubuntu를 업데이트 해준다.

```ubuntu
$sudo apt update && sudo apt upgrade -y
```

### 🚗현대인을 위한 3줄요약.
>  Window 환경에서 별다른 조작 없이 Virtual Box(가상머신)를 이용해 가상환경에서 ubuntu 리눅스를 설치, 각종 task를 수행할 수 있다.

***

## **📌 설치 및 정보**

우선 실습에 필요한 것들(Cockpit, Cloud panel)을 설치하고 또 알아보도록 한다.

***

### 👉 Cockpit
`Cockpit`은 리눅스를 `원격`에서 쉽게 관리하기 위한 툴이다.

보통 원격에서 접근한다고 하면 `SSH`를 떠올리기 마련인데 `SSH`를 사용하기엔 준비하는 프로젝트가 가벼울 때 사용된다.

![](https://velog.velcdn.com/images/banma1234/post/2c7420ed-ce8b-4f3a-bd57-d31b6767001d/image.png)

위 사진과 같이 관리자 페이지를 제공해주는데 이곳에서 다양한 기능을 수행할 수 있다.


이외에도 `자원/로그 모니터링` 같은 기능도 제공한다.

***

설치는 다른것 필요 없이 아래 코드만 입력하면 된다. 우분투의 기본 패키지에 포함되어있기 때문이다.

```ubuntu
$sudo apt-get install cockpit
$sudo systemctl enable cokcpit
$sudo ufw allow 9090/tcp
```

각각 설치, 자동실행, 포트오픈의 역할을 한다.

***

### 👉 Cloud panel 

`Cloud panel`은 무료 소프트웨어로 서버를 제어하고 관리하는 툴이다.

관리자 페이지를 제공하며 `Node.js`, `python`등 다양한 `언어`와 각종 `DB` 서비스(mySQL, mariaDB), `클라우드 서비스`와의 연계(AWS, firebase 등) 모두 가능하다.



***

>Cloud panel Docs : https://www.cloudpanel.io/docs/v2/getting-started/

Cloud panel도 마찬가지로 설치파일을 갖는게 아니라 명령어로 설치한다.

```ubuntu
$apt update && apt -y upgrade && apt -y install curl wget sudo
```

***

>#### 참고문서
* https://teamlab.github.io/jekyllDecent/blog/tutorials/%EA%B0%80%EC%83%81%EB%A8%B8%EC%8B%A0(VirtualBox)%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%98%EC%97%AC-%EB%A6%AC%EB%88%85%EC%8A%A4-%EC%8B%A4%EC%8A%B5-%ED%99%98%EA%B2%BD-%EB%A7%8C%EB%93%A4%EA%B8%B0 ( 설치 관련자료 )
* https://blog.dalso.org/linux/ubuntu-20-04-lts/17453 ( Cockpit 관련 자료 )
