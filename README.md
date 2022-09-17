# UpworkBinanceVisualization

This python script lets you check for Binance Tokens returns. It classifies the tokens who are top and worst performing based on their returns. 

# Requirements
1. `Python 3.9.5` or latest.
2. Python IDE (Spyder, VSCode, etc)
3. Jupyter Lab or Notebook or any IDE that opens `.ipynb` files

# How to Install

1. Download and install python 3.9.5 for your OS (https://www.python.org/downloads)
2. Open CMD, use `cd (directory of choice, preferably desktop)` (eg. `cd C:\Users\Leavatin\Desktop\UPWORK`), then copy paste `git clone https://github.com/leavatin/UpworkBinanceVisualization.git`. ` `
`CD with CMD`
![cd](https://user-images.githubusercontent.com/60631793/190859188-122955ce-09f9-4dbb-85ae-f13ee55d65a8.jpg)
`Git Clone`
![clone](https://user-images.githubusercontent.com/60631793/190859189-178a5dea-a592-4b39-b252-a499fde0f1af.jpg)
3. `pip install -r requirements.txt` to install the dependencies.
![pip install](https://user-images.githubusercontent.com/60631793/190859197-2cfc980d-adcd-4cd7-9080-729f710e96f9.jpg)

# How to start the server

1. Open `VIS Server.ipynb`
2. Run all cells.
3. If you encounter an output of `False` or `{'result': None, 'id': 1, 'unicorn_fied': ['binance.com', '0.12.2']}` after running `data`, run again from Cell 4 (`ubwa.create_stream(['kline_1m'], [i.lower() for i in symbols], output="UnicornFy")`) up to Cell 6 (`data`) till you get an output as shown as the image below.
`Output with false`
![1st error](https://user-images.githubusercontent.com/60631793/190859185-2fef18c8-168d-4787-86f8-6a53bdf38de7.jpg)
`Output with Null values
![error 2](https://user-images.githubusercontent.com/60631793/190859195-45fdb866-b92b-4558-ae40-42da78e77189.jpg)
4. Run the remaining cells and ensure that the stream is running by checking if it is consistently updating as shown on the image below.
![desired output 2](https://user-images.githubusercontent.com/60631793/190859193-b8e99698-9257-4f9d-ae24-2d519f130e04.jpg)

# How to run the visualization
1. Open CMD, use `cd (directory of this repository)` (eg. `cd C:\Users\Leavatin\Desktop\Local Repo GIT\UpworkBinanceVisualization`)` `
`CD with CMD`
![cd](https://user-images.githubusercontent.com/60631793/190859188-122955ce-09f9-4dbb-85ae-f13ee55d65a8.jpg)
2. Run `streamlit run LiveDataExecutable.py`. ` `
`Streamlit Command Line`
![streamlit ini](https://user-images.githubusercontent.com/60631793/190859201-fc0b76c8-7f04-459c-9fdb-c11475428c68.jpg)
4. CMD will prompt the Local URL and Network URL if connection is successful.
`Streamlit Success Prompt`
![streamlit success](https://user-images.githubusercontent.com/60631793/190859202-5a62f8b3-14a6-45e8-878e-0e9107d763dc.jpg)
6. A window will open from your browser. 
`Sample Window`
![Sample](https://user-images.githubusercontent.com/60631793/190859200-03de6d5f-0b0b-47b4-9455-019ec3b2d46d.jpg)
8. You can choose on how many minutes will you query (1min, 15mins, and 30min).
`Timeframe`
![timeframe](https://user-images.githubusercontent.com/60631793/190859179-2a9a2ff1-5dcc-4028-bd97-7dfcc3df914e.jpg)
10. Press update to see the changes.


# Notes

You may encounter an error on cell 9 on `VIS Server.ipynb` where the stream have stopped. 
Just repeat Steps 3 and 4 in `How to start the server` and `Rerun` ` `
`Rerun button`
![rerun](https://user-images.githubusercontent.com/60631793/190859198-68c4514c-a07b-4abd-8032-2525a6187b29.jpg)


# Credits
`Algovibes for base code`
`extremedevalt and jamiebuilds for read me`

