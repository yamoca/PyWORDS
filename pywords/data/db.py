import sqlite3
con = sqlite3.connect("minimal.db") # connection
cur = con.cursor() # cursor

def create_dl_db():
    dl_column_types = {
        'dl_id': 'INTEGER',
        'dl_stem1': 'TEXT',
        'dl_stem2': 'TEXT',
        'dl_stem3': 'TEXT',
        'dl_stem4': 'TEXT',
        'dl_pos': 'TEXT',
        'dl_type': 'INTEGER',
        'dl_variant': 'INTEGER',
        'dl_gender': 'TEXT',
        'dl_comparison': 'INTEGER',
        'dl_kind': 'TEXT',
        'dl_aux_case': 'TEXT',
        'dl_age': 'TEXT',
        'dl_area': 'TEXT',
        'dl_geography': 'TEXT',
        'dl_frequency': 'TEXT',
        'dl_source': 'TEXT',
        'dl_senses': 'TEXT'
    }

    create_table("words", dl_column_types, "DICTLINE.tsv")


def populate_table(table_name, column_names, filename):
    dictionary = open(filename, 'r')
    lines = dictionary.readlines()

    insert_query = f"INSERT INTO {table_name} VALUES (" + ', '.join(['?' for _ in column_names]) + ")"
    for line in lines[1:]:
        values = line.split() 
        print(insert_query, values)
        cur.execute(insert_query, values)

    con.commit()



def create_table(table_name, column_types_dictionary, filename):
    column_names = list(column_types_dictionary.keys())
    columns_str = ', '.join([f"{column} {column_types_dictionary.get(column)}" for column in column_names]) # construct a string which formats column names and types for sql query
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
    cur.execute(create_table_query)
    con.commit()
    populate_table(table_name, column_names, filename)


def create_infl_db():
    infl_column_types = {
        'infl_id': 'INTEGER',
        'infl_pos': 'TEXT',
        'infl_type': 'TEXT',
        'infl_variant': 'TEXT',
        'infl_tense': 'TEXT',
        'infl_plurality': 'TEXT',
        'infl_person': 'TEXT',
        'infl_voice': 'TEXT',
        'infl_mood': 'TEXT',
        'infl_stem_id': 'INTEGER',
        'infl_ending': 'TEXT',
        'infl_age': 'TEXT',
        'infl_frequency': 'TEXT'
    }

    create_table("inflections", infl_column_types, "INFLECTS.tsv")

