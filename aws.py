import cudaq 
from cudaq import spin 

cudaq.set_target("nvidia-mqpu")

cudaq.mpi.initialize()
num_ranks = cudaq.mpi.num_ranks() 
rank = cudaq.mpi.rank() 

print('mpi is initialized? ', cudaq.mpi.is_initialized())
print('rank', rank, 'num_ranks', num_ranks)


qubit_count = 15
term_count = 100000

kernel = cudaq.make_kernel()
qubits = kernel.qalloc(qubit_count)
kernel.h(qubits[0])
for i in range(1, qubit_count):
    kernel.cx(qubits[0], qubits[i])

hamiltonian = cudaq.SpinOperator.random(qubit_count, term_count)

# Single node, single GPU.
result = cudaq.observe(kernel, hamiltonian) 
result.expectation() 

# Single node, multi-GPU.
result = cudaq.observe(kernel, hamiltonian, execution = cudaq.parallel.thread)  
result.expectation() 

# Multi-node, multi-GPU.
result = cudaq.observe(kernel, hamiltonian, execution = cudaq.parallel.mpi) 
result.expectation() 

cudaq.mpi.finalize()
