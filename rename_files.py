import os
import csv
from datetime import datetime

def rename_and_log_files(folder_path, output_csv="report.csv"):
    renamed_files = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            full_path = os.path.join(folder_path, filename)
            modified_time = os.path.getmtime(full_path)
            new_name = datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d_%H-%M-%S") + ".pdf"
            new_full_path = os.path.join(folder_path, new_name)

            # Уникаємо конфлікту імен
            counter = 1
            while os.path.exists(new_full_path):
                new_name = datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d_%H-%M-%S") + f"_{counter}.pdf"
                new_full_path = os.path.join(folder_path, new_name)
                counter += 1

            os.rename(full_path, new_full_path)
            renamed_files.append((filename, new_name))

    # Створюємо CSV звіт
    with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Original Name", "New Name"])
        writer.writerows(renamed_files)

    print(f"[✓] Renamed {len(renamed_files)} files. Report saved to {output_csv}")

# === ВИКОРИСТАННЯ ===
if __name__ == "__main__":
    folder = input("Enter the path to the folder with PDF files: ")
    rename_and_log_files(folder)