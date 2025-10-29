from dispositivos.dispositivo_a import DispositivoA
from dispositivos.dispositivo_b import DispositivoB
from adaptadores.adaptador_generico import AdaptadorGenerico

# Criando instâncias dos dispositivos
dispositivo_a = DispositivoA()
dispositivo_b = DispositivoB()

# Adaptando DispositivoA para ter o método 'executar', que é esperado pelo cliente
adaptador = AdaptadorGenerico(dispositivo_a, "metodo_especifico", "executar")

# Agora podemos chamar 'executar' no adaptador
resultado = adaptador.executar()

# Passando o resultado para o dispositivo B
print(dispositivo_b.executar(resultado))
