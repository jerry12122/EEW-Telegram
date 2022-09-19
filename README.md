###### tags: `README`

# 地牛 Wake up Telegram 通知連動

配合地牛 Wake Up! Windows 版 https://eew.earthquake.tw

## 說明

由於地牛 wake up 僅會顯示桌面通知，可以藉由此連動程式來發送 telegram 訊息通知

## 需求

- Telegram Bot Token
- Telegram User ID
- Python 環境

## 使用說明

1. 安裝依賴套件

```
pip install -r requirements.txt
```

2. 將設定檔`config.json.sample`更改為`config.json`並新增 bot_token
3. 使用指令來新增/移除 uid

```
python notifications.py [add/remove] [uid]
```

4. 使用系統管理員打開地牛 Wake up 程式，打開設定>其他
5. 啟用連動設定並選擇`start.bat`的路徑，儲存
