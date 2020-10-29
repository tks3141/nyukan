
# イメージ

ロジックはFlask上で持たせて，React側とNFC側はAPI叩くだけ

# ブラウザ上でユーザーの登録

1. 現在存在するユーザー一覧にして，そこから選択して，ユーザーにNFCを登録
    * 登録は，次のNFCタッチを待ち受けして，それをIDとする．
1. 登録後は，Slackでユーザー設定コマンドを出力できるように？

* API
  * GET users
    * res : users json
  * post mkuser name
    * res : success or failed
  * post addnfc user
    * res : (success,nfc_id) or failed
      * NFC待ちして，成功すればNFC

# 入退館時

* API
  * post nfc idm
    * res : suc or fail

Flask : when post nfc:NFCを検索して，

* 登楼されていれば
  * データベース更新，
    * ユーザーのStatusが0
      * 1にして，Recordに入館時間を追加
    * 1
      * 0にして，Last_loginのレコードに体感時間を追加
* いなければ，Slackにそのまま投げて未登録を表示でおわる．

# NFCサーバー

基本的に，登録待ちか入館街の2状態
ので，NFCタッチされたらAPIにそれを通知するだけだ
API: post nfc idm
