# 変数とデータ型
name = "太郎"
age = 25
height = 170.5
is_student = False

print(f"名前: {name}, 年齢: {age}, 身長: {height} cm, 学生か？ {is_student}")

# 関数
def greet(name):
    return f"こんにちは、{name}さん！"

print(greet("太郎"))

score = 50

# 条件分岐
if score >= 80:
    print("合格！")
elif score >= 50:
    print("補習が必要です")
else:
    print("不合格…")

# ループ
for i in range(1, 6):
    print(f"カウント: {i}")    

# 配列とリスト
fruits = ["りんご", "バナナ", "さくらんぼ"]
print(fruits[2])

# オブジェクトと辞書
person = {
    "name": "花子",
    "age": 30
}
print(person["name"])

# クラスとオブジェクト指向
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"こんにちは、私は{self.name}です。")

person = Person("花子", 30)
person.greet()

# 例外処理
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("0では割り算できません！")

# 同期処理と非同期処理の違い
# 同期処理
import time

print("1. ご飯を炊く（時間がかかる）")
time.sleep(3)  # 3秒待つ（ご飯が炊けるまで待つ）
print("2. ご飯が炊けた")
print("3. 野菜を切る")
print("4. 味噌汁を作る")
print("5. ご飯を盛る")


















