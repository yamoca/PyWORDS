import sqlite3
con = sqlite3.connect("minimal.db") # connection
cur = con.cursor() # cursor

def create_dictionary_db():
    column_types = {
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


    dictionary = open("DICTLINE.TSV", 'r')
    lines = dictionary.readlines()


    column_names = list(column_types.keys())
    columns_str = ', '.join([f"{column} {column_types.get(column)}" for column in column_names])
    create_table_query = f"CREATE TABLE IF NOT EXISTS words ({columns_str})"
    cur.execute(create_table_query)

    # must construct this as dont want to write out 17 lots of (?, ?, ?, ) by hand
    insert_query = "INSERT INTO words VALUES (" + ', '.join(['?' for _ in column_names]) + ")"
    for line in lines[1:]:
        values = line.split() 
        print(insert_query, values)
        cur.execute(insert_query, values)

    con.commit()