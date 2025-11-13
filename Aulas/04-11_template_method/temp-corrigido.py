"""
Padrão de Projeto: TEMPLATE METHOD
====================================================================
 Ideia principal:
------------------
O Template Method define **um algoritmo base (modelo)** que descreve
a sequência dos passos que todas as subclasses devem seguir.

Cada subclasse (estratégia concreta) implementa **alguns passos específicos**,
mas o "roteiro" (ordem dos passos) é o mesmo para todos.

É como uma receita de bolo: a ordem dos passos é fixa,
mas cada tipo de bolo muda alguns ingredientes ou etapas.

====================================================================
# EXEMPLO: Sistema de Pipelines de Dados
Cada pipeline tem a mesma estrutura (carregar → limpar → analisar → reportar),
mas os detalhes de cada etapa variam conforme o tipo de pipeline.
====================================================================
"""

from abc import ABC, abstractmethod  # Para criar classes e métodos abstratos

# ====================================================================
# CLASSE BASE ABSTRATA: define o esqueleto do algoritmo (Template)
# ====================================================================
class PipelineDeDados(ABC):
    """
    Classe abstrata que define o modelo (template) do pipeline de dados.

    Ela garante que TODAS as subclasses sigam o mesmo roteiro:
    1. Carregar dados
    2. (gancho opcional) Ações após carregar
    3. Limpar dados
    4. (gancho opcional) Ações após limpar
    5. Analisar dados
    6. Gerar relatório
    """

    def executar_pipeline(self, fonte: str) -> None:
        """
        Este é o TEMPLATE METHOD — ele define a sequência fixa
        dos passos que qualquer pipeline concreto deve seguir.

        OBS: As subclasses NÃO devem alterar esse método.
        """
        # 1️ Carrega os dados
        self.carregar_dados(fonte)
        # Hook opcional: executa algo após o carregamento
        self.hook_apos_carregar()

        # 2️ Limpa os dados
        self.limpar_dados()
        # Hook opcional: executa algo após a limpeza
        self.hook_apos_limpar()

        # 3️ Analisa os dados
        self.analisar_dados()

        # 4️ Gera o relatório final
        self.gerar_relatorio()

    # ----------------------------------------------------------------
    # Métodos obrigatórios: DEVEM ser implementados por cada subclasse
    # ----------------------------------------------------------------
    @abstractmethod
    def carregar_dados(self, fonte: str) -> None:
        """Carrega os dados a partir da fonte especificada."""
        pass

    @abstractmethod
    def limpar_dados(self) -> None:
        """Realiza o processo de limpeza/preparação dos dados."""
        pass

    @abstractmethod
    def analisar_dados(self) -> None:
        """Executa a análise principal sobre os dados."""
        pass

    @abstractmethod
    def gerar_relatorio(self) -> None:
        """Gera o resultado ou saída final da análise."""
        pass

    # ----------------------------------------------------------------
    # Métodos opcionais (hooks): podem ou não ser sobrescritos
    # ----------------------------------------------------------------
    def hook_apos_carregar(self) -> None:
        """
        Gancho (hook) chamado logo após o carregamento dos dados.
        Subclasses podem sobrescrever para adicionar comportamento extra.
        """
        pass

    def hook_apos_limpar(self) -> None:
        """
        Gancho (hook) chamado logo após a limpeza dos dados.
        Subclasses podem sobrescrever se desejarem.
        """
        pass


# ====================================================================
# SUBCLASSE CONCRETA 1: Pipeline de Análise de Vendas
# ====================================================================
class PipelineAnaliseVendas(PipelineDeDados):
    """Pipeline específico para análise de dados de vendas."""

    def carregar_dados(self, fonte: str) -> None:
        print(f" Carregando dados de vendas do arquivo: {fonte}")

    def limpar_dados(self) -> None:
        print(" Limpando dados de vendas (removendo duplicatas, valores nulos etc.)")

    def analisar_dados(self) -> None:
        print(" Analisando tendências de vendas e desempenho por produto...")

    def gerar_relatorio(self) -> None:
        print(" Relatório final: vendas totais e top 5 produtos mais vendidos.")

    def hook_apos_carregar(self) -> None:
        print(" Pré-visualização rápida: primeiros 5 registros de vendas carregados.")


# ====================================================================
# SUBCLASSE CONCRETA 2: Pipeline de Detecção de Fraudes
# ====================================================================
class PipelineDeteccaoFraude(PipelineDeDados):
    """Pipeline específico para detectar fraudes em transações."""

    def carregar_dados(self, fonte: str) -> None:
        print(f" Carregando transações bancárias do arquivo: {fonte}")

    def limpar_dados(self) -> None:
        print(" Removendo transações inválidas ou incompletas...")

    def analisar_dados(self) -> None:
        print(" Aplicando modelo de machine learning para detectar fraudes suspeitas...")

    def gerar_relatorio(self) -> None:
        print(" Relatório final: lista de transações suspeitas enviadas para auditoria.")

    def hook_apos_limpar(self) -> None:
        print(" Total de transações válidas após limpeza: 98.2%.")


# ====================================================================
# EXEMPLO DE USO
# ====================================================================
if __name__ == "__main__":
    print("\n=== PIPELINE 1: Análise de Vendas ===")
    pipeline_vendas = PipelineAnaliseVendas()
    pipeline_vendas.executar_pipeline("vendas.csv")

    print("\n=== PIPELINE 2: Detecção de Fraudes ===")
    pipeline_fraudes = PipelineDeteccaoFraude()
    pipeline_fraudes.executar_pipeline("transacoes.csv")
