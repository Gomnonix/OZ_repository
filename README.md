# Admin 페이지 프로트단 제작 프로젝트

## ⚙️ 사용 기술
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)


## 🗓프로젝트 기간
-  **기본요구사항 :'24.03.26 ~ '24.03.26**
-  **더 만들어볼 기능 : '24.03.26 ~ '24.03.26**

## 🗞실행 방법
1. Git Repo Clone

```
https://github.com/Gomnonix/admin_page
```
2. Move to Project HTML Folder
```
https://github.com/Gomnonix/admin_page/blob/main/admin-page.html
```
3. Run HTML File

## 프로젝트 내용

### 기본 요구 사항
- 카테고리(셀렉트)를 클릭하면 상의, 하의, 신발, 패션잡화 메뉴가 나오게 코드 작성
- 입력 버튼 안에 “제품명을 입력해주세요
- 조회 버튼이 입력창 옆에 붙어 있도록 코드 작성
- 테이블을 이용해 최 상단에는 속성 값을 넣고 하단에는 데이터가 입력되도록 코드 작성
- 최하단에는 페이지 네이션 기능이 나타나도록 코드 작성
### 더 만들어볼 기능
- 성별로 구별할 수 있는 버튼 또는 테이블 속성값에 성별을 구분할 수 있는 속성을 넣어주세요
- 카테고리 앞에 체크 박스를 하나씩 넣어주고, 선택된 체크 박스를 삭제하는 버튼을 만들어주세요 그 위치는 조회 버튼이 있는 라인의 가장 끝에 위치했으면 좋겠습니다.
- 신규 등록 상품 옆에  신규 등록 상품 (2024-01-22) 형태로 변경해주시고요 날짜는 업데이트된 일자가 반영되도록 만들어주세요
- 테이블 하단 또는 상단에 github 아이콘을 넣어주세요 그리고 이미지 클릭하면 여러분의 깃허브 주소로 이동하도록 만들주세요

  
![adminPage1](https://github.com/Gomnonix/admin_page/blob/main/adminPage1.png)

## 프로젝트 구조
```yaml

📦admin_page
 ┣ 📂.git
 ┃ ┣ 📂hooks
 ┃ ┃ ┣ 📜applypatch-msg.sample
 ┃ ┃ ┣ 📜commit-msg.sample
 ┃ ┃ ┣ 📜fsmonitor-watchman.sample
 ┃ ┃ ┣ 📜post-update.sample
 ┃ ┃ ┣ 📜pre-applypatch.sample
 ┃ ┃ ┣ 📜pre-commit.sample
 ┃ ┃ ┣ 📜pre-merge-commit.sample
 ┃ ┃ ┣ 📜pre-push.sample
 ┃ ┃ ┣ 📜pre-rebase.sample
 ┃ ┃ ┣ 📜pre-receive.sample
 ┃ ┃ ┣ 📜prepare-commit-msg.sample
 ┃ ┃ ┣ 📜push-to-checkout.sample
 ┃ ┃ ┣ 📜sendemail-validate.sample
 ┃ ┃ ┗ 📜update.sample
 ┃ ┣ 📂info
 ┃ ┃ ┗ 📜exclude
 ┃ ┣ 📂logs
 ┃ ┃ ┣ 📂refs
 ┃ ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┃ ┗ 📂remotes
 ┃ ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┗ 📜HEAD
 ┃ ┣ 📂objects
 ┃ ┃ ┣ 📂04
 ┃ ┃ ┃ ┗ 📜e0386ae0b909e1055a1608609ef7b013721de8
 ┃ ┃ ┣ 📂08
 ┃ ┃ ┃ ┗ 📜88f564c9d199c5649f0234904dad12546be2e2
 ┃ ┃ ┣ 📂09
 ┃ ┃ ┃ ┗ 📜ef2c0028cf0735d4912aed40e1f4d197a71e0b
 ┃ ┃ ┣ 📂0f
 ┃ ┃ ┃ ┗ 📜8ad1be898a816277949959efcac7744975c1d7
 ┃ ┃ ┣ 📂11
 ┃ ┃ ┃ ┗ 📜f0114df20cae8f9036918e5cd81eb64025133b
 ┃ ┃ ┣ 📂15
 ┃ ┃ ┃ ┗ 📜fec84e8f04e666198ee2664add2c17e2957269
 ┃ ┃ ┣ 📂16
 ┃ ┃ ┃ ┗ 📜000604d13843fb1866ea42ddf6577db4c6677c
 ┃ ┃ ┣ 📂18
 ┃ ┃ ┃ ┗ 📜95dff8c62cf328122414cba0e06a582b334f99
 ┃ ┃ ┣ 📂19
 ┃ ┃ ┃ ┗ 📜06b00702ec3d36e2fce0299e15e7121a765427
 ┃ ┃ ┣ 📂24
 ┃ ┃ ┃ ┗ 📜09bf8c3cae7e1306f1624a8224246a5c6d22fe
 ┃ ┃ ┣ 📂28
 ┃ ┃ ┃ ┗ 📜a1607387ca585d7c160c2b98405998d89c07fc
 ┃ ┃ ┣ 📂29
 ┃ ┃ ┃ ┗ 📜2cf6fbb48a7116ad7cd6dc27b6f6afd8b1c146
 ┃ ┃ ┣ 📂2a
 ┃ ┃ ┃ ┣ 📜a835472f1f1c01089bd7f9b3484deb771586e8
 ┃ ┃ ┃ ┗ 📜bbe6ba12b95922abe460ab47515a686c80d8cf
 ┃ ┃ ┣ 📂2e
 ┃ ┃ ┃ ┗ 📜a427a0ad49c6b6e9e03119791fe8781fb30b5a
 ┃ ┃ ┣ 📂31
 ┃ ┃ ┃ ┣ 📜29c365ebdb4964b74e51f21c40ef43db1705fa
 ┃ ┃ ┃ ┗ 📜c92d6c6b4ce892f471a69f3b31316891812763
 ┃ ┃ ┣ 📂37
 ┃ ┃ ┃ ┣ 📜5e0569cedce76cee89f835e5b8a92730fad797
 ┃ ┃ ┃ ┗ 📜af6b4a7fc8ab4b1373bef3d0a1d67eb9d73a2d
 ┃ ┃ ┣ 📂3b
 ┃ ┃ ┃ ┗ 📜e7cec59f164d3c10144d0563fa47ac318d2889
 ┃ ┃ ┣ 📂3d
 ┃ ┃ ┃ ┗ 📜ad2b921229b4486ff59bdc231dfb1c0e417e1a
 ┃ ┃ ┣ 📂3f
 ┃ ┃ ┃ ┗ 📜2e8f28b1086d2fce43e965c56a1cdd10079cfb
 ┃ ┃ ┣ 📂41
 ┃ ┃ ┃ ┣ 📜aa4ef65940add871f692e2eb5552f6676b2fd4
 ┃ ┃ ┃ ┗ 📜f239cf39bbf17483d2949e5d4e29201a2972c8
 ┃ ┃ ┣ 📂4d
 ┃ ┃ ┃ ┗ 📜a5e45b87f4bacf4f0865a39f14eb52a712cbcc
 ┃ ┃ ┣ 📂4e
 ┃ ┃ ┃ ┗ 📜1d630465d3ee28beb47c1ef5b6a299fdf5d44a
 ┃ ┃ ┣ 📂57
 ┃ ┃ ┃ ┣ 📜00de521e4b5cc6a9b7ecafa4f3b66eec41a0cb
 ┃ ┃ ┃ ┗ 📜cda940c9dc72d23ffb8cea32fc9290e582a093
 ┃ ┃ ┣ 📂5a
 ┃ ┃ ┃ ┗ 📜a09d971cc7bb452c40bc9351d4c0d964d0f904
 ┃ ┃ ┣ 📂5b
 ┃ ┃ ┃ ┗ 📜c2929f2eef0fcc21dcca9a980c0a7c355d01d6
 ┃ ┃ ┣ 📂60
 ┃ ┃ ┃ ┗ 📜31c53b618d2f0b7c7cb5afcb5d28c7a7469f76
 ┃ ┃ ┣ 📂74
 ┃ ┃ ┃ ┗ 📜3a1556e7f0180672e92dc203e62bab04baff89
 ┃ ┃ ┣ 📂75
 ┃ ┃ ┃ ┗ 📜f540176aa6eef2d9d1b80ce6fbdfe7f8ce382c
 ┃ ┃ ┣ 📂78
 ┃ ┃ ┃ ┗ 📜6c21a6be33cca391c38d9b7d3a280cbdee14f9
 ┃ ┃ ┣ 📂7b
 ┃ ┃ ┃ ┗ 📜3f5bd82bb5a44fbd79685d33dd13772a7730fa
 ┃ ┃ ┣ 📂7c
 ┃ ┃ ┃ ┗ 📜40162d827afe8fbbfca8f1bc094a878551de28
 ┃ ┃ ┣ 📂7f
 ┃ ┃ ┃ ┗ 📜c081c47e116202f75e5b06e688b78bc5e5d021
 ┃ ┃ ┣ 📂82
 ┃ ┃ ┃ ┗ 📜8d64e91cc174b3ec6e1cf7e5e7bee8352608f9
 ┃ ┃ ┣ 📂83
 ┃ ┃ ┃ ┣ 📜01aa22f8a41209a52d480d41b37e447b4a30ac
 ┃ ┃ ┃ ┗ 📜38281e8334dbbee8350c917594a047c4e7b63d
 ┃ ┃ ┣ 📂85
 ┃ ┃ ┃ ┗ 📜726116a07d1cc8820492677445ab525a20444e
 ┃ ┃ ┣ 📂87
 ┃ ┃ ┃ ┗ 📜ab15c9e667cd287ceb58bf0fed285775eb0cb1
 ┃ ┃ ┣ 📂88
 ┃ ┃ ┃ ┗ 📜41921e1aade6f0090b37b0e29babd0fa5b81f2
 ┃ ┃ ┣ 📂8a
 ┃ ┃ ┃ ┗ 📜b01d234a376942a522a423ba04fd206587dbbd
 ┃ ┃ ┣ 📂8b
 ┃ ┃ ┃ ┗ 📜e8e510e33d6b8a459f97854ef17051a87f2789
 ┃ ┃ ┣ 📂8d
 ┃ ┃ ┃ ┣ 📜005dd8159e5775c1acced9f4e5577da9b1fb96
 ┃ ┃ ┃ ┗ 📜a5c2ff2baefb68337fb4117ed45c0094370fdc
 ┃ ┃ ┣ 📂92
 ┃ ┃ ┃ ┗ 📜d01e32e69dc58c92658270a67763ef028a2c47
 ┃ ┃ ┣ 📂9a
 ┃ ┃ ┃ ┗ 📜cf054923f2683599a6809cda6181592c5ddf69
 ┃ ┃ ┣ 📂9b
 ┃ ┃ ┃ ┗ 📜24e71697a4734d02c24a2866c68f8a27d21415
 ┃ ┃ ┣ 📂9f
 ┃ ┃ ┃ ┗ 📜b9f6b9d931dae3ed04c4b8cad6fb3135ae6e3b
 ┃ ┃ ┣ 📂a7
 ┃ ┃ ┃ ┗ 📜2da56da31ab0000df35ade24eb49b8d15ff0f1
 ┃ ┃ ┣ 📂aa
 ┃ ┃ ┃ ┗ 📜37641c1069bfedb992a5720c669773b44f3461
 ┃ ┃ ┣ 📂ab
 ┃ ┃ ┃ ┗ 📜a68ab82d08e9f8330f41046461afd1dfc51a79
 ┃ ┃ ┣ 📂b0
 ┃ ┃ ┃ ┣ 📜adf586f5716f9a5a110d0676098662847e7d12
 ┃ ┃ ┃ ┗ 📜cde2bbc7b71cf3a07f5ee74f4e235484e76ba2
 ┃ ┃ ┣ 📂b8
 ┃ ┃ ┃ ┗ 📜9e0da28de3429d9a58f9c2b255e31f7fc4f936
 ┃ ┃ ┣ 📂b9
 ┃ ┃ ┃ ┗ 📜725d50277fedd9896a010863c93349dcfe84e5
 ┃ ┃ ┣ 📂bf
 ┃ ┃ ┃ ┗ 📜1794dc229a421f46f385963699fc981f37e422
 ┃ ┃ ┣ 📂c0
 ┃ ┃ ┃ ┗ 📜44d082e4d53f129a359df462be9a416ee9aca0
 ┃ ┃ ┣ 📂c3
 ┃ ┃ ┃ ┣ 📜87e50a1e4e5c23542f63c428fc9e23fcb5afc9
 ┃ ┃ ┃ ┣ 📜986e28a6ef13a7b26f7cee18960643b5a25703
 ┃ ┃ ┃ ┗ 📜f85e3c52c6b440046bb402ef32d17353d47519
 ┃ ┃ ┣ 📂c5
 ┃ ┃ ┃ ┗ 📜8d71467303e5b16d6c5a6b28df76b5b5d63682
 ┃ ┃ ┣ 📂c7
 ┃ ┃ ┃ ┗ 📜2bc96985d8d3f80e7371e72f29967ffd56bcdd
 ┃ ┃ ┣ 📂c9
 ┃ ┃ ┃ ┗ 📜0608a45c08af2f3228dd43decf9ddab557ead0
 ┃ ┃ ┣ 📂cd
 ┃ ┃ ┃ ┗ 📜cf218a24c4f3bb38ae4f729a50ea7c115b1334
 ┃ ┃ ┣ 📂ce
 ┃ ┃ ┃ ┗ 📜4e4e41189b99cf3a7dc6e8dc6888177a387cd8
 ┃ ┃ ┣ 📂d4
 ┃ ┃ ┃ ┗ 📜fa1709436e987d3889f8e454177d4dd6a4feb5
 ┃ ┃ ┣ 📂d6
 ┃ ┃ ┃ ┗ 📜9cc4e2fb9ff52bd02a81de3617008d105f68bd
 ┃ ┃ ┣ 📂d8
 ┃ ┃ ┃ ┗ 📜92afafaeae2e89d51bdac4c584136a43862e90
 ┃ ┃ ┣ 📂e0
 ┃ ┃ ┃ ┗ 📜f2754239e654255d1fe1eaa7840679e2101ea3
 ┃ ┃ ┣ 📂e5
 ┃ ┃ ┃ ┗ 📜607d7664b4a15dd37c93c5f5b88c30155ccd8b
 ┃ ┃ ┣ 📂ef
 ┃ ┃ ┃ ┣ 📜af94bfc8c886e5c0155f0ddfb17d673770741a
 ┃ ┃ ┃ ┣ 📜ba69d136bc2c0931561c0acae2b8ff1cdd9d99
 ┃ ┃ ┃ ┗ 📜d5597f13f172eccfcb67613e2ffe61918be509
 ┃ ┃ ┣ 📂f7
 ┃ ┃ ┃ ┗ 📜9f81f0d031687a9386638706699d8b2577281e
 ┃ ┃ ┣ 📂info
 ┃ ┃ ┗ 📂pack
 ┃ ┣ 📂refs
 ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┣ 📂remotes
 ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┗ 📂tags
 ┃ ┣ 📜COMMIT_EDITMSG
 ┃ ┣ 📜config
 ┃ ┣ 📜description
 ┃ ┣ 📜FETCH_HEAD
 ┃ ┣ 📜HEAD
 ┃ ┣ 📜index
 ┃ ┗ 📜ORIG_HEAD
 ┣ 📂images
 ┃ ┗ 📜github.png
 ┣ 📜admin-page.html
 ┣ 📜admin-page.js
 ┣ 📜adminPage1.png
 ┗ 📜README.md
