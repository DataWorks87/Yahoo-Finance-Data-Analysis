import json
import boto3

import yfinance as yf

stocks = ['FB','SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']

def lambda_handler(event, context):
 
  kinesis = boto3.client("kinesis", "us-east-2")

  for stock in stocks:
      data = yf.download(stock, start='2021-05-11', end='2021-05-12', interval = "5m")
     
      for datetime, value in data.iterrows():
          record = {'high': value['High'], 'low': value['Low'],'ts': str(datetime), 'name': stock}
          data = json.dumps(record)+"\n"
          kinesis.put_record(StreamName="sta9760-stream1",Data = data, PartitionKey = "partitionkey")
          
  return {
      'statusCode': 200,
      'body': json.dumps(f'Done!')
  }