# Funcionamento:
Apartir de um conjunto de fotos localizados na pasta 'fotos', são detectados as coordenadas dos rostos em cada uma delas, e extrai-se as caracteristicas de cada rosto onde os mesmos são armazenados em um arquivo serializado pickle com seu respectivo filename.
Após isso, extrai-se as caracteristicas da foto de referência da pessoa a ser encontrada e compara-se a distancia euclidiana das caracteristicas da pessoa X, com as de cada rosto encntrado no conjunto de fotos.

# Como testar:
1: Instalar 'Desktop development with C++ em https://visualstudio.microsoft.com/visual-cpp-build-tools/

2: Instalar as depêndencias do 'requirements.txt'

2: Colocar as todas as fotos na pasta 'fotos', e a foto de referencia na pasta referencia.

3: Rodar o features_to_file.py e depois o find_photos, as fotos onde a pessoa de referêcia aparece irão aparecer na pasta 'correspondencias'.
