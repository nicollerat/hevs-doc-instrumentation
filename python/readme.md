# Utilisation des notebooks

Ces notebook jupyter peuvent être lu avec Jupyterlab

Attention : Le contenu peut être mis à jour pour corriger des erreurs ou améliorer la cohérence

# Précédure d'installation

1. Installer python
    * https://www.python.org/downloads/
    
    * Python s'installe dans un répertoire de l'utilisateur. Si nécessaire ajouter un path à la variable path pour avoir un lien sur le répertoire de base et sur le répertoire Scripts
    
    * Depuis un terminal (menu démarrer|<cmd>), python doit démarrer ainsi que pip. vérifiez que c'est bien le cas et que les bonnes version sont référées.
    
```
    C:\Users\marc.nicoller>python --version
    Python 3.11.2

    C:\Users\marc.nicoller>pip --version
    pip 23.2.1 from C:\Users\marc.nicoller\AppData\Local\Programs\Python\Python311\Lib\site-packages\pip (python 3.11)
```

2. Installer jupyterlab (depuis la lig
    * pip install jupyterlab
    
3. Installer les librairies
    * pip install scikit-learn
    * pip install matplotlib
    * pip install seaborn
    * pip install numpy
    * pip install scipy
    * ... si elles manquent, il suffit de faire pip install *ce_qui_manque*
    
4. Depuis le répertoire des notebook, lancer jupyter
    * Ouvrir un terminal, aller dans le répertoire des scripts
```
    >cd hevs-doc-instrumentation/python
    >jupyter lab
```

     * Une fenêtre de l'explorateur par défaut s'ouvre sur l'environnement Jupyterlab
     * Jouer un peu avec les scripts !
     
     
 # Contenu
 
 - Les exercices commencent par ex_nom-du-sujet.ipynb
 - Les solutions se terminent par _sol
 
 D'autres notebooks sont donnés pour info.
 
 
