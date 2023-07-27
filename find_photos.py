import os
import cv2
import face_recognition
import pickle
import shutil
TRESHOLD = 0.7
def extract_face_features(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    
    if len(face_encodings) > 0:
        return face_encodings[0]
    else:
        return None

if __name__ == "__main__":
    reference_folder = "referencia"
    features_folder = "face_features_pickles"
    correspondence_folder_path = "correspondencias"
    
    # Get the reference image filename from the 'referencia' folder
    reference_image_filename = os.listdir(reference_folder)[0]
    reference_image_path = os.path.join(reference_folder, reference_image_filename)
    
    person_x_features = extract_face_features(reference_image_path)

    print(person_x_features)
    
    if person_x_features is not None:
        os.makedirs(correspondence_folder_path, exist_ok=True)
        
        matching_photos = []
        
        for pickle_file in os.listdir(features_folder):
            pickle_file_path = os.path.join(features_folder, pickle_file)
            
            # Get the image filename without extension
            image_file_name = os.path.splitext(pickle_file)[0]
            image_file_with_ext = None
            
            # Find the corresponding image file with different extensions in the "fotos" folder
            for ext in [".png", ".jpg", ".jpeg"]:
                image_file_with_ext = os.path.join("fotos", image_file_name + ext)
                if os.path.isfile(image_file_with_ext):
                    break
            
            if image_file_with_ext is not None:
                with open(pickle_file_path, "rb") as pickle_file:
                    face_features_list = pickle.load(pickle_file)
                    
                    # Check if the reference person's face features match with any of the faces in the pickle file
                    for face_features in face_features_list:
                        distance = face_recognition.face_distance([face_features], person_x_features)
                        if distance <= TRESHOLD:
                            matching_photos.append(image_file_with_ext)
                            break
            else:
                print(f"Erro: Imagem {image_file_name} não encontrada.")
        
        if matching_photos:
            print("A pessoa de referência está presente nas seguintes fotos:")
            for photo in matching_photos:
                print(photo)
                image_file_name = os.path.basename(photo)
                image_dst_path = os.path.join(correspondence_folder_path, image_file_name)
                shutil.copyfile(photo, image_dst_path)
        else:
            print("A pessoa de referência não foi encontrada em nenhuma das fotos.")
    else:
        print("Nenhum rosto encontrado na imagem de referência da pessoa X.")
