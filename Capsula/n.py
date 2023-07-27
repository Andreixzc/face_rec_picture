import os
import cv2
import face_recognition

def extract_face_features(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    
    if len(face_encodings) > 0:
        return face_encodings[0]
    else:
        return None

def recognize_faces(known_face_features, image, tolerance=0.6):
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    
    matches = []
    
    for face_encoding in face_encodings:
        face_distances = face_recognition.face_distance(known_face_features, face_encoding)
        name = "Desconhecido"
        if any(face_distance <= tolerance for face_distance in face_distances):
            index = face_distances.argmin()
            name = f"Pessoa {index + 1}"
        matches.append(name)
    
    return matches

def load_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)
        if img is not None:
            images.append(img)
    return images

def compare_with_folder_images(person_x_features, folder_path):
    images = load_images_from_folder(folder_path)
    all_matches = []
    
    for img in images:
        matches = recognize_faces([person_x_features], img)
        all_matches.append(matches[0])
        
    return all_matches

if __name__ == "__main__":
    person_x_image_path = "Screenshot_1.png"
    images_y_folder_path = "fotos"
    person_x_features = extract_face_features(person_x_image_path)
    if person_x_features is not None:
        matches_list = compare_with_folder_images(person_x_features, images_y_folder_path)
        for idx, image_file in enumerate(os.listdir(images_y_folder_path)):
            print(f"Imagem {idx+1}: {image_file} - Correspondências: {matches_list[idx]}")
    else:
        print("Nenhum rosto encontrado na imagem de referência da pessoa X.")
