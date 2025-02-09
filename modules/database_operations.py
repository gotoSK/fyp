import pandas as pd
import psycopg2
from psycopg2.extras import execute_values


def load_csv_to_db(csv_path, db_uri):
    df = pd.read_csv(csv_path)
    conn = psycopg2.connect(db_uri)
    cur = conn.cursor()
    # Assuming the table is named 'temp_table'
    execute_values(cur, "INSERT INTO temp_table VALUES %s", df.values)
    conn.commit()
    cur.close()
    conn.close()


def create_table_from_model(db_uri, table_name, columns):
    conn = psycopg2.connect(db_uri)
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE {table_name} ({columns});")
    conn.commit()
    cur.close()
    conn.close()
