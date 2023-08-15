# Funcionamento:
A partir de um conjunto de fotografias localizado na pasta 'fotos', realizamos a detecção das coordenadas dos rostos presentes em cada imagem. Posteriormente, procedemos com a extração das características distintivas de cada rosto, as quais são armazenadas em um arquivo serializado no formato pickle, juntamente com o nome do arquivo correspondente.

Após essa etapa, efetuamos a extração das características do rosto da pessoa de referência que desejamos encontrar. Em seguida, realizamos a comparação utilizando a distância euclidiana entre as características do indivíduo X e as características de cada rosto identificado no conjunto de fotografias.

Essa análise nos permite identificar possíveis correspondências, considerando a proximidade das características faciais. Dessa forma, é possível determinar quais rostos nas fotografias se assemelham ao da pessoa de referência, facilitando a localização desejada.


# Como testar:
1: Instalar 'Desktop development with C++ em https://visualstudio.microsoft.com/visual-cpp-build-tools/

2: Instalar as depêndencias do 'requirements.txt' (pip install -r requirements.txt)

2: Colocar as todas as fotos na pasta 'fotos', e a foto de referencia na pasta referencia.

3: Rodar o features_to_file.py e depois o find_photos, as fotos onde a pessoa de referêcia aparece irão aparecer na pasta 'correspondencias'.
