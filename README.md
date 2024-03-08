# ProjetMicroservices



- Projet Microservices

Ce projet consiste en la mise en place d'un système de microservices permettant à un utilisateur de s'authentifier, de jouer à un jeu de devinettes et de voir son score. Les microservices sont développés en utilisant Flask et sont conteneurisés avec Docker. La communication entre les microservices est réalisée via des requêtes HTTP.


- État du projet

Le projet comprend quatre microservices fonctionnels : auth_service, motus_service, score_service, et webapp_service. Chaque microservice est dockerisé et peut être exécuté individuellement. Ils ont été testés avec succès en utilisant Postman pour vérifier leurs fonctionnalités respectives.


- Architecture


L'architecture comprend les composants suivants :

auth_service : Gère l'authentification des utilisateurs.
motus_service : Fournit la logique pour le jeu de devinettes Motus.
score_service : Gère le stockage et la mise à jour des scores des joueurs.
webapp_service : Fournit une interface utilisateur web pour l'authentification et l'interaction avec les autres services.


Architecture Technique du Système de Microservices (voir diagramme d'architecture)


Chaque boîte représente un microservice avec ses fonctionnalités spécifiques.
Les flèches indiquent la direction de la communication entre les microservices.
Les détails techniques sont inclus dans les descriptions de chaque service, tels que les technologies utilisées (Flask), les fonctionnalités spécifiques (gestion de l'authentification, logique du jeu de devinettes, etc.), ainsi que les interactions avec les autres services.
Les endpoints spécifiques sont mentionnés pour chaque microservice, indiquant les points d'entrée pour les requêtes HTTP.




- Exécution du projet

Pour exécuter le projet, assurez-vous d'avoir Docker installé sur votre machine.

Clonez ce dépôt sur votre machine locale.
Ouvrez un terminal et accédez au répertoire racine du projet.
Exécutez la commande suivante pour démarrer les services :
bash
Copy code
docker-compose up
Attendez que tous les services soient démarrés.
Accédez à http://localhost:5004 dans votre navigateur pour accéder à l'application web.


- Test avec Postman

Chaque microservice peut être testé individuellement en utilisant Postman :

auth_service : Envoyez une requête POST à http://localhost:5002/auth/login avec un corps JSON contenant un nom d'utilisateur et un mot de passe pour vérifier l'authentification.
motus_service : Envoyez une requête POST à http://localhost:5003/motus/guess avec un corps JSON contenant un mot à deviner pour tester le jeu de devinettes.
score_service : Envoyez une requête POST à http://localhost:5001/score/update avec un corps JSON contenant un nom de joueur et un score pour mettre à jour le score du joueur.
Problème rencontré

Après l'authentification, l'application web ne communique pas correctement avec les autres microservices. Malgré une authentification réussie, une erreur se produit lors de l'interaction avec les services de jeu et de score. Cela nécessite une analyse plus approfondie pour identifier et résoudre le problème.

- Prochaines étapes

Examiner les journaux des services pour identifier les erreurs spécifiques.
Vérifier les configurations réseau des microservices pour s'assurer qu'ils peuvent se communiquer correctement.
Ajouter des tests unitaires et d'intégration pour chaque microservice afin de garantir un fonctionnement correct.
Envisager l'ajout de fonctionnalités supplémentaires telles que la gestion des utilisateurs, la sauvegarde des scores précédents, etc.
