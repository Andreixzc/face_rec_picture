# How it works:
From a set of photographs located in the 'fotos' folder, we detect the coordinates of the faces in each image. We then extract the distinctive features of each face, which are stored in a serialized file in pickle format, along with the name of the corresponding file.

After this stage, we extract the features of the face of the reference person we want to find. We then compare the Euclidean distance between the features of individual X and the features of each face identified in the set of photographs.

This analysis allows us to identify possible matches, taking into account the proximity of the facial features. In this way, it is possible to determine which faces in the photographs are similar to those of the reference person, facilitating the desired location.


#How to test it:
1: Install 'Desktop development with C++' from https://visualstudio.microsoft.com/visual-cpp-build-tools/

2: Install the 'requirements.txt' dependencies (pip install -r requirements.txt)

2: Put all the photos in the 'fotos' folder, and the reference photo in the reference folder.

3: Run features_to_file.py and then find_photos, the photos where the reference person appears will appear in the 'correspondencias' folder.
