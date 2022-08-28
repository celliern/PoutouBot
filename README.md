# PoutouBot

Bot pour un serveur privé, avec 4 fonctionnalités :

## Bientôt le (!bientot_apero et !bientot_weekend)

Affiche le contenu des pages https://estcequecestbientotlapero.fr/ et https://estcequecestbientotleweekend.fr/ 

## What a Week (!whataweek)

Affiche le meme What A Week, avec le jour actuel affiché

## Wololo (!wololo)

Change la couleur du rôle #wololo (qui doit exister sur le serveur). La couleur du rôle change aussi toutes les 30 minutes.

## Mange ta main

Répond une variante de type "mange ta main" lorsque "j'ai faim" apparait dans un message.

## Config

La config se fait avec des variables d'environnements (ou avec un fichier .env): $TOKEN contient le token de l'app (voir https://discord.com/developers/applications) et $GUILD_UID contient l'ID du serveur où le bot est actif. Le bot n'est pas fait pour fonctionner sur de multiples serveurs en l'état.
