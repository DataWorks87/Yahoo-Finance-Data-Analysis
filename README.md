Project Title: Streaming Data with AWS Services

Goal : Set a data pipeline to consume real-time data, process, store and query it. 

AWS Services: Lambda, Kinesis, Glue, S3, Athena.

In order to consume data I have set a Lambda function which also transforms the data in JSON format. The function is set to pull high and low prices for 10 stocks at an interval of 5 minutes for May 11th, 2021 trading day. Next, a Kinesis Data Stream will collect the data and a Kinesis Delivery Stream will push the data into a S3 bucket. Finally, a AWS Glue was configured to point to the S3 bucket which wil allow me to interactively query the S3 files using AWS Athena. To help with data analysis, i have set up a Glue Crawler. Once all was configured I run a query to get the highest hourly stock price per company and downloaded the results. The results was imported in Jupyter Notebook to create visualizations. 

A screenshot of AWS Kinesis configuration is provided below:

![kinesis_config](/Users/oleseagalusca/Desktop/TU_Big Data/Project3 /Project03/assets/kinesis_config.png)

