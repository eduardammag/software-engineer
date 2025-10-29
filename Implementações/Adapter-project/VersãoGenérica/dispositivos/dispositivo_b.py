class DispositivoB:
    """Dispositivo que espera um método padrão 'executar'."""

    def executar(self, resultado):
        """
        Método esperado pelo cliente.
        :param resultado: valor adaptado do DispositivoA
        """
        return f"Dispositivo B recebeu: {resultado}"
