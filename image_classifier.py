import glob
import os
import shutil

INPUT_FOLDER = None
OUTPUT_FOLDER = None


def create_output_folder(folder_path):
    os.makedirs(folder_path)


def mupltiple_folders_in_input_folder(input_folder):
    # 입력 폴더 내에 여러 개의 폴더가 있는지 확인하는 로직 구현
    # 예시: 입력 폴더 내에 "album1", "album2" 등의 폴더가 있는지 확인
    folder_list = [f.path for f in os.scandir(input_folder) if f.is_dir()]
    return folder_list


def search_images_in_folder(folder_path):
    if mupltiple_folders_in_input_folder(folder_path):
        for sub_folder in mupltiple_folders_in_input_folder(folder_path):
            search_images_in_folder(sub_folder)
    # 이미지 파일만 가져오기
    file_list = glob.glob(folder_path + '/*.jpg') + glob.glob(folder_path + '/*.jpeg') + glob.glob(folder_path + '/*.png') + glob.glob(folder_path + '/*.bmp') + glob.glob(folder_path + '/*.gif') + glob.glob(folder_path + '/*.tiff') + glob.glob(folder_path + '/*.webp')
    return file_list


def reorganize_images_by_name(file_list):
    # 이미지 파일들을 이름에 따라 앨범별로 재정렬하는 로직 구현
    # 예시: "album1_image1.jpg" -> "album1" 앨범에 추가
    album_dict = {"FCMobile-Highlights": [], "Screenshot": [], "WhatsApp": [], "Instagram": [], "Camera": []}
    for file in file_list:
        # 파일 이름에서 앨범 이름 추출 (예: "album1_image1.jpg" -> "album1")
        album_name = file.split('/')[-1].split('_' or '-')[0]  # 파일 경로에서 파일 이름만 추출 후 앨범 이름 추출
        if album_name not in album_dict:
            album_dict[album_name] = []
        album_dict[album_name].append(file)
        # 아무 태그도 없으면 camera로 분류
        if not album_name:
            album_dict["Camera"].append(file)
    return album_dict


def print_album_contents(album_dict):
    for album, files in album_dict.items():
        print(f"Album: {album}, Number of images: {len(files)}")
        for file in files:
            print(f" - {file}")


def duplicate_images_in_album(album_dict):
    for album, files in album_dict.items():
        if len(files) > 1:
            print(f"Album: {album} has {len(files)} images. Duplicating images...")
            for file in files:
                # 이미지 파일을 복제 (예: shutil.copy(file, new_file_path))
                print(f"Duplicating {file} in album {album}...")
                # 실제 복제 로직은 shutil.copy를 사용하여 구현할 수 있습니다.
                shutil.copy(file, f"{OUTPUT_FOLDER}/{album}_{os.path.basename(file)}")


def main():
    # 사용자로부터 입력 폴더와 출력 폴더 경로를 받기
    INPUT_FOLDER = input("Enter the folder path containing images: ")
    OUTPUT_FOLDER = input("Enter the folder path to save duplicated images: ")
    if not os.path.exists(INPUT_FOLDER):
        print("Input folder does not exist. Please check the path and try again.")
        return
    if not os.path.exists(OUTPUT_FOLDER):
        print("Output folder does not exist. Creating output folder...")
        create_output_folder(OUTPUT_FOLDER)
    # 이미지 파일만 가져오기
    file_list = search_images_in_folder(INPUT_FOLDER)
    # 이미지 파일들을 이름에 따라 앨범별로 재정렬
    album_dict = reorganize_images_by_name(file_list)
    for album, files in album_dict.items():
        print(f"Album: {album}, Number of images: {len(files)}")
        for file in files:
            print(f" - {file}")
    # 앨범별로 이미지 복제
    duplicate_images_in_album(album_dict)


if __name__ == "__main__":
    main()