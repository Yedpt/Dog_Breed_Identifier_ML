# backend/ML/training/data_preprocessor.py
import cv2
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import albumentations as A
import torch
from torch.utils.data import Dataset, DataLoader

class DogBreedDataset(Dataset):
    def __init__(self, image_paths, labels, transform=None, img_size=(224, 224)):
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform
        self.img_size = img_size
        
    def __len__(self):
        return len(self.image_paths)
    
    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        label = self.labels[idx]
        
        image = cv2.imread(str(img_path))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, self.img_size)
        
        if self.transform:
            image = self.transform(image=image)['image']
            
        return image, label

class DataPreprocessor:
    def __init__(self, dataset_path):
        self.dataset_path = Path(dataset_path)
        self.images_path = self.dataset_path / "images" / "Images"
        self.label_encoder = LabelEncoder()
        
    def prepare_data(self, test_size=0.2, val_size=0.1, random_state=42):
        print("🔄 Preparando datos...")
        
        image_paths = []
        breed_names = []
        
        for breed_folder in self.images_path.iterdir():
            if breed_folder.is_dir():
                breed_name = breed_folder.name.split('-')[-1]
                for img_path in breed_folder.glob("*.jpg"):
                    image_paths.append(img_path)
                    breed_names.append(breed_name)
        
        labels_encoded = self.label_encoder.fit_transform(breed_names)
        
        print(f"✅ Total imágenes: {len(image_paths)}")
        print(f"✅ Razas únicas: {len(self.label_encoder.classes_)}")
        
        # Split 80% train, 10% val, 10% test
        train_paths, temp_paths, train_labels, temp_labels = train_test_split(
            image_paths, labels_encoded, 
            test_size=test_size + val_size,
            stratify=labels_encoded,
            random_state=random_state
        )
        
        val_ratio = val_size / (test_size + val_size)
        val_paths, test_paths, val_labels, test_labels = train_test_split(
            temp_paths, temp_labels,
            test_size=1 - val_ratio,
            stratify=temp_labels,
            random_state=random_state
        )
        
        print(f"📊 Train: {len(train_paths)}")
        print(f"📊 Validation: {len(val_paths)}")
        print(f"📊 Test: {len(test_paths)}")
        
        return (train_paths, train_labels, 
                val_paths, val_labels, 
                test_paths, test_labels)
    
    def get_transforms(self):
        train_transform = A.Compose([
            A.Resize(224, 224),
            A.HorizontalFlip(p=0.5),
            A.RandomRotate90(p=0.3),
            A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0.2, rotate_limit=15, p=0.5),
            A.RandomBrightnessContrast(p=0.3),
            A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        
        val_transform = A.Compose([
            A.Resize(224, 224),
            A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        
        return train_transform, val_transform