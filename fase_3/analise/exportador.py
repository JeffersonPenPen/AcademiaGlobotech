import os
import re
from analise.sistema_fase3 import SistemaAnaliseEngajamento

class Exportador:
    def __init__(self, caminho="relatorios"):
        self.caminho = os.path.abspath(caminho)

    def exportar_relatorios(self, sistema):
        conteudo = [
            ("Top Conteúdos por Consumo", sistema.relatorio1_top_conteudos_por_consumo()),
            ("Usuários Mais Engajados", sistema.relatorio2_usuarios_mais_engajados()),
            ("Engajamento por Plataforma", sistema.relatorio3_engajamento_por_plataforma()),
            ("Conteúdos Mais Comentados", sistema.relatorio4_conteudos_mais_comentados()),
            ("Total de Interações por Tipo", sistema.relatorio5_total_interacoes_por_tipo()),
            ("Tempo Médio por Plataforma", sistema.relatorio6_tempo_medio_por_plataforma()),
            ("Comentários por Conteúdo", sistema.relatorio7_comentarios_por_conteudo()),
            ("Conteúdos Mais Interagidos", sistema.relatorio8_conteudos_mais_interagidos()),
        ]

        relatorios_validados = 0

        for i, (titulo, resultado) in enumerate(conteudo, start=1):
            nome_arquivo = os.path.join(self.caminho, f"{titulo}.txt")
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write(f"TÁ NA GLOBO: {titulo}\n")
                f.write(str(resultado))
            print(f"Salvo: {nome_arquivo}")
            relatorios_validados += 1

        if relatorios_validados == 0:
            print("Nenhum relatório disponível.")
