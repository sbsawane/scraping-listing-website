from scraper.scraper import Scraper
from database.db_handler import DBHandler
from config.settings import DATABASE_CONFIG

def main():
    # Initialize the database handler
    db_handler = DBHandler(DATABASE_CONFIG)
    db_handler.connect()

    # Initialize the scraper
    scraper = Scraper()

    # Scrape property listings
    property_listings = scraper.scrape_property_listings()

    # Save the scraped data to the database
    db_handler.save_data(property_listings)

    # Close the database connection
    db_handler.close_connection()

if __name__ == "__main__":
    main()