import unittest
from src.scraper.scraper import Scraper

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = Scraper()

    def test_scrape_property_listings(self):
        listings = self.scraper.scrape_property_listings()
        self.assertIsInstance(listings, list)
        self.assertGreater(len(listings), 0)
        for listing in listings:
            self.assertIn('title', listing)
            self.assertIn('price', listing)
            self.assertIn('location', listing)

if __name__ == '__main__':
    unittest.main()