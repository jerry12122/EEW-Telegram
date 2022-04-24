###### tags: `README`
# 地牛Wake up Telegram通知連動
配合地牛Wake Up! Windows版 https://eew.earthquake.tw   

說明
---
由於地牛wake up僅會顯示桌面通知，可以藉由此連動程式來發送telegram訊息通知

需求
---
* Telegram Bot Token
* Telegram User ID
* Python環境

使用說明
---
1. 安裝依賴套件
```
pip install -r requirements.txt
```
2. 將設定檔`config.json.sample`更改為`config.json`並新增bot_token  
3. 使用指令來新增/移除uid
```
python notifications.py [uid]
```
4. 使用系統管理員打開地牛Wake up程式，打開設定>其他  
5. 啟用連動設定並選擇`start.bat`的路徑，儲存
