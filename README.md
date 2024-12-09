# 강화 학습을 통한 유전형질 제어 교배 전략 연구
## 김도형 / Dohyung Kim
### 충북과학고등학교 / Chungbuk Science Highschool (CBSH)


본 리포지토리는 제 31회 삼성휴먼테크논문대상에 응모한 연구의 환경 코드와 학습된 모델, 결과 등을 담고 있습니다.

## 환경 구성

'requirements.txt'를 참고하여 필요한 라이브러리를 다운받을 수 있으며, pytorch는 컴퓨터 환경에 맞는 버전으로 설치하기 바랍니다.

아래는 requirements 설치 명령어와 연구자 본인 환경에서 사용한 pyTorch 설치 명령어입니다.

```
pip install -r requirements.txt
```

---이부분은 각자 환경에 따라 다름
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip3 install torch torchvision torchaudio

pip install "stable-baselines3[extra]>=2.0.0a4"
pip install gymnasium

```
---이부분은 각자 환경에 따라 다름


## 파일 구성

아래는 본 연구의 파일 구성입니다. 

```
.
├── result
│   ├── TwoDise
|   |   ├── envInfo.txt
|   |   ├── pigInfo.txt
|   |   ├── trained_model.zip
|   |   ├── monitor.csv
|   ├──TwoDiseInverse
│   └── ...
|
├── pig.py
├── geneEnv.py
├── flockEnv.py
├── ratioEnv.py
|
├── train.ipynb
├── eval_res.ipynb
|
└── ...
```

학습의 결과는 `result/(각 환경명)` 폴더에 위치해있습니다.
각 환경 폴더는 환경에 대한 정보를 간단히 기록한 `envInfo.txt` 파일과,
실행 시 환경의 정보를 설정할 명령어를 담은 `pigInfo.txt` 파일을 가집니다.

학습 환경은 총 네 개의 파이썬 파일로 구성됩니다.
`pig.py` 파일은 본 환경에서 하나의 개체로 작용하는 `pig` 클래스를 정의합니다.
`geneEnv.py` 파일은 gymnasium의 Env 클래스를 상속받아 본 연구의 강화학습 환경을 정의합니다.
`flockEnv.py' 는 에이전트에 의해서가 아닌 우수종끼리 교배하도록 설계된 환경입니다. `geneEnv` 클래스를 상속받습니다.
`ratioEnv.py`는 원하는 비율로 세대의 표현형이 나타나는 것이 보상으로 정의된 환경입니다. `geneEnv` 클래스를 상속받습니다.
