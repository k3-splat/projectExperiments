import os
import glob
from tqdm import tqdm
import cv2
from chooseProjectView import projectList
from pathDatabase import pathDatabase

class makeVideo:
    def __init__(self):
        db = pathDatabase()
        self.projectname = projectList.getprojectName()
        self.input_dir = 'C:/Users/gunda/projectExperiments/Sunagawa/assets/canvases'           # 入力する画像が保存されたフォルダ名
        self.output_path = os.path.join(db.get_path_from_tag(self.projectname), db.get_title_from_tag(self.projectname)) # 作成する 動画ファイル
        print(self.output_path)

    def makeVideo(self, fps):
        # フォルダ内の画像のファイルリストを取得する
        files  = glob.glob(os.path.join(self.input_dir, f'{self.projectname}*.png'))
        files.sort()
        frames=len(files)
        assert frames != 0, 'not found image file'    # 画像ファイルが見つからない

        # 最初の画像の情報を取得する
        img = cv2.imread(files[0])
        h, w, channels = img.shape[:3]

        # 作成する動画
        codec = cv2.VideoWriter.fourcc(*'mp4v')
        #codec = cv2.VideoWriter_fourcc(*'avc1')
        writer = cv2.VideoWriter(self.output_path, codec, fps, (w, h),1)

        bar = tqdm(total=frames, dynamic_ncols=True)
        for f in files:
            # 画像を1枚ずつ読み込んで 動画へ出力する
            img = cv2.imread(f)
            writer.write(img)   
            bar.update(1)
            
        bar.close()
        writer.release()