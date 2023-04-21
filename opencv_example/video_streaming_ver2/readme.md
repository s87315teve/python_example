# 使用教學

在樹莓派的terminal中輸入
```
sudo apt-get install ffmpeg
```
安裝完後輸入以下指令開始串流影像
```
ffmpeg -f v4l2 -i /dev/video0 -preset ultrafast -vcodec libx264 -tune zerolatency -b 1000k -f h264 udp://your_IP:your_PORT
```
-f v4l2 -i /dev/video0這段是讓我連接到webcam，但不知道樹莓派能不能用

IP請去找自己設備的IP （我有點忘記是要放樹莓派的ip還是筆電的ip了，你們可能要去試試看）
PORT自訂一個不會衝突到的就好（例如:5000)


樹莓派都設定好之後，在筆電執行以下指令安裝python的opencv環境
```
pip intall opencv-python
```
之後再執行opencv_test.py就可以串流影像了(要注意IP和PORT)
```
python opencv_test.py
```
