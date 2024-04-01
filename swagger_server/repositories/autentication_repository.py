from swagger_server.resources.databases.mysql import Connection

class AutenticationRepository():

    def login(body):

        response = None


        try:
            connection = Connection()
            connection = connection.get_connection("PYTHON")
            cursor = connection.cursor()

            query = '''
                    SELECT 
                    
                    U.id,
                    U.usuario,
                    U.nombre,
                    U.email,
                    U.rol_id,
                    U.rol,
                    U.estado

                    FROM users AS U 
                    
                    WHERE 1 = 1
                    
            '''


            params = []


            if body.user_name is not None and body.user_name != "":
                pass

                       

        except Exception as ex:
            pass
