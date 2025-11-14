from datetime import datetime

# プロファイルを設定
profiles = [
    "太郎":{age = 25,height = 170.5,is_student = False}
]

print(profiles[])

def greet(name,age):
    # 現在時刻の時間を0-23で取得
    hour = datetime.now().hour

    # 時間帯によって挨拶を変える
    if 5 <= hour < 11:
        greeting = "おはようございます"
    elif 11 <= hour < 17:
        greeting = "こんにちは"
    else:
        greeting = "こんばんは"
    
    return f"{greeting},{name},さん！{age}歳"

print(greet("太郎"))    