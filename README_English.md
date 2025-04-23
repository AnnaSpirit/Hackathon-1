# Hackathon-1
EN ⏯️:    Pawn to King 
"The progress of the pawn to the king, as your project which is gaining momentum"


⚙️ Settings & Steps for player_gamer to play our game.

1️⃣ Get the project: 
    - Open a terminal and clone the repo:

    | git clone https://…/your-repo.git
    | cd your-repo


2️⃣ Install Python 3 :
    - On Windows, if needed:

    | python.org ( find the installer)
    
    - On macOS, if needed:

    | brew install python

     - On Linux, if needed:
    | sudo apt install python3 python3-pip


3️⃣ Open in VS Code: 
    - In VS Code: File → Open Folder…, select the cloned project directory.


4️⃣ Install extensions: 
    - Python (by Microsoft) for running/debugging the script.
    - SQLTools + SQLTools PostgreSQL/Redshift for database access.


6️⃣ Configure the PostgreSQL connection: 
    - Hit Ctrl+Shift+P → SQLTools: Add new connection → choose PostgreSQL.
    - Fill in: 

    | Host     : localhost
    | Port     : 5432
    | Database : pawn_to_king
    | Username : player_gamer
    | Password : SuperMotDePasseSecu

    - Click Test Connection, then Save.


7️⃣ Start the game: 
    - Open the integrated terminal
    - Run: 

    | python pawn_cli.py

The board will display, then prompt:
    | Your move (ex : e2 e4) ou 'quit' :   --------


8️⃣ Play
     - Enter moves in file-rank file-rank format, e.g. e2 e4.
     - Press Enter to move your pawn.
     - Type quit to exit.

Have fun and may the best strategist win! 🎉🥇


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Mini Chess Movement Guide 🎯
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

🐾 Pawn
Move: 1 square straight forward
First move: you can push 2 squares forward once
Capture: 1 square diagonally forward
Special: en passant (when an opposing pawn jumps 2 squares beside you)

🏰 Rook
Move: any number of squares, straight along ranks or files (rows or columns)
Can’t jump: path must be clear

🐎 Knight
Move: in an “L” shape: 2 squares in one direction + 1 perpendicular
Unique: can hop over any pieces

⛪ Bishop
Move: any number of squares diagonally
Can’t jump: path must be clear

👑 Queen
Move: combination of rook + bishop
any number of squares straight or diagonal
Most powerful: covers tons of ground

🤴 King
Move: 1 square in any direction (straight or diagonal)
Special: castling
King moves 2 squares toward a rook, and the rook jumps to the square beside the king

*******************************
🎉 That’s it! Practice these basics, and you’ll see your pawn’s journey to king—or queen—unfold in no time. Go crush that game!
*******************************
