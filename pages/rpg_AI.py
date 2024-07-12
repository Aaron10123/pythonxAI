import random


def start_game():
    print("歡迎來到冒險遊戲！")
    player_name = input("請輸入你的名字：")
    print(f"你好，{player_name}！讓我們開始冒險吧！")

    player_health = 100
    enemy_health = random.randint(50, 100)

    while player_health > 0 and enemy_health > 0:
        print("\n你的生命值：", player_health)
        print("敵人的生命值：", enemy_health)
        print("\n選擇你的行動：")
        print("1. 進攻")
        print("2. 防禦")

        player_action = input("請輸入你的選擇（1或2）：")

        if player_action == "1":
            player_attack = random.randint(10, 20)
            enemy_health -= player_attack
            print(f"你對敵人造成了 {player_attack} 點傷害！")
        elif player_action == "2":
            player_defense = random.randint(5, 10)
            player_health += player_defense
            print(f"你進行了防禦，回復了 {player_defense} 點生命值！")

        enemy_attack = random.randint(5, 15)
        player_health -= enemy_attack
        print(f"敵人對你造成了 {enemy_attack} 點傷害！")

    if player_health <= 0:
        print("你被敵人擊敗了，遊戲結束！")
    else:
        print("你成功擊敗了敵人，恭喜你完成冒險！")


start_game()
