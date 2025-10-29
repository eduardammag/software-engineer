class AdaptadorTomada:
    """
    Adaptador que converte a interface de um dispositivo
    (por exemplo, de TomadaAmericana para o que o DispositivoEuropeu espera).
    """

    def __init__(self, tomada_americana):
        """
        Recebe a instância do objeto que precisa ser adaptado.
        :param tomada_americana: Objeto com interface incompatível
        """
        self.tomada_americana = tomada_americana

    def obter_220v(self):
        """
        Método que adapta a interaface original para a interface esperada.
        Aqui simulamos a conversão de 110V para 220V.
        """  
        tensao = self.tomada_americana.ligar() # Chama o método original
        if tensao == "110V":
            print("Adaptador: Convertendo 110V para 220V...")
            return "220V"  
        return tensao
