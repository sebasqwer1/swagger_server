from swagger_server.config.access import access
import mysql.connector


class Connection():  


    @staticmethod
    def get_connection(db):

        db_config = Connection.get_credentials(db)

        try:

            connection = mysql.connector.connect(**db_config)

            if connection.is_connected():
                print(f"Conexión a la base de datos {db_config['database']} establecida.")
            
            return connection
        
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

        finally:
            # Cierra la conexión al finalizar
            if 'connection' in locals() and connection.is_connected():
                # connection.close()
                print("Conexión cerrada.")

    @staticmethod
    def get_credentials(db):

        response_json = access()
        mode =  response_json["MODE"]
        credentials_db = response_json.get(mode).get("DB").get("MYSQL").get(db)
        response = {
            "host": credentials_db.get("HOST"),
            "port": credentials_db.get("PORT"),
            "database": credentials_db.get("DB"),
            "user": credentials_db.get("USER"),
            "password": credentials_db.get("PASSWORD")
        }
        return response
