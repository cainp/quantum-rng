# Quantum Random Number Generator (QRNG)

Este projeto implementa um Gerador de Números Aleatórios Quânticos utilizando o SDK **Qiskit**. Ao contrário de geradores pseudo-aleatórios clássicos baseados em algoritmos determinísticos, este projeto utiliza a natureza inerentemente probabilística da mecânica quântica.

## Fundamentos Quânticos

* [cite_start]**Superposição:** Através da porta **Hadamard (H)**, cada qubit é colocado em um estado onde as probabilidades de medir 0 ou 1 são iguais (50/50). [cite: 71]
* [cite_start]**Colapso da Função de Onda:** No momento da medição, o estado de superposição colapsa para um estado definido (0 ou 1), gerando um bit verdadeiramente aleatório. [cite: 71]
* [cite_start]**Escalabilidade:** O circuito é projetado para trabalhar com múltiplos qubits, gerando strings de bits que são convertidas para números decimais. [cite: 49]

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12+
* [cite_start]**Framework Quântico:** Qiskit (Aer Simulator) [cite: 55]
* **Ambiente:** WSL 2 (Ubuntu)
* **Gerenciamento:** venv e pip

##  Como Rodar o Projeto

### 1. Requisitos Prévios
Certifique-se de ter o Python instalado e o WSL 2 configurado.

### 2. Configuração do Ambiente
No seu terminal Ubuntu:

```bash
# Clone o repositório
git clone [https://github.com/SEU_USUARIO/quantum-rng.git](https://github.com/SEU_USUARIO/quantum-rng.git)
cd quantum-rng

# Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt