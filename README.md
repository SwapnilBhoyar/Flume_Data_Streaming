# Store real time stock data to hdfs using flume
1) Get the api key from https://www.alphavantage.co/
2)  Go through the documentation provided by the side.
3)  Write python program using the keyword provided in documentation
4)  Configure the file and provide python file as source
5)  Run the command : bin/flume-ng agent –conf ./conf/ -f conf/stock.conf -n agent1 -Dflume.root.logger=DEBUG
6)  Check the output in hdfs directory
