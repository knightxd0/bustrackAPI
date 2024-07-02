import psycopg2
from Engine.settings import CONNECTION

#users
# def create_table_users():
#     conn = psycopg2.connect(CONNECTION)
#     cursor = conn.cursor()
#     query = """
#           CREATE TABLE IF NOT EXISTS users (
#             id SERIAL PRIMARY KEY,
#             cover_img VARCHAR(255),
#             email VARCHAR(255),
#             name  VARCHAR(255),
#             organize_name VARCHAR(255)
#         );
#     """
#     cursor.execute(query)
#     conn.commit()
#     cursor.close()
#     conn.close()
#
#
#
#
# #category
# def create_table_category():
#     conn = psycopg2.connect(CONNECTION)
#     cursor = conn.cursor()
#     query = """
#               CREATE TABLE IF NOT EXISTS category(
#                 id  SERIAL PRIMARY KEY,
#                 name VARCHAR(255),
#                 color VARCHAR(255)
#             );
#         """
#     cursor.execute(query)
#     conn.commit()
#     cursor.close()
#     conn.close()
#
# def insert_default_category():
#     conn = psycopg2.connect(CONNECTION)
#     cursor = conn.cursor()
#     query = """
#               INSERT INTO public.category(id, name, color)
# 	          VALUES (1,'ไม่มีหมวดหมู่', 'BlueFolder.png');
#         """
#     cursor.execute(query)
#     conn.commit()
#     cursor.close()
#     conn.close()
#
# #project
# def create_table_project():
#     conn = psycopg2.connect(CONNECTION)
#     cursor = conn.cursor()
#     query = """
#               CREATE TABLE IF NOT EXISTS project(
#                 id  SERIAL PRIMARY KEY,
#                 name VARCHAR(255) UNIQUE,
#                 description VARCHAR(255),
#                 cover_img VARCHAR(255),
#                 project_type VARCHAR(255),
#                 host_id INTEGER REFERENCES users(id),
#                 member JSONB,
#                 "create_at" timestamp with time zone NOT NULL DEFAULT now(),
#                 vendor_name VARCHAR(255),
#                 category_id INTEGER[]
#             );
#         """
#     cursor.execute(query)
#     conn.commit()
#     cursor.close()
#     conn.close()
#
# #file
# def create_table_file():
#     conn = psycopg2.connect(CONNECTION)
#     cursor = conn.cursor()
#     query = """
#           CREATE TABLE IF NOT EXISTS file(
#             id  VARCHAR(255),
#             name VARCHAR(255),
#             type VARCHAR(255),
#             project_id INTEGER REFERENCES project(id),
#             "upload_at" timestamp with time zone NOT NULL DEFAULT now()
#         );
#     """
#     cursor.execute(query)
#     conn.commit()
#     cursor.close()
#     conn.close()
#
# #recycle_bin
# def create_table_recycle_bin():
#     conn = psycopg2.connect(CONNECTION)
#     cursor = conn.cursor()
#     query = """
#           CREATE TABLE IF NOT EXISTS recycle_bin(
#             id  VARCHAR(255) PRIMARY KEY,
#             name VARCHAR(255),
#             type VARCHAR(255),
#             project_id INTEGER REFERENCES project(id),
#             "upload_at" timestamp with time zone NOT NULL DEFAULT now(),
#             "delete_at" timestamp with time zone NOT NULL DEFAULT now()
#         );
#     """
#     cursor.execute(query)
#     conn.commit()
#     cursor.close()
#     conn.close()
#
# #notification
def create_table_data():
    conn = psycopg2.connect(CONNECTION)
    cursor = conn.cursor()
    query = """
          CREATE TABLE IF NOT EXISTS data(
            id  SERIAL PRIMARY KEY,
            name VARCHAR(255),
            lat REAL,
            long REAL,
            speed REAL,
            "time_at" timestamp with time zone NOT NULL DEFAULT now()
        );
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()




if __name__ == '__main__':
    # create_table_users()
    # create_table_category()
    # insert_default_category()
    # create_table_project()
    # create_table_notification()
    # create_table_file()
    # create_table_recycle_bin()
    create_table_data()

