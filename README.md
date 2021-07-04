# notice_to_slack
機械学習を回すといつ終わったかわからなくなるので、通知を出す
# 用意するもの
 * slack api からtokenと権限の設定をする
 * このgitをクローン 
 * token.iniを作る

## 権限の内容
```
chat.posMessage
    chat:write
```

## token.iniの中身
```
xoxb-hogehoge...
hogehoge...
```
１行目、slack apiを設定した場合のtoken  
２行目、送信するチャンネルの名前

