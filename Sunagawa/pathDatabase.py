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
            title = tag + "_Animation.mp4"
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

    def read_data(self):
        folders = []
        with open(self.csvFilePath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if os.path.exists(row["FilePath"]):
                    folders.append(row)
                else:
                    self.remove_folder(row["Tag"])
        return folders
    
    def get_video(self):
        videos = []
        with open(self.csvFilePath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                videoPath = os.path.join(row["FilePath"], row['Title'])
                if os.path.exists(videoPath):
                    videos.append(row)
        return videos


if __name__ == "__main__":
    pass