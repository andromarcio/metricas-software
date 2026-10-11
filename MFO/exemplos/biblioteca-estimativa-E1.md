# Estimativa MFO — Biblioteca 1.0 (estimativa)

**Rótulo:** ≈ 43 PFO (estimativa E1, 32 a 54) · MFO 1.0 · nível R · evidência 0% · agente: ferramenta (mfo.py estimar 1.0); sem revisão humana · escopo: Biblioteca 1.0 (estimativa), 9 itens da proposta comercial, equivalentes a RF-01 a RF-09

| Indicador | Valor |
|---|---|
| Nível da estimativa | E1 |
| Processos estimados | 9 |
| PFO do modelo (perfis típicos) | 43 |
| Intervalo | 32 a 54 PFO |
| Base | perfis padrão do capítulo 11 (sem calibração local) |
| Medido (para conferência) | 54 PFO · erro relativo 20% |

## Itens

| ID | Processo | Tipo | Entidades | PFO |
|---|---|---|---|---|
| P01 | Cadastrar livro | criar | Livro | 4 |
| P02 | Alterar livro | alterar | Livro | 4 |
| P03 | Excluir livro | excluir | Emprestimo, Livro | 4 |
| P04 | Consultar livros | consultar | Livro | 3 |
| P05 | Cadastrar leitor | criar | Leitor | 4 |
| P06 | Registrar empréstimo | criar | Emprestimo, Leitor, Livro | 6 |
| P07 | Registrar devolução | criar | Emprestimo, ParametroMulta | 5 |
| P08 | Relatório de atrasos | relatorio | Emprestimo, Leitor, Livro | 7 |
| P09 | Notificar atrasos por e-mail | processar | Emprestimo, Leitor, Livro, Notificacao | 6 |

Todos os movimentos e desfechos estão marcados como inferidos (evidência 0%); a extração substitui cada um por evidência conforme os artefatos surgem.

