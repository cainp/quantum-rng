from qiskit import QuantumCircuit
from qiskit_aer import Aer
qbits = 8

def quantum_random_number_generator(qbits):
    #  Cria um circuito com qbits qubits e bits clássicos
    qc = QuantumCircuit(qbits, qbits)

    # Aplica a porta Hadamard para criar superposição
    for i in range(qbits):
        qc.h(i)

    # 3. Mede os qubits
    qc.measure(range(qbits), range(qbits))

    # Executa no simulador local (Aer)
    try:
        backend = Aer.get_backend('aer_simulator')
    except Exception:
        backend = Aer.get_backend('qasm_simulator')

    job = backend.run(qc, shots=1000, memory=True)
    result = job.result()

    # Obtém o bit gerado
    bit = result.get_memory()[0]
    decimal_number = int(bit, 2)
    print(f"Número Quântico Gerado: {bit} -> {decimal_number}")
    return bit, decimal_number

if __name__ == "__main__":
    # Testando com 8 bits
    try:
        resultado_bin, resultado_dec = quantum_random_number_generator(qbits)
    except ValueError as e:
        print(f"Erro ao gerar número quântico: {e}")