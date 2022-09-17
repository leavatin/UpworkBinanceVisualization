# UpworkBinanceVisualization

This python script lets you check for Binance Tokens returns. It classifies the tokens who are top and worst performing based on their returns. 

# Requirements
1. `Python 3.9.5` or latest.
2. Python IDE (Spyder, VSCode, etc)
3. Jupyter Lab or Notebook or any IDE that opens `.ipynb` files

# How to Install

1. Download and install python 3.9.5 for your OS (https://www.python.org/downloads)
2. Open CMD, use `cd (directory of choice, preferably desktop)` (eg. `cd C:\Users\Leavatin\Desktop\UPWORK`), then copy paste `git clone https://github.com/leavatin/UpworkBinanceVisualization.git` .
3. `pip install -r requirements.txt` to install the dependencies.

# How to start the server

1. Open `VIS Server.ipynb`
2. Run all cells.
3. If you encounter an output of `False` or `{'result': None, 'id': 1, 'unicorn_fied': ['binance.com', '0.12.2']}` after running `data`, run again from Cell 4 (`ubwa.create_stream(['kline_1m'], [i.lower() for i in symbols], output="UnicornFy")`) up to Cell 6 (`data`) till you get an output as shown as the image below.
4. Run the remaining cells and ensure that the stream is running by checking if it is consistently updating as shown on the image below.

# How to run the visualization
1. Open CMD, use `cd (directory of this repository)` (eg. `cd C:\Users\Leavatin\Desktop\Local Repo GIT\UpworkBinanceVisualization`)
2. Run `streamlit run LiveDataExecutable.py`.
3. CMD will prompt the Local URL and Network URL if connection is successful.
4. A window will open from your browser. 
5. You can choose on how many minutes will you query (1min, 15mins, and 30min).
6. Press update to see the changes.

# Notes

You may encounter an error on cell 9 on `VIS Server.ipynb` where the stream have stopped. 
Just repeat Steps 3 and 4 in `How to start the server` and `Rerun`

# Credits
`Algovibes for base code`
`extremedevalt and jamiebuilds for read me`

