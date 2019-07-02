# AlgoProjetData

## SUJET :

Le but de votre étude est de générer une tournée de livraison (problème du VRP). Le problème algorithmique consiste donc à calculer sur un réseau routier une tournée permettant de relier entre elles un sous-ensemble de villes, puis de revenir à son point de départ, de manière à minimiser la distance totale parcourue.

Vous devrez proposer une méthode issue de la Recherche Opérationnelle pour générer une tournée de livraison correspondant à ce problème. L’implémentation se fera sur une version de base du problème, à laquelle vous pourrez ajouter des contraintes supplémentaires, rendant le problème plus réaliste, mais aussi plus dur à traiter.

Par ailleurs, vous devrez effectuer une étude statistique du comportement de votre méthode de résolution, faisant apparaitre ses performances (qualité de solution, temps de convergence). Idéalement, des statistiques prédictives permettent d’extrapoler ce comportement sur des cas d’usages que vos ordinateurs seuls ne pourraient traiter.

## generateData.py

Le fichier generateData.py est un script de génération de data sous format JSON

Il demande 2 entrées à l'utilisateur :

1.  Un nombre de villes à générer
2.  Le nom du fichier sous lequel les données vont être sauvegarder
    A noter que tous les fichiers générés seront sous format ".json" et dans le dossier "/data".

## displayDataOnGraph.py

Le fichier displayDataOnGraph.py est un script qui récupère les données d'un JSON et les affichent sous format graphique

Il demande 2 entrées à l'utilisateur :

1.  Un nom de fichier à utiliser (ex: monFichierJson.json)
2.  Le nom du fichier sous lequel le graph va être sauvegarder
    A noter que tous les fichiers générés seront sous format '.png' et dans le dossier '/graph'.

# Equipe

- Benjamin THIBAULT
- Théo FOMBASSO
- Martin HUBERT
- Maxence KRUGER
- Théo VANENGELANDT
