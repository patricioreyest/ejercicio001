

class Guitarra:
    def __init__(self, tipo, estilo):
        self.tipo = tipo
        self.estilo = estilo
        
    def audio(self):
        return (f"la guitarra es {self.tipo} sirve para tocar musica del estilo {self.estilo}")
    

acustica = Guitarra("acustica", "blue")
bajo = Guitarra("bajo", "cumbia")


print(acustica.audio())
print(bajo.audio())