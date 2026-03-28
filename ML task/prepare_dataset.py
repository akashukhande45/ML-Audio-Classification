import os
import numpy as np
from feature import extract_features   # ✅ correct import

data = []
labels = []


dataset_path = r"C:/Users/akash/Desktop/ML task/G9/archive (2)"

for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)

    if not os.path.isdir(folder_path):
        continue

    print("Folder:", folder)

    for file in os.listdir(folder_path):
        if file.endswith(".wav"):
            file_path = os.path.join(folder_path, file)

            try:
                features = extract_features(file_path)
                data.append(features)
                labels.append(folder)

            except Exception as e:
                print("Error processing:", file_path)
                print("Error:", e)


X = np.array(data)
y = np.array(labels)


np.save("X.npy", X)
np.save("y.npy", y)

print("\nDataset prepared successfully!")
print("X shape:", X.shape)
print("y shape:", y.shape)