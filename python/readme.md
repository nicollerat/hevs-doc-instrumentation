## Ces notebook jupyter peuvent être lu avec Jupyterlab

Précédure d'installation

1. Installer python
    * https://www.python.org/downloads/
    
    * Python s'installe dans un répertoire de l'utilisateur. Si nécessaire ajouter un path à la variable path pour avoir un lien sur le répertoire de base et sur le répertoire Scripts
    
    * A la ligne de commande, python doit démarrer ainsi que pip. vérifiez que c'est bien le cas et que les bonnes version sont référées.
    
```
    C:\Users\marc.nicoller>python --version
    Python 3.11.2

    C:\Users\marc.nicoller>pip --version
    pip 23.2.1 from C:\Users\marc.nicoller\AppData\Local\Programs\Python\Python311\Lib\site-packages\pip (python 3.11)
```

1. Installer jupyterlab
    * pip install jupyterlab
    
1. Installer les librairies
    * pip install scikit-learn
    * pip install matplotlib
    * pip install seaborn
    * pip install numpy
    * pip install scipy
    * ... si elles manquent, il suffit de faire pip install *ce qui manque*
    
1. Depuis le répertoire des notebook, lancer jupyter
    * jupyter lab