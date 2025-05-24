# Deployment Instructions for Scraping Demo Project

## Prerequisites
- Ensure you have Docker and Docker Compose installed on your machine.
- Make sure you have access to an SQL Server instance and the necessary credentials.

## Step 1: Clone the Repository
Clone the project repository to your local machine using the following command:
```
git clone <repository-url>
cd scraping-demo
```

## Step 2: Build the Docker Image
Navigate to the `deployment` directory and build the Docker image using the following command:
```
docker build -t scraping-demo .
```

## Step 3: Configure Environment Variables
Create a `.env` file in the `deployment` directory to store your environment variables. Include the following variables:
```
DB_HOST=<your_sql_server_host>
DB_PORT=<your_sql_server_port>
DB_USER=<your_sql_server_username>
DB_PASSWORD=<your_sql_server_password>
DB_NAME=<your_database_name>
```

## Step 4: Start the Application
Use Docker Compose to start the application and its dependencies:
```
docker-compose up
```

## Step 5: Access the Application
Once the containers are running, you can access the application logs to monitor the scraping process. Use the following command:
```
docker-compose logs -f
```

## Step 6: Stop the Application
To stop the application, use:
```
docker-compose down
```

## Step 7: Clean Up
If you want to remove the Docker images and containers, run:
```
docker system prune -a
```

## Additional Notes
- Ensure that the SQL Server is accessible from the Docker containers.
- Modify the `src/config/settings.py` file if you need to adjust any scraping parameters or database settings.

Follow these steps to successfully deploy and run the scraping demo project.