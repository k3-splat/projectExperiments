import csv
import os
import shutil
from datetime import datetime

class pathDatabase:
    def __init__(self):
        self.csvFilePath = "folderPaths.csv"

    def initialize_csv(self):
        if not os.path.exists(self.csvFilePath):  # ファイルが存在しない場合のみ作成
            with open(self.csvFilePath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "FilePath", "Title", "Tag", "CreatedAt"])
            print(f"{self.csvFilePath} initialized.")

    def add_folder(self, file_path):
        with open(self.csvFilePath, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            id = sum(1 for _ in open(self.csvFilePath, encoding='utf-8'))  # ヘッダーを含む行数
            tag = os.path.basename(file_path)
            title = tag + "_Animation"
            created_at = datetime.now().strftime('%Y-%m-%d')
            writer.writerow([id, file_path, title, tag, created_at])
        print(f"Folder added: {file_path}")

    def remove_folder(self, tag):
        if not os.path.exists(self.csvFilePath):
            print(f"{self.csvFilePath} does not exist.")
            return

        temp_file = self.csvFilePath + ".tmp"
        with open(self.csvFilePath, mode='r', newline='', encoding='utf-8') as infile, \
            open(temp_file, mode='w', newline='', encoding='utf-8') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            deleted = False
            for row in reader:
                if row["Tag"] == tag:
                    deleted = True
                    folder_path = row["FilePath"]
                    # フォルダ削除の処理
                    if os.path.exists(folder_path):
                        try:
                            shutil.rmtree(folder_path)  # フォルダを削除
                            print(f"Deleted folder on disk: {folder_path}")
                        except Exception as e:
                            print(f"Failed to delete folder {folder_path}: {e}")
                    else:
                        print(f"Folder does not exist: {folder_path}")

                    print(f"Deleted entry from CSV with tag {tag}")
                else:
                    writer.writerow(row)

        os.replace(temp_file, self.csvFilePath)
        if not deleted:
            print(f"No entry found with tag {tag}")

    def get_nth_entry(self, n):
        """n番目に登録されたファイルのパス、タグ、日時を返す関数。"""
        if not os.path.exists(self.csvFilePath):
            print(f"{self.csvFilePath} does not exist.")
            return -1

        with open(self.csvFilePath, mode='r', newline='', encoding='utf-8') as file:
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

    def read_videos(self):
        videos = []
        with open(self.csvFilePath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                videos.append(row)
        return videos

    def search_videos(self, tag):
        results = []
        with open(self.csvFilePath, mode='r', newline='', encoding='utf-8') as file:
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

    def search_registered_videos(self, tag):
        """登録されたパスの配下にある動画を検索する関数。"""
        results = []
        videos = pathDatabase.search_videos(self, tag)
        for video in videos:
            folder_path = video["FilePath"]
            if os.path.exists(folder_path):  # フォルダが存在する場合のみ探索
                mp4_files = pathDatabase.get_mp4_files(folder_path)
                results.extend(mp4_files)
        return results

if __name__ == "__main__":
    db = pathDatabase()
    entry = db.get_nth_entry(3)
    if entry:  # エントリが存在する場合のみ出力
        print(f"FilePath: {entry['FilePath']}, Tag: {entry['Tag']}, CreatedAt: {entry['CreatedAt']}")