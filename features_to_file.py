import os
import face_recognition
import pickle

def extract_face_features(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    
    return face_encodings

def load_images_from_folder(folder_path):
    images = {}
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
        face_encodings = extract_face_features(img_path)
        images[filename] = face_encodings
    return images

if __name__ == "__main__":
    images_y_folder_path = "fotos"
    features_folder = "face_features_pickles"
    
    os.makedirs(features_folder, exist_ok=True)
    
    images_face_features = load_images_from_folder(images_y_folder_path)

    for image_file, face_features in images_face_features.items():
        pickle_file_path = os.path.join(features_folder, os.path.splitext(image_file)[0] + ".pkl")
        with open(pickle_file_path, "wb") as pickle_file:
            pickle.dump(face_features, pickle_file)
