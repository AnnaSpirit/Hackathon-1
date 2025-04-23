# Hackathon-1

FR ⏯️: Pawn to King
« La progression du pion jusqu’au roi, comme ton projet qui prend de l’élan »


⚙️ Paramètres et étapes pour player_gamer pour jouer à notre jeu.

1️⃣ Obtenir le projet :
- Ouvre un terminal et clone le dépôt :

    | git clone https://…/your-repo.git
    | cd your-repo


2️⃣ Installer Python 3 :
    - Sur Windows, si besoin:

    | python.org (trouver l'installateur})

    - Sur macOS, si besoin :

    | brew install python

    - Sur Linux, si besoin :

    | sudo apt install python3 python3-pip


3️⃣ Ouvrir dans VS Code :
    - Dans VS Code : Fichier → Ouvrir un dossier…, puis sélectionne le dossier cloné.


4️⃣ Installer les extensions :
    - Python (par Microsoft) pour exécuter et déboguer le script.
    - SQLTools + SQLTools PostgreSQL/Redshift pour accéder à la base.


6️⃣ Configurer la connexion PostgreSQL :
    - Appuie sur Ctrl+Shift+P → SQLTools : Add new connection → choisis PostgreSQL.
    - Renseigne :

    | Host     : localhost
    | Port     : 5432
    | Database : pawn_to_king
    | Username : player_gamer
    | Password : SuperMotDePasseSecu

    - Clique sur Tester la connexion, puis sur Enregistrer.


7️⃣ Lancer le jeu :
    - Ouvre le terminal intégré (`Ctrl+``).
    - Exécute :

    | python pawn_cli.py

    - Le plateau s’affiche, puis la console affiche :
    | Your move (ex : e2 e4) ou 'quit' : ---------


8️⃣ Jouer :
    - Saisis tes coups au format colonne-rangée colonne-rangée, par ex. e2 e4.
    - Appuie sur Entrée pour déplacer ton pion.
    - Tape quit pour quitter la partie.

Amuse-toi bien et que le meilleur stratège gagne ! 🎉🥇

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Mini guide de mouvement d'échecs 🎯
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

🐾 Pawn (Pion)
Déplacer: 1 carré simple
Premier mouvement: vous pouvez pousser 2 carrés vers l'avant une fois
Capture: 1 carré vers l'avant en diagonale
Spécial: au fait (lorsqu'un pion opposé saute 2 carrés à côté de vous)

🏰 Rook (Tour)
Déplacer: n'importe quel nombre de carrés, directement le long des rangs ou des fichiers (lignes ou colonnes)
Ne peut pas sauter: le chemin doit être clair

🐎 Knight (Cavalier)
Déplacer: dans une forme «l»: 2 carrés dans une direction + 1 perpendiculaire
Unique: peut sauter sur toutes les pièces

⛪ Bishop (Fou)
Déplacer: n'importe quel nombre de carrés en diagonale
Ne peut pas sauter: le chemin doit être clair

👑 Queen (Reine)
Déplacement: combinaison de Rook + Bishop
N'importe quel nombre de carrés droits ou diagonaux
Le plus puissant: couvre des tonnes de terrain

🤴 King (Roi)
Déplacer: 1 carré dans n'importe quelle direction (droit ou diagonal)
Special: Castling
King se déplace 2 carrés vers une tour, et la tour saute sur le carré à côté du roi

********************************
🎉 C'est tout! Pratiquez ces bases, et vous verrez le voyage de votre pion vers le roi - ou la reine - un fois en un rien de temps. Allez écraser ce jeu!
********************************
