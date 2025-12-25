# Quantum Random Number Generator (QRNG) 🎲💻

Este projeto implementa um Gerador de Números Aleatórios Quânticos utilizando o SDK **Qiskit**. [cite_start]O objetivo é demonstrar a aplicação prática de conceitos fundamentais da computação quântica para gerar aleatoriedade real através do colapso da função de onda[cite: 32, 71].

##  Estrutura do Projeto

[cite_start]O repositório está dividido em duas frentes principais, refletindo o fluxo de desenvolvimento profissional[cite: 17, 18, 50]:

### 1. Pesquisa e Visualização (`notebooks/`)
Contém o arquivo `.ipynb` utilizado para a fase de experimentação.
* **Objetivo:** Visualizar o circuito quântico e analisar a distribuição estatística dos resultados através de histogramas.
* [cite_start]**Uso:** Ideal para aprendizado e demonstração visual da porta Hadamard e da superposição quântica[cite: 71].

### 2. Produção e Scripting (`src/`)
Contém o arquivo `generator.py` com a lógica modularizada.
* **Objetivo:** Funcionar como uma ferramenta reutilizável que pode ser integrada a outros sistemas.
* **Diferencial:** Implementa funções (`def`) com tratamento de erros e seleção automática de backends (simuladores Aer/QASM).

## Fundamentos Quânticos Aplicados

* [cite_start]**Superposição:** Uso da porta **Hadamard (H)** para criar estados equiprováveis[cite: 71].
* [cite_start]**Álgebra Linear:** Representação de estados através de vetores no espaço de Hilbert e operadores matriciais[cite: 55, 71].
* [cite_start]**Medição:** Processo de colapso que converte informação quântica em bits clássicos aleatórios[cite: 71].

## 🛠️ Como Rodar o Projeto

### Configuração do Ambiente
```bash
# Clone e entre na pasta
git clone [https://github.com/SEU_USUARIO/quantum-rng.git](https://github.com/SEU_USUARIO/quantum-rng.git)
cd quantum-rng

# Ambiente Virtual
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt