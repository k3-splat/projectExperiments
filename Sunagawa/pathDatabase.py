import csv
import os
from datetime import datetime

def initialize_csv(file_name):
    if not os.path.exists(file_name):  # ファイルが存在しない場合のみ作成
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # ヘッダーを記述
            writer.writerow(["ID", "FilePath", "Title", "Tag", "CreatedAt"])
    print(f"{file_name} initialized.")


def add_video(file_name, file_path, title, tag):
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # IDを自動生成（現在の行数を利用）
        id = sum(1 for _ in open(file_name, encoding='utf-8'))  # ヘッダーを含む行数
        created_at = datetime.now().strftime('%Y-%m-%d')  # 作成日を記録
        writer.writerow([id, file_path, title, tag, created_at])
    print(f"Video added: {file_path}")


def read_videos(file_name):
    videos = []
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            videos.append(row)  # 各行を辞書形式で保存
    return videos


def search_videos(file_name, tag):
    results = []
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Tag"] == tag:
                results.append(row)
    return results

if __name__=="__main__":
    print(f"Current working directory: {os.getcwd()}")

    csv_file = "videos.csv"

    # 初期化
    initialize_csv(csv_file)