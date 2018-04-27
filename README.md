# UdeM - Technical interview, Level 1

**Question**

Expliquez les compromis en espace et en temps entre un tableau et une liste chaînée, dans des termes que ma grand-mère pourrait comprendre.

<details>
 <summary><b>Answer (in french)</b></summary>

Un tableau est une représentation linéaire de plusieurs valeurs représentées en mémoire aussi appelées une liste. Un tableau est une abstraction faite pour la représenter sous la forme de deux dimensions; c'est une solution qui prend l'espace nécessaire de la valeur à représenter. Par contre, cela vous prendra plus de temps pour présenter différemment les valeurs, car vous êtes obligé de déplacer ces valeurs en mémoire.

Une liste chainée est une abstraction qui est utilisée pour représenter une liste d'élément (un tableau si vous voulez) présent en mémoire;
La liste chainée est plus gourmande en termes d'espace mémoire, car elle demande de l'espace mémoire pour la valeur de l'adresse qui pointe sur la prochaine valeur en mémoire; elle est plus rapide en temps si vous voulez trier ou présenter les valeurs différemment.

**Version grand-mère**:

Prenons par exemple un jeu de cartes. On vous donne 5 cartes face cachée. Une fois que vous avez vos cartes en possession, vous avez deux scénarios avant de commencer à jouer votre première carte:

Scénario 1 -- liste (tableau):
Vous prenez vos cartes et commencez à analyser vos cartes et les trier de la plus petite valeur à la plus grande valeur de votre main. Vous êtes d'accord que cela prend un certain temps pour trier vos cartes. Par la suite, il sera plus facile de repérer vos cartes dans votre main.

Scénario 2 -- liste chainée:
Vos cartes sont face cachée et elles sont présentées enlignées devant vous. On vous fournit la liste des cartes sur un bout de papier. On vous dit que l'as de pique est la deuxième carte à partir de la gauche; la dame de coeur est votre quatrième carte, ainsi de suite. De plus cette liste est triée par ordre de grandeur et par couleur.

On complexifie le jeu. Faisons le même exercice, mais on vous donne 100 000 cartes!

Q1: Lequels des scénarios 1 et 2 vous allez être plus rapide pour jouer?
R:

Le scénario 2, car vos cartes seront déjà triées (par couleur et ordre de grandeur) sur votre bout de papier. De plus, vous allez être plus rapide pour jouer une carte!

Si vous optez pour le scénario 1, vous comprendrez qu'il sera possible de trouver la bonne carte à jouer; il sera plus facile de trier vos cartes et par le fait même de retrouver votre carte.

En conclusion, tout dépend de ce que vous voulez faire en termes d'espace (votre bout de papier). Vous comprendrez que vous allez devoir sortir une feuille d'une dimension adéquate pour indexer la position de chacune de vos cartes. Grâce à cet index, vous allez pouvoir trouver votre carte à jouer plus rapidement. Par contre, si vous n'avez pas de papier, vous allez devoir trier votre carte qui est très couteuse en temps.

Recommandation : Si vous avez à trier plusieurs fois vos cartes selon la situation, il est recommandé d'utiliser la technique de la liste chainée pour économiser de temps.

</details>

## Part 1 : (Simple) Data Processing

How to

```
$ cd part1
$ chmod u+x parser.py
$ parser.py -i <file1> [-i file2[, -i fileN]]
```

Test with the actual text files:

```
$parser.py -i test.txt -i test2.txt -i test3.txt -i test4.txt
```

Run partial unit test (in progress)

```
$ pip3 install -U pytest
$ pytest test_parser.py -s
```

## Part 2 : SQL

I use MySQL 5.7.21

See `create.sql` and `req.sql`

