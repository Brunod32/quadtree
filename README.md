# Evaluation Arbre quaternaire

## Description:
Un quadtree ou arbre quaternaire (arbre Q) est une structure de données de type arbre dans laquelle chaque nœud a quatre fils.
Les quadtrees sont le plus souvent utilisés pour partitionner un espace bidimensionnel en le subdivisant récursivement en quatre nœuds.

Il existe plusieurs types de quadtree. Dans notre cas il s'agit d'un quadtree "region".
Le quadtree «région» représente une partition de l'espace en deux dimensions en décomposant la région en quatre quadrants égaux, puis chaque quadrant en quatre sous-quadrants, et ainsi de suite, avec chaque «nœud terminal» comprenant des données correspondant à une sous-région spécifique. Chaque nœud de l'arbre a exactement : soit quatre enfants, soit aucun (cas d'un nœud terminal).
Chaque Noeud comportant quatre éléments. Il s'agit d'une technique connue pour l'encodage d'images.  Pour simplifier, les images sont carrées, de couleur noir et blanc
et de côté 2^n.

## Cloner le projet:
```git clone https://github.com/Brunod32/quadtree.git```

## L'environnement virtuel:
### Créer l'environnement:
Saisissez la commande suivante dans un terminal:

```python -m venv <environment name>```

### Activer l'environnement sous Windows avec la commande:
```env/Scripts/activate.bat```:

### Activer l'environnement sous Linux avec la commande:
```source env/bin/activate```

### Désactiver l'environnement:
```deactivate```

## Installer les packages contenus dans le requirements.txt
```pip install -r requirements.txt```
