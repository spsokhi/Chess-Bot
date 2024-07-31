# Chess Bot Project

This project contains two main components: a command-line chess bot and a GUI-based chess bot.

## Project Structure
```
├── chessbot
│   ├── chess_bot.py
│   └── readme.md
├── chessbot_gui
│   ├── ChessEngine.py
│   ├── images
│   │   ├── bB.png
│   │   ├── bK.png
│   │   ├── bN.png
│   │   ├── bP.png
│   │   ├── bQ.png
│   │   ├── bR.png
│   │   ├── wB.png
│   │   ├── wK.png
│   │   ├── wN.png
│   │   ├── wP.png
│   │   ├── wQ.png
│   │   └── wR.png
│   ├── main.py
│   ├── readme.md
│   └── requirements.txt
```
## How to Run
### Command-Line Chess Bot
1. **Navigate to the chessbot directory:**
   ```cd chessbot```
2. **Create and activate a virtual environment:**
   ```
   python3 -m venv chess_bot_env
   source chess_bot_env/bin/activate

3. **Install the required dependencies:**
   ```
   pip install python-chess
4. **Run the chess bot:**
   ```
   python chess_bot.py

   
### GUI-Based Chess Bot
1. **Navigate to the chessbot_gui directory:**
   ```
   cd chessbot_gui

2. **Create and activate a virtual environment:**
   ```
   python3 -m venv chess_bot_env
   source chess_bot_env/bin/activate
   
3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt

4. **Download Stockfish:**
   - Visit the Stockfish website and download the appropriate version for your operating system. [Stockfish website](https://stockfishchess.org/download/)
   - Extract the downloaded file to a directory of your choice (e.g., stockfish).
   
5. **Update the engine_path in main.py to point to your Stockfish executable:**
     ```
     engine_path = "/path/to/your/stockfish/executable"

6. **Run the GUI-based chess bot:**
   
   python main.py

   
Notes
Make sure to download and place the Stockfish engine executable in an accessible location if you plan to use it with the GUI-based chess bot.
Update the path to the Stockfish executable in the code as needed.


This setup will ensure that the `stockfish` directory and `stockfish-macos-x86-64.tar` file are not uploaded to GitHub, and provides clear instructions on how to run both parts of the project.

