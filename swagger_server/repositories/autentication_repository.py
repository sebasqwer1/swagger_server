from swagger_server.resources.databases.mysql import Connection
from swagger_server.models.response_get_users import ResponseGetUsers
from swagger_server.models.response_get_users_data import ResponseGetUsersData

class AutenticationRepository():

    @staticmethod
    def login(body):

        print("login")

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
                query += ' AND usuario = %s'
                params.append(body.user_name)

            if body.password is not None and body.password != "":
                query += ' AND clave = %s'
                params.append(body.password)

            # print(query)

            cursor.execute(query, params)
            
            result = cursor.fetchone()
            result = cursor .fetchall()
            print(result)

            if(result is None):
                return ResponseGetUsers(
                    code=0,
                    message="Usuario o contraseña incorrecta",
                    data=[]
                )
            
            lista =[(1, 'sebasqwer1', 'Sebastian Alvarado', 'sebasqwer1@gmail.com', 1, 'Administrador', 'AC'),
                    (1, 'sebasqwer1', 'Sebastian Alvarado', 'sebasqwer1@gmail.com', 1, 'Administrador', 'AC'),
                    (1, 'sebasqwer1', 'Sebastian Alvarado', 'sebasqwer1@gmail.com', 1, 'Administrador', 'AC'),
                    (1, 'sebasqwer1', 'Sebastian Alvarado', 'sebasqwer1@gmail.com', 1, 'Administrador', 'AC')]
            
            return ResponseGetUsers(
                code=1,
                message="Usuario logeado exitosamente",
                data=ResponseGetUsersData(
                    id= result[0],
                    user_name= result[1],
                    full_name= result[2],
                    email= result[3],
                    rol_id= result[4],
                    rol_name= result[5]
                )
            )

                    
        except Exception as ex:
            error = "Error: {} ".format(ex)
            print(error)
