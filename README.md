# Scraping Demo Project

This project is a web scraping application built using Python and Selenium. It scrapes property listings from a specified website and saves the data to an SQL server.

## Project Structure

```
scraping-demo
├── src
│   ├── main.py
│   ├── scraper
│   │   ├── __init__.py
│   │   ├── scraper.py
│   │   └── utils.py
│   ├── database
│   │   ├── __init__.py
│   │   └── db_handler.py
│   └── config
│       └── settings.py
├── tests
│   ├── test_scraper.py
│   └── test_db_handler.py
├── requirements.txt
├── README.md
└── deployment
    ├── Dockerfile
    ├── docker-compose.yml
    └── deployment_instructions.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd scraping-demo
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure settings:**
   Update the `src/config/settings.py` file with your database connection details and any scraping parameters.

## Usage

To run the scraper, execute the following command:
```
python src/main.py
```

This will start the scraping process and save the property listings to the configured SQL server.

## Testing

To run the tests, use:
```
pytest tests/
```

This will execute the unit tests for both the scraper and the database handler.

## Deployment

For deployment, you can use Docker. Follow the instructions in `deployment/deployment_instructions.md` to build and run the Docker containers.

## License

This project is licensed under the MIT License. See the LICENSE file for details.