# Revue3EI_IA
Ce repo contient des codes utilisés dans certains article de la Revue 3EI sur l'intelligence artificielle. Seul les articles "Introduction à l'IA" et "Réseaux de neurones" sont concernés par les fichiers présents dans ce dépôt

# Contenu du dépot
Le dépot contient à la racine des fichiers utilisés pour créer les figures des articles et les fichiers contenant les exemples.
* *mnist.ipynb* est un jupyter notebook permettant de visualiser les images et les labels de la base de donnée MNIST
* *fonctions_activation.ipynb* est un jupyter notebook permettant de tracer plusieurs fonctions d'activation différentes
* *MLP_sklearn.py* est un exemple de MLP basé sur la bibliothèque scikit learn. Cet exemple défini et entraine un MLP permettant de classifier les chiffres manuscripts de la base de donnée MNIST
* *supervised.ipynb* est un jupyter notebook présentant les tracés d'erreur dans le cadre de régression linéaire. Ce fichier présente aussi les données labélisées des Iris de Fisher. L'algorithme des k plus proche voisins n'est pas encore implémenté
* *unsupervised.ipynb* est un jupyter notebook présentant l'algorithme des k moyennes basé sur les données des Iris de Fisher. Les centres initiaux sont définis aléatoirement.
Les fichiers utilisant les données de la bases des Iris de Fisher ne considèrent que les colonnes 3 et 4 (numérotées 2 et 3), correspondant à la longueur et à la largeur des pétales. Les sépales ne sont pas utilisées dans ces exemples.

* Le dossier **Exemple tensorflow** donne deux exemples d'utilisation de tensorflow pour définir des réseaux de neurones. L'un des deux présente la reconnaissance de chiffres manuscript et l'autre montre l'utilisation d'un GAN (réseaux adverses). Ces deux exemples sont basé sur les exemples fournis par [tensorflow](https://www.tensorflow.org/tutorials?hl=fr)
* Le dossier **NN_simple** présente une réalisation et un entrainement d'un MLP n'utilisant aucune bibliothèque prédéfini. Cet exemple est largement perfectible, notament pour l'utilisation de quelques méthodes telles que [autograd](https://github.com/HIPS/autograd). Il reste cependant intéressant pour présenter le fonctionnement réel d'un MLP. L'utilisation de bibliothèque existante (pytorch, tensorflow, scikit learn...) permet toutefois d'obtenir plus rapidement un résultat plus polyvalent et généralement plus performant.

# Bibliothèques Python nécessaires
Pour pouvoir exécuter tous les fichiers de ce dépôt il est nécessaire d'avoir jupyter notebook. Au besoin, [Google Colaboratory](https://colab.research.google.com/) permet l'exécution de notebooks.
Les fichiers de ce dépôt demandent également un certain nombre d'installation de bibliothèques :
* tensorflow
* scikit learn (sklearn)
* pandas
* numpy
* matplotlib
