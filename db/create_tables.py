# セッション変数の取得
from setting import session
# Userモデルの取得
from user import *
from record import *

Base.metadata.create_all(bind=ENGINE)

