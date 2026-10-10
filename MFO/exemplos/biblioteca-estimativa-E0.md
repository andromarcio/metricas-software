# Estimativa MFO — Biblioteca 1.0 (indicativa)

**Rótulo:** ≈ 55 PFO (estimativa E0, 33 a 77) · MFO 1.0 · nível R · evidência 0% · agente: ferramenta (mfo.py estimar 1.0); sem revisão humana · escopo: Biblioteca 1.0 (indicativa), 3 entidades mantidas (Livro, Leitor, Emprestimo) e 2 só lidas ou geradas

| Indicador | Valor |
|---|---|
| Nível da estimativa | E0 |
| Processos estimados | 12 |
| PFO do modelo (perfis típicos) | 55 |
| Intervalo | 33 a 77 PFO |
| Base | perfis padrão do capítulo 11 (sem calibração local) |
| Medido (para conferência) | 51 PFO · erro relativo 8% |

## Itens

| ID | Processo | Tipo | Entidades | PFO |
|---|---|---|---|---|
| Livro-C | Cadastrar Livro | criar | Livro | 4 |
| Livro-A | Alterar Livro | alterar | Livro | 4 |
| Livro-E | Excluir Livro | excluir | Livro | 3 |
| Livro-L | Consultar Livro | consultar | Livro | 4 |
| Leitor-C | Cadastrar Leitor | criar | Leitor | 4 |
| Leitor-A | Alterar Leitor | alterar | Leitor | 4 |
| Leitor-E | Excluir Leitor | excluir | Leitor | 3 |
| Leitor-L | Consultar Leitor | consultar | Leitor | 4 |
| Emprestimo-C | Cadastrar Emprestimo | criar | Emprestimo, Leitor, Livro | 6 |
| Emprestimo-A | Alterar Emprestimo | alterar | Emprestimo, Leitor, Livro | 6 |
| Emprestimo-E | Excluir Emprestimo | excluir | Emprestimo, Leitor, Livro | 5 |
| Emprestimo-L | Consultar Emprestimo | consultar | Emprestimo, Leitor, Livro | 8 |

Todos os movimentos estão marcados como inferidos (evidência 0%); a extração substitui cada um por evidência conforme os artefatos surgem.

