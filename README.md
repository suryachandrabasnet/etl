# etl

Extract:
Fetches data from the API endpoint using Python (e.g., requests ).
Parses the JSON response and extracts relevant fields.

Transform:
Cleans and normalizes the extracted data.

Load:
Connects to PostgreSQL using psycopg2 or SQLAlchemy.
Inserts or updates records in the appropriate tables.
