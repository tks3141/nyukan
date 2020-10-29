# セッション変数の取得
from setting import session
# Userモデルの取得
from user import *

# sql = 'DROP TABLE '
# for table in ['idms','records','users']:
#     session.execute(sql+table)



# DBにレコードの追加
session.add(user = User(name='takashi'))

 
idm = Idm(idm='asdfasdfasdfasdf')

session.add(idm)  
session.commit()

# Userテーブルのnameカラムをすべて取得
users = session.query(User).join(Idm, User.id == Idm.users_id).all()
for user in users:
    print(user.name)
    for idm in user.idms:
        print(idm.idm)
