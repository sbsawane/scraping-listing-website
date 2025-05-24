class Scraper:
    def __init__(self, driver):
        self.driver = driver

    def scrape_property_listings(self, url):
        self.driver.get(url)
        listings = self.driver.find_elements_by_class_name('property-listing')
        properties = []

        for listing in listings:
            title = listing.find_element_by_class_name('title').text
            price = listing.find_element_by_class_name('price').text
            location = listing.find_element_by_class_name('location').text
            properties.append({
                'title': title,
                'price': price,
                'location': location
            })

        return properties

    def close(self):
        self.driver.quit()