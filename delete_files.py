import os


def delete_files(folder_path, delete_file_type):
    try:
        # 檢查資料夾是否存在
        if not os.path.exists(folder_path):
            print(f"資料夾 '{folder_path}' 不存在")
            return

        # 遞迴地取得資料夾中的所有檔案及子資料夾
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # 檢查檔案是否以 delete_file_type 結尾
                if file.endswith(delete_file_type):
                    file_path = os.path.join(root, file)
                    # 刪除檔案
                    os.remove(file_path)
                    print(f"已刪除檔案: {file_path}")

        print(f"已完成刪除 '{folder_path}' 及其子資料夾中的所有'.pth'檔案")

    except Exception as e:
        print(f"發生錯誤: {e}")

# 設定要刪除的資料夾路徑和指定副檔名
target_folder_path = "/path/to/your/target/folder"
delete_file_type=".pth"

# 呼叫函式刪除指定資料夾及其子資料夾中的所有指定附檔名的檔案
delete_pth_files(target_folder_path, delete_file_type)
