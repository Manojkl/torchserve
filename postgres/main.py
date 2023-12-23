from fastapi import FastAPI
import psycopg2

app = FastAPI()

# Database configuration
DATABASE_URL = "dbname='my_database' user='welcome' host='postgres-service' password='welcome' port='5432'"


def create_table():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


create_table()


@app.get("/")
async def read_root():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return {"items": items}
