# SQL Introduction

This project demonstrates how to set up a MySQL server using Docker and Docker Compose, and how to execute a SQL script to list all databases.

## Steps to Run the Project

1. **Start the MySQL container**:
    ```sh
    sudo docker-compose up -d
    ```

2. **Copy the SQL script into the container**:
    ```sh
    sudo docker cp 0-list_databases.sql $(sudo docker-compose ps -q db):/0-list_databases.sql
    ```

3. **Execute the SQL script inside the container**:
    ```sh
    sudo docker exec -it $(sudo docker-compose ps -q db) bash -c "mysql -uroot -proot < /0-list_databases.sql"
    ```

## Output

The expected output of the SQL script is:
```plaintext
Database
information_schema
mysql
performance_schema
sys
