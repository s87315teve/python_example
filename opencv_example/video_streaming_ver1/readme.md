# 使用教學
* 首先先在樹莓派和電腦都先安裝python的opencv環境
```
pip install opencv-python
```
* 然後把code裡面IP的地方改成樹莓派的IP (client和server的都要改)
* 之後在筆電上面執行server的code
```
python cam_server.py
```
* 最後在樹莓派上面執行client的code
```
python cam_client.py
```

功能介紹
* server端會自動錄影
* 按下"q"可以關掉
* 按下"c"可以截圖存下來
