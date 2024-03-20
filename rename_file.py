import os

# 디렉토리 경로
directory = "BeakJoon/Bronze"

# 디렉토리 내 모든 파일의 이름을 가져옴
file_names = os.listdir(directory)

# 파일 이름 변경
for filename in file_names:
    if filename.endswith(".py") and filename.startswith("PRO_"):
        # 새 파일 이름 생성 (PRO를 BOJ로 변경)
        new_filename = filename.replace("PRO_", "BOJ_")
        
        # 파일 이동 및 이름 변경
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"{filename} 파일의 이름이 {new_filename}으로 변경되었습니다.")
    else:
        print(f"{filename}은(는) 변경할 파일이 아닙니다.")
