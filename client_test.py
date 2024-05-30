import unittest
from client import getDataPoint
from client import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for i in quotes:
       self.assertEqual(getDataPoint(i),(i['stock'],i['top_bid']['price'],i['top_ask']['price'],(i['top_bid']['price']+i['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for i in quotes:
       self.assertEqual(getDataPoint(i),(i['stock'],i['top_bid']['price'],i['top_ask']['price'],(i['top_bid']['price']+i['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """


  def test_getRatio_calculateRatio(self):
    price_a = 120.48
    price_b = 121.68
    ratio = price_a / price_b
    """ Add the assertion below """
    self.assertAlmostEqual(getRatio(price_a, price_b), ratio)

  def test_getRatio_divisionByZero(self):
    price_a = 120.48
    price_b = 0
    """ Add the assertion below """
    self.assertIsNone(getRatio(price_a, price_b))




if __name__ == '__main__':
    unittest.main()
