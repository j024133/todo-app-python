tasks = []
completed = []
import os

if os.path.exists("tasks.txt"):
    with open("tasks.txt","r",encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                status, task = line.split("|")
                tasks.append(task)
                completed.append(status =="True")


def save_tasks():
            with open("tasks.txt","w", encoding="utf-8") as file:
                for i in range(len(tasks)):
                    file.write(f"{completed[i]}|{tasks[i]}\n")


while True:
    print("\n=== ToDoアプリ ===")
    print("1. タスク追加")
    print("2. タスク表示")
    print("3. タスク削除")
    print("4. 完了切り替え")
    print("5. 終了")

    choice = input("選択してください")

    if choice == "1":
        task = input("タスク名: ")
        tasks.append(task)
        completed.append(False)
        save_tasks()
        print("追加しました！")

    elif choice == "2":
        print("\n--- タスク一覧 ---")

        if len(tasks) == 0:
            print("タスクはありません")

        else:
            for i, task in enumerate(tasks):
                status = "✓" if completed[i] else " "
                print(f"{i+1}.[{status}]{task}")
                      
    elif choice =="3":
        print("\n--- タスク一覧 ---")

        for i, task in enumerate(tasks):
            print(f"{i+1}.{task}")
        delate_num = int(input("削除する番号を入力: "))

        if 1 <= delate_num <= len(tasks):
            removed = tasks.pop(delate_num - 1)
            print(f"{removed}を削除しました！")
            save_tasks()

        else:
            print("無効な番号です")

    elif choice =="4":
        print("\n--- タスク一覧 ---")

        for i, task in enumerate(tasks):
                status = "✓" if completed[i] else " "
                print(f"{i+1}.[{status}]{task}")

        num = int(input("完了状態を切り替える番号: "))

        if 1 <= num <= len(tasks):
            completed[num - 1] = not completed[num - 1]
            print("更新しました！")
            save_tasks()

        else:
            print("無効な番号です")

    elif choice =="5":
        print("終了します")
        break

    else:
        print("正しい番号を入力してください")