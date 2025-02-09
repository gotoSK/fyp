from modules.database_operations import create_table_from_model


def process_data(db_uri):
    # Example: Create a new table based on some processing logic
    new_table_name = "processed_data"
    columns = "id SERIAL PRIMARY KEY, data_column VARCHAR"
    create_table_from_model(db_uri, new_table_name, columns)
