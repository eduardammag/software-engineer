from dispositivos.tomada_americana import TomadaAmericana
from dispositivos.dispositivo_europeu import DispositivoEuropeu
from adaptadores.adaptador_tomada import AdaptadorTomada


# Criando instâncias dos objetos originais
tomada = TomadaAmericana()
dispositivo = DispositivoEuropeu()

# Criando o Adaptador para "traduzir" a interface
adaptador = AdaptadorTomada(tomada)

# Obtendo a tensão adaptada
tensao = adaptador.obter_220v()

# Ligando o dispositivo europeu com a tensão adaptada
resultado = dispositivo.ligar_dispositivo(tensao)
print(resultado)

# Outros testes

print("=== Cenário 1: Dispositivo europeu ligado direto na tomada americana ===")
tomada = TomadaAmericana()
dispositivo = DispositivoEuropeu()
    
tensao = tomada.ligar()  # Sem adaptador
resultado = dispositivo.ligar_dispositivo(tensao)
print("Resultado:", resultado)  

print("\n=== Cenário 2: Dispositivo europeu usando adaptador ===")
adaptador = AdaptadorTomada(tomada)
tensao_adaptada = adaptador.obter_220v()  
resultado_adaptado = dispositivo.ligar_dispositivo(tensao_adaptada)
print("Resultado:", resultado_adaptado)  

print("\n=== Cenário 3: Testando múltiplos dispositivos ===")
tomadas = [TomadaAmericana(), TomadaAmericana()]
dispositivos = [DispositivoEuropeu(), DispositivoEuropeu()]

for i, (t, d) in enumerate(zip(tomadas, dispositivos), start=1):
    adaptador_multi = AdaptadorTomada(t)
    tensao_multi = adaptador_multi.obter_220v()
    resultado_multi = d.ligar_dispositivo(tensao_multi)
    print(f"Dispositivo {i}: {resultado_multi}")
