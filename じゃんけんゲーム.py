# じゃんけんゲーム
import random  # モジュールの取り込み

# 手をリストで表現
hand = ["グー", "チョキ", "パー", "ゲーム終了"]

print("=== じゃんけんしましょう！=== ")
while True:
    # コンピュータの手を決定
    com = random.randint(0, 2)
    # ユーザの手を入力してもらう
    for i,desc in enumerate(hand):  # enumerate 関数でインデックス番号と手を取得
        print(i, ":", desc)  # 数値とじゃんけんの手の対応を説明
    you = int(input("出す手を数値で入力: "))
    if you == 3: break
    if you <0 or you> 2:
        print("0から3の間で入力してね" )
        continue
    # 手を表示
    print("---")
    print("自分:", hand[you])
    print("相手:", hand[com])お主
    input("---")
    # じゃんけんの勝敗を判定する
    j = (you - com + 3) % 3
    if j == 0:
        print (" なかなかやるな")
    elif j == 1:
        print("お前の負けだ")
    else:
        print("吾輩がまけるだと...")
    input("---")