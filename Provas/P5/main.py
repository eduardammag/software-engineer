from funcoes import *

# a)

""" Definindo os padrões (todos comportamentais):

1 - COMMAND: encapsula uma solicitação como um objeto transformando um
 pedido em um objeto independente. 
2 - STRATEGY: define uma família de algoritmos intercambiáveis em tempo
 de execução através da construção dos seus objetos em classes separadas. 
3 - CHAIN OF RESPONSABILITY: permite que você crie uma cadeia de handlers. 
Cada handler escolhe passar pra frente ou processar o pedido.
4 - TEMPLATE METHOD: define o 'esqueleto' fixo de um algoritmo na
superclasse, mas deixa as subclasses sobrescreverem coisas mais 
específicas sem modificar o esqueleto.

Aprendi com o professor Max que devemos sempre usar o princípio da parcimônia
(escolher o modelo mais simples mas que resolve o problema). Por isso escolhi 
Strategy + Template Method, que é uma forma organizada de estruturar tarefas
que seguem uma sequência fixa, mas que precisam de algumas variações em 
partes específicas. 

O Template garante que todas as tarefas sigam o mesmo fluxo geral 
(tipo pipeline) enquanto o Strategy permite alterar o comportamento 
interno de etapas específicas sem modificar o resto do código. 
Essa separação entre estrutura e comportamento deixa o código limpo, flexível e
extensível, pois é só criar uma nova subclasse para uma tarefa ou uma nova 
estratégia de processamento, sem interferir nas implementações antigas. 
Isso reduz o risco de erros e evita retrabalho.

O Chain of Responsibility + Command é indicada para sistemas que precisam 
de um fluxo dinâmico e condicional de execução, tipo quando diferentes partes 
de um sistema devem decidir se processam ou passam a requisição adiante.   
Aqui teríamos uma maior complexidade estrutural por causa do encadeamento de 
vários handlers e o controle de comandos. """

# b)

# Criando as tarefas e a fonte dos dados
import_task = ImportTask("Importacao de Dados")
report_task = ReportTask("Geracao de Relatorio")
dados_exemplo = "dados_eduarda_mesquita.csv"

# Execução sem strategy
import_task.execute(dados_exemplo)
report_task.execute(dados_exemplo)

print("###############################################")

# Execução com a troca dinâmica
contexto = TaskStrategyContext()

contexto.set_strategy(UppercaseStrategy())
contexto.executar(import_task, dados_exemplo)

contexto.set_strategy(LowercaseStrategy())
contexto.executar(report_task, dados_exemplo)

