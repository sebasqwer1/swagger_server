from swagger_server.repositories.autentication_repository import AutenticationRepository


class AutenticationUseCase():

    @staticmethod
    def login(body):

        repository = AutenticationRepository()
        response = repository.login(body)

        if response.code == 1:

            result = response.data.email

            if result == "sebasqwer1@gmail.com":
                data = response.data
                data.rol_name = data.rol_name.upper()
            
        return response
