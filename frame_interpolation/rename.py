import os

def rename_frames_to_even_numbers(directory):
    # ディレクトリ内のファイル名を取得し、ソート
    frame_files = sorted([f for f in os.listdir(directory) if f.endswith(".png")])
    
    # 偶数番号にリネーム
    for index, filename in enumerate(frame_files):
        # 現在のファイルパス
        current_path = os.path.join(directory, filename)
        
        # 新しいファイル番号（偶数）
        new_index = (index + 1) * 2  # 1-based indexの偶数番号にする
        new_filename = f"frame_{new_index:04d}.png"
        new_path = os.path.join(directory, new_filename)
        
        # ファイルの名前を変更
        os.rename(current_path, new_path)
        print(f"Renamed {filename} to {new_filename}")

# フレームの入ったディレクトリのパス
frame_directory = "./interpolation_frame"
rename_frames_to_even_numbers(frame_directory)