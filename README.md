# calculs_jdr_systeme_custom

## Description :

Ce script python contient plusieurs fonctions qui permettent : de calculer le nombre de points d'expérience que donne une créature, le nombre de points d'expérience par niveau dont une créature aura besoin pour passer au niveau supérieur, une fonction qui calcule le nombre de points de style acquis durant un combat pour donner un grade au joueur, et une fonction qui permet d'arrondir les nombres.

## Comment s'en servir ? 

Pour l'instant, il est possible de se servir du script uniquement dans Pyzo. Il suffit d'exécuter le fichier, puis d'appeler une des fonctions.

### Fonctions :

* **set_nombre(nombre)**

  Cette fonction attend qu'on lui passe un nombre en paramètre pour l'arrondir à 0 ou à 5. Elle est déjà utilisée dans les autres fonctions.
  
* **get_experience_ennemi(niveau, nature, indice_menace)**
  
  Cette fonction retourne le nombre total de points d'expérience que rapporte la créature en fonction de :
    - son niveau, sachant que les niveaux vont de 1 à 20;
    - sa nature, il y a plusieurs natures possibles : Humanoïdes, Bête, Démon, Inorganique, Volatiles,       Aquatique, Revenants, Fée, Dragon, Inconnu, Titan, Déité
    - de son indice de menace : l'indice de menace est calculé dans un fichier Excel en fonction de(s)       critère(s) que la créature rempli(s)

* **get_courbe_experience(progression, base_experience, creature)**
  
  Cette fonction retourne le nombre d'expérience requis par niveau pour atteindre le niveau suivant :
    - il y a trois types de progressions : *Rapide*, *Moyenne*, *Lente*
    - la base d'expérience est le nombre de points d'expérience requis pour atteindre le niveau 2
    - si la créature est un *Personnage*, le nombre de niveau est de 20, si c'est un *Familier* le nombre de niveau est de 10

* **get_grade_combat(tour, nombre_combo, coups_recus, coup_grace, contre_attaque_reussie)**

  Cette fonction retourne le grade obtenu par les joueurs à la fin du combat en fonction :
    - du nombre de tour qu'il y a eu pour terminer le combat
    - du nombre de combo qu'il y a eu durant le combat
    - du nombre de coups reçus par l'équipe **globalement**
    - s'il y a eu un coup de grâce
    - si au moins **une** contre-attaque a été réussie
