import csv
import os
import shutil
from datetime import datetime

class pathDatabase:
    def __init__(self):
        self.csvFilePath = "C:/Users/gunda/projectExperiments/Sunagawa/folderPaths.csv"
        self.pickle_file = "C:/Users/gunda/projectExperiments/Sunagawa/assets/pickles"

    def initialize_csv(self):
        if not os.path.exists(self.csvFilePath):  # ファイルが存在しない場合のみ作成
            with open(self.csvFilePath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "FilePath", "Title", "Tag", "CreatedAt"])
        else:
            print(True)

    def add_folder(self, file_path):
        with open(self.csvFilePath, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            id = sum(1 for _ in open(self.csvFilePath, encoding='utf-8'))  # ヘッダーを含む行数
            tag = os.path.basename(file_path)
            title = tag + "_Animation.mp4"
            created_at = datetime.now().strftime('%Y-%m-%d')
            writer.writerow([id, file_path, title, tag, created_at])

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
        os.remove(os.path.join(self.pickle_file, tag + ".pkl"))
        if not deleted:
            print(f"No entry found with tag {tag}")

    def read_data(self):
        folders = []
        temp_file = self.csvFilePath + ".tmp"

        with open(self.csvFilePath, mode='r', newline='', encoding='utf-8') as infile, \
            open(temp_file, mode='w', newline='', encoding='utf-8') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if os.path.exists(row["FilePath"]):
                    folders.append(row)
                    writer.writerow(row)
        
        os.replace(temp_file, self.csvFilePath)

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
    
    def get_video_from_tag(self, tag):
        with open(self.csvFilePath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["tag"] == tag:
                    videoPath = os.path.join(row["FilePath"], row['Title'])
                    if os.path.exists(videoPath):
                        return videoPath
    
    def has_tag(self, tag):
        if not os.path.exists(self.csvFilePath):
            print(f"{self.csvFilePath} does not exist.")
            return False

        with open(self.csvFilePath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Tag"] == tag:
                    return True
        return False
    
    def update_video_title(self, tag, new_title):
        temp_file = self.csvFilePath + ".tmp"
        updated = False
        
        with open(self.csvFilePath, mode='r', newline='', encoding='utf-8') as infile, \
            open(temp_file, mode='w', newline='', encoding='utf-8') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if row["Tag"] == tag:
                    old_path = os.path.join(row["FilePath"], row["Title"])
                    row["Title"] = new_title
                    new_path = os.path.join(row["FilePath"], row["Title"])
                    os.rename(old_path, new_path)
                    updated = True
                writer.writerow(row)

        os.replace(temp_file, self.csvFilePath)
        if not updated:
            print(f"No entry found with tag {tag}")

    def update_tag(self, old_tag, new_tag):
        temp_file = self.csvFilePath + ".tmp"
        updated = False
        
        with open(self.csvFilePath, mode='r', newline='', encoding='utf-8') as infile, \
            open(temp_file, mode='w', newline='', encoding='utf-8') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if row["Tag"] == old_tag:
                    old_path = row["FilePath"]
                    new_path = os.path.join(os.path.dirname(row["FilePath"]), new_tag)
                    row["Tag"] = new_tag
                    row["FilePath"] = new_path
                    os.rename(old_path, new_path)
                    updated = True
                writer.writerow(row)

        os.replace(temp_file, self.csvFilePath)
        if not updated:
            print(f"No entry found with tag {old_tag}")


if __name__ == "__main__":
    pass