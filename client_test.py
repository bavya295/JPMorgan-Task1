import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      
      {
  "top_ask": {
    "price": 150.75,
    "size": 50
  },
  "timestamp": "2019-03-11 14:22:30.572453",
  "top_bid": {
    "price": 149.85,
    "size": 120
  },
  "id": "0.209874563211",
  "stock": "XYZ"
},
{
  "top_ask": {
    "price": 95.5,
    "size": 20
  },
  "timestamp": "2019-04-15 11:45:00.345678",
  "top_bid": {
    "price": 94.75,
    "size": 150
  },
  "id": "0.305678912345",
  "stock": "DEF"
}
,
{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {
  "top_ask": {
    "price": 201.4,
    "size": 70
  },
  "timestamp": "2019-05-22 12:10:45.987654",
  "top_bid": {
    "price": 200.9,
    "size": 150
  },
  "id": "0.310234567890",
  "stock": "GHI"
}
,{
  "top_ask": {
    "price": 65.4,
    "size": 120
  },
  "timestamp": "2019-07-27 09:05:10.654321",
  "top_bid": {
    "price": 64.8,
    "size": 140
  },
  "id": "0.510345678912",
  "stock": "MNO"
}
,
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
