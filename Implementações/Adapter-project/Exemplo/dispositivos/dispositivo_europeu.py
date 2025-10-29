class DispositivoEuropeu:
    """
    Classe que espera energia em 220V.
    """
    def ligar_dispositivo(self, tensao):
        """
        Liga o dispositivo apenas se a tensão for 220V.
        :param tensao: string representando a tensão.
        """
        if tensao == "220V":
            return "Dispositivo europeu está funcionando!"
        else:
            return "Tensão inadequada!"