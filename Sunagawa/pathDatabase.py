import csv
import os
from datetime import datetime

class pathDatabase:
    def __init__(self, file_path):
        tag = os.path.basename(file_path)
        title = tag + "_Animation"
        pathDatabase.add_folder(self, "folderPaths.csv", file_path, title, tag)

    def initialize_csv(self, file_name):
        if not os.path.exists(file_name):  # ファイルが存在しない場合のみ作成
            with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "FilePath", "Title", "Tag", "CreatedAt"])
            print(f"{file_name} initialized.")

    def add_folder(self, file_name, file_path, title, tag):
        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            id = sum(1 for _ in open(file_name, encoding='utf-8'))  # ヘッダーを含む行数
            created_at = datetime.now().strftime('%Y-%m-%d')
            writer.writerow([id, file_path, title, tag, created_at])
        print(f"Folder added: {file_path}")

    def remove_folder(self, file_name, tag):
        if not os.path.exists(file_name):
            print(f"{file_name} does not exist.")
            return

        temp_file = file_name + ".tmp"
        with open(file_name, mode='r', newline='', encoding='utf-8') as infile, \
             open(temp_file, mode='w', newline='', encoding='utf-8') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            deleted = False
            for row in reader:
                if row["Tag"] == tag:
                    deleted = True
                    print(f"Deleted folder: {row['FilePath']} with tag {tag}")
                else:
                    writer.writerow(row)

        os.replace(temp_file, file_name)
        if not deleted:
            print(f"No entry found with tag {tag}")

    def get_nth_entry(self, file_name, n):
        """n番目に登録されたファイルのパス、タグ、日時を返す関数。"""
        if not os.path.exists(file_name):
            print(f"{file_name} does not exist.")
            return -1

        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            entries = list(reader)
            if 0 < n <= len(entries):  # nが有効な範囲内であることを確認
                entry = entries[n - 1]  # インデックスは0から始まるためn-1
                return {
                    "FilePath": entry["FilePath"],
                    "Tag": entry["Tag"],
                    "CreatedAt": entry["CreatedAt"]
                }
            else:
                print(f"Invalid entry number: {n}")
                return -2

    def read_videos(self, file_name):
        videos = []
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                videos.append(row)
        return videos

    def search_videos(self, file_name, tag):
        results = []
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Tag"] == tag:
                    results.append(row)
        return results

    def get_mp4_files(self, directory):
        """指定したディレクトリ配下にあるすべての.mp4ファイルを取得する関数。"""
        mp4_files = []
        for root, _, files in os.walk(directory):  # ディレクトリを再帰的に探索
            for file in files:
                if file.endswith(".mp4"):  # 拡張子が.mp4のファイルのみ
                    full_path = os.path.join(root, file)
                    mp4_files.append(full_path)
        return mp4_files

    def search_registered_videos(self, file_name, tag):
        """登録されたパスの配下にある動画を検索する関数。"""
        results = []
        videos = pathDatabase.search_videos(self, file_name, tag)
        for video in videos:
            folder_path = video["FilePath"]
            if os.path.exists(folder_path):  # フォルダが存在する場合のみ探索
                mp4_files = pathDatabase.get_mp4_files(folder_path)
                results.extend(mp4_files)
        return results

if __name__ == "__main__":
    db = pathDatabase("C:/Users/gunda/projectExperiments/Sunagawa/test")
    entry = db.get_nth_entry("C:/Users/gunda/projectExperiments/Sunagawa/folderPaths.csv", 1)
    if entry:  # エントリが存在する場合のみ出力
        print(f"FilePath: {entry['FilePath']}, Tag: {entry['Tag']}, CreatedAt: {entry['CreatedAt']}")