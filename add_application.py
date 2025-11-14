# 日時を取得するためのモジュールをインポート
from datetime import datetime
# プロファイルを設定
profiles = {
    "太郎":{"age":25,"height":170.5,"is_student":False}
}

# 時間によって挨拶を変更する関数の作成
def greet():
    #現在時刻を0-23で取得
    hour = datetime.now().hour
    #挨拶の変更をIFにて実装
    if 5 <= hour < 11:
        greeting = "おはようございます"
    elif 11 <= hour < 17:
        greeting = "こんにちは"
    else:
        greeting = "こんばんは"
    return greeting

# 名前の入力を要求
profiles_name = input("名前を入力してください: ")

#入力内容からプロファイルから情報を取得
if profiles_name in profiles:
    profile = profiles[profiles_name]
    name = profiles_name
    age = profile["age"]
    height = profile["height"]
    is_student = profile["is_student"]
    #プロファイルが確認できたら、挨拶と名前、年齢を出力
    print(f"{greet()}、{name}さん！ 年齢:{age}、身長{height}、在学生:{is_student}")
#登録がない場合
else:
    print("登録がありません")

