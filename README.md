### Django 예제
#### 투표 (polls) application 예행 제작하기
---
##### 연습 목표
##### 1. URL, Template, View의 개념 이해하기 (MVT 모듈)
##### 2. Python 가상머신 테스트
##### 3. runserver 테스트 -> 추후 개별 서버 사용을 위한 사전작업
---
#### 테스트 방법 </b>반드시 순서를 지키기
##### 1. 해당 레포지토리를 git add remote {이름} 명령어로 원격 저장소 지정
##### 2. linux 환경 구성 (Window 사용자만 해당됩니다. 자세한 내용은 WSL 환경 구성 자료들을 검색해서 확인해 주세요. 권장 WSL은 Ubuntu LTS입니다.) </b>-> 앞으로의 모든 과정은 linux 환경을 전제로 기술됩니다.
##### 3. 파이썬 v.3.0 이상 설치 (Python 설치 웹페이지에 접속하여 운영체제에 맞게 설치)
##### 4. 파이썬 가상머신 설치 (명령어: python -m venv {가상환경명}) </b>만약 설치가 안 된다면 python 대신 python3로 바꿔서 재입력 </b>pip가 설치되지 않아서 생기는 오류는 sudo apt install python3-pip를 입력해서 pip를 먼저 설치한 후에 시도해 주세요. </b>여기서 python으로 명령어가 실행되었다면 앞으로도 python만 사용하면 되고, python3로 해야만 설치가 된다면 앞으로도 pyhton3로 항상 명령어를 입력해 주세요.
##### 5. 파이썬 가상머신 접속 (명령어: source {가상환경명}/bin/activate) </b>가상머신 접속에 성공했다면 맨 왼쪽에 ({가상환경명})이라는 헤드가 추가될 것입니다. </b>가상머신 종료는 deactivate 명령어만 입력해 주면 실행할 수 있습니다. linux 터미널을 닫기 전에 반드시 가상머신이 종료된 상태인지 확인할 것을 권장드립니다.
##### 6. "가상머신 접속 상태"에서 django 설치 (명령어: pip install django) </b>여기까지 완료되었다면 django 실행 환경은 모두 자동적으로 python이 구성해 주었을 것입니다. 이제 remote(=현재 Backend 레포지토리)에서 djangotutorial 파일을 참고하여 서버를 실행하고 생성된 웹페이지에 접속해 봅시다.
##### 7. cd djangotutorial -> 명령어 python manage.py runserver 입력 (이때 ls를 통해 해당 위치에 manage.py가 존재하는지 먼저 확인하시길 바랍니다 !)
