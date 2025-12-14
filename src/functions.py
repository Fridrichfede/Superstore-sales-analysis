from config  import db_connection_str
from sqlalchemy import text, create_engine

#USE THIS FUNCTION TO CONNECT DATABASE
def get_engine():
     return create_engine(db_connection_str)

# USE THIS FUNCTION IF QUERY IS (INSERT/DELETE/UPDATE) STATEMENT
def execute_queries(query):
     with get_engine().connect() as conn:
          try:
            conn.execute(text(query))
            conn.commit()
          except Exception as e:
            print(f'Something went wrong: {e}')
     
        