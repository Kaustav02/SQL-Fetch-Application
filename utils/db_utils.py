import sqlite3

def execute_sql_command(db_path, sql_command):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute(sql_command)
        rows = cursor.fetchall()
        
        # Fetch column names
        column_names = [description[0] for description in cursor.description]
        
        # Convert the result to a list of dictionaries
        result = [dict(zip(column_names, row)) for row in rows]
    except sqlite3.Error as e:
        result = {"error": str(e)}
    finally:
        conn.close()
    
    return result
