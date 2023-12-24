import psycopg2

SERVER_FILE_PATH = "/Users/mark/Downloads/downloaded.png"
DATABASE_URL = "postgresql://user:password@localhost:5432/database"
TABLE_NAME = "table_name"
BYTEA_COLUMN_NAME = "bytea_column_name"
LO_COLUMN_NAME = "lo_column_name"


with open(SERVER_FILE_PATH, 'rb') as file:
    file_data = file.read()

with psycopg2.connect(DATABASE_URL) as conn:
    with conn.cursor() as cursor:
        # using bytea column
        cursor.execute(
            f"insert into {TABLE_NAME} ({BYTEA_COLUMN_NAME}) values (%s)",
            (psycopg2.Binary(file_data),)
        )
        # using LOs. the file must be located on the server side.
        cursor.execute(
            f"insert into {TABLE_NAME} ({LO_COLUMN_NAME}) values (lo_import(%s))",
            (SERVER_FILE_PATH,)
        )
    conn.commit()
