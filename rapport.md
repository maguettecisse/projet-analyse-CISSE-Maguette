# Rapport d'analyse des journaux d'un pare-feu

## 1. Résumé de l'analyse

Ce projet consiste à analyser les journaux d'un pare-feu à l'aide de Python afin d'identifier les activités inhabituelles sur un réseau informatique. L'analyse a été réalisée avec les bibliothèques Pandas et Matplotlib. Après le nettoyage des données, 5 440 lignes ont été conservées. Les résultats montrent que le port 443 est le plus utilisé et que 13,57 % des connexions ont été refusées. Deux comportements nécessitant une investigation ont également été identifiés : une activité de scan de ports et un volume important de données envoyées par une adresse IP.

## 2. Comportements suspects identifiés

### 2.1. Activité de scan de ports

L'adresse IP `192.168.1.99` a contacté 328 ports de destination différents. Cette activité peut correspondre à une tentative de reconnaissance du réseau ou à un scan de ports. Un tel comportement peut être utilisé pour identifier les services accessibles sur une machine avant une éventuelle attaque.

### 2.2. Volume important de données envoyées

L'adresse IP `192.168.1.11` présente un volume total de données envoyées de 259 932 541 octets, soit environ 260 Mo. Ce volume peut correspondre à un transfert de données inhabituel. Il est donc nécessaire de vérifier l'origine, la destination et la nature de ces échanges afin de rechercher une éventuelle exfiltration de données.

Ces deux comportements sont considérés comme suspects et nécessitent des vérifications complémentaires avant de conclure à une activité malveillante.

## 3. Recommandations de sécurité

À la suite de cette analyse, les recommandations suivantes sont proposées :

1. **Renforcer les règles du pare-feu :** limiter les connexions vers les ports non nécessaires et surveiller les tentatives répétées de connexion.
2. **Segmenter le réseau IoT :** isoler les objets connectés dans un réseau distinct afin de limiter les risques de propagation d'une attaque.
3. **Désactiver les services non sécurisés :** fermer les ports et services inutilisés, notamment Telnet (port 23), et privilégier des protocoles sécurisés.
4. **Surveiller les volumes de données :** mettre en place des alertes lorsqu'une adresse IP envoie un volume inhabituel de données.

## 4. Conclusion

Cette analyse a permis de nettoyer les journaux du pare-feu, d'extraire des indicateurs importants et de produire des graphiques facilitant la compréhension du trafic réseau. Elle a également permis de repérer deux comportements nécessitant une investigation. L'utilisation de Python constitue ainsi une aide intéressante pour la supervision et l'amélioration de la sécurité d'un réseau informatique.