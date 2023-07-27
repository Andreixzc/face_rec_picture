import cv2
import face_recognition

def extract_face_features(image_path):
    # Carregar a imagem usando face_recognition
    image = face_recognition.load_image_file(image_path)
    
    # Obter os encodings (características) do rosto
    face_encodings = face_recognition.face_encodings(image)
    
    if len(face_encodings) > 0:
        # Retornar as características do primeiro rosto encontrado
        return face_encodings[0]
    else:
        return None

def recognize_faces(image_path, known_face_features, tolerance=0.6):
    # Carregar a imagem usando OpenCV
    image = cv2.imread(image_path)
    
    # Encontrar as coordenadas dos rostos na imagem usando Haar Cascade
    face_locations = face_recognition.face_locations(image)
    print("face locations:")
    print(face_locations)
    
    # Obter os encodings (características) de todos os rostos encontrados
    face_encodings = face_recognition.face_encodings(image, face_locations)
    
    # Inicializar a lista para armazenar as correspondências encontradas
    matches = []
    
    for face_encoding in face_encodings:
        # Comparar as características do rosto com as características conhecidas
        face_distances = face_recognition.face_distance(known_face_features, face_encoding)
        
        # Verificar se alguma correspondência está acima do limite de tolerância
        name = "Desconhecido"
        if any(face_distance <= tolerance for face_distance in face_distances):
            # Encontrou uma correspondência
            index = face_distances.argmin()
            name = f"Pessoa {index + 1}"
        
        matches.append(name)
    
    return matches

if __name__ == "__main__":
    person_x_image_path = "Screenshot_1.png"
    images_y_path = ["1.jpeg", "2.jpg"]
    
    person_x_features = extract_face_features(person_x_image_path)

    print(person_x_features)
    
    if person_x_features is not None:
        # Reconhecer os rostos nas imagens do conjunto Y
        for image_path in images_y_path:
            matches = recognize_faces(image_path, [person_x_features])
            print(f"Imagem: {image_path} - Correspondências: {matches}")
    else:
        print("Nenhum rosto encontrado na imagem de referência da pessoa X.")

