# 🐝 Beecrowd Progress
[![Solved](https://img.shields.io/badge/Solved-11/3400-brightgreen)](https://www.beecrowd.com.br/judge/pt/profile/1210688)
[![Rank](https://img.shields.io/badge/Rank-%23352499-blue)](https://www.beecrowd.com.br/judge/pt/ranking/)
![Python](https://img.shields.io/badge/Python-3.x-yellow)

Acompanho meu avanço resolvendo desafios da Beecrowd (URI) em Python.

**Perfil**: [1210688](https://www.beecrowd.com.br/judge/pt/profile/1210688)


## Sumário
- [Objetivos](#objetivos)
- [Como rodar](#como-rodar)
- [Automação](#automação)

## Stats Diárias
| Data        | Hoje | Total | Rank     |
|-------------|------|-------|----------|
| 04/02/2026 | 18 | **18**| **#352499** |
| 02/02/2026 | 11   | **11**| **#352499**|

## Objetivos
- [ ] Completar a categoria Beginner
- [ ] Iniciar a categoria Ad-Hoc
- [ ] Automatizar captura de estatísticas diretamente da Beecrowd

## Como rodar
```bash
python beginner/1001.py < input.txt
```

## Automação
- Workflow: `.github/workflows/update_stats.yml` roda a cada push e atualiza o README.
- Script: `scripts/update_readme.py` conta exercícios e preenche a tabela de stats.
