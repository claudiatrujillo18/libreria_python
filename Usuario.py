class Usuario:
    def __init__(self, id, nombre, apellido, correo, contrasena):
        # Se definen las instancias de la clase
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contrasena = contrasena

    # Getters y setters

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, nueva_contrasena):
        self._contrasena = nueva_contrasena

    # Método propio que se llama registrar_usuario

    def registrar_usuario(self):
        self.id = input("Ingrese el id del usuario:")
        self.nombre = input("Ingrese el nombre del usuario:")
        self.apellido = input("Ingrese el apellido del usuario:")
        self.correo = input("Ingrese el correo del usuario:")
        self.contrasena = input("Ingrese la contrasena del usuario:")

    def ver_usuario(self):
        print(f"Id:{self._id} Nombre:{self._nombre} Apellido:{self._apellido} Correo:{self._correo} Contraseña:{self._contrasena}")

