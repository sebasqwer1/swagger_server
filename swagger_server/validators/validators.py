class Validator:

    def validar_login(body):

        if body.user_name == None:
            return False, "El usuarioes requerido"
        if body.password == None:
            return False, "La contraseña es requerida"
        
        return True, "Exito"