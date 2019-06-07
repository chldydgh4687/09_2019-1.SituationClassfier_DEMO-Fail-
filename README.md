# SituationClassfier_DEMO

## making Pipeline

### Pipeline_design#1 목표
- ~~실시간 서비스를 대비할 비디오 -> 사진 추출 함수를 구현한다.  (OpenCV)~~
- ~~프로그램을 돌릴 main 파일 일부를 구현한다.~~
- ~~Depth_Estimation 변수 및 필요없는 소스 코드 파일 재구성한다.~~ (수정은 완료 / 삭제는 보류 )
- ~~Disparity 파일이 제대로 추출되는지 DEMO 영상을 넣어 돌려본다. ~~

- 실시간으로 돌릴시 참고되는 코드링크 : https://m.blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220500854338&proxyReferer=https%3A%2F%2Fwww.google.com%2F

### Pipeline_design#2 목표
- SSD 가 구성됬다는 기준으로 대략적인 각 물체의 GT 박스 수동으로 좌표 배열을 주어 RGB와 DEPTH 픽쳐에 보내준다.
- DEPTH 의 대략적인 평균값을 정하여 기준을 정한다.
- ROAD_DETECTION 이 구성됬다는 으로 바닥의 GT를 박스 좌표 배열을 RGB에 보내준다.

### Pipeline_design#3 목표
- CLASSFICATION 의 기준을 세워 분류한다.
- 이의 위험도를 색깔로 표현

#### colab에서 돌리기( 계속 추가됨 )
~~~
!git clone https://github.com/chldydgh4687/SituationClassfier_DEMO.git
!pip3 install torch torchvision
pip install torch torchvision scikit-image h5py
cd SituationClassfier_DEMO
cd Depth_e
!bash fetch_checkpoints.sh
cd -
!python test.py --input single_view
#화살표 파일 Depth_e/viz_predictions/images/ 경로에 disparity 파일 결과 생성됨.
~~~

### 최종 목표
- 실시간으로 비디오의 FRAME을 나눠 위의 메커니즘을 통하여 사용자 인터페이스를 통한 위험도를 분류한다.
