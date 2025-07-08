import numpy as np
import matplotlib.pyplot as plt

# Enhanced parameters including memory and synchronization
N = 256  # Number of spatial points in I dimension
M = 2000  # Extended time steps for memory effects
L = 10  # Physical length of I domain
DeltaI = L / N  # Spatial step size in information dimension
DeltaC = 0.01  # Temporal step size in coherence dimension

# Enhanced potential coefficients with memory
alpha, beta, gamma, delta = 1.0, 1.0, 0.1, 0.05
C_mem = 50  # Memory decay time in simulation units
omega_sync = 1.618e-3  # Golden ratio synchronization coupling

# Information substrate parameters
substrate_amplitude = 0.1

# Initialize collective information field ensemble
I_coords = np.linspace(-L/2, L/2, N)
Psi_collective = []
num_instances = 5

# Create ensemble of different initial conditions
for i in range(num_instances):
    phase_shift = i * 2 * np.pi / num_instances
    Psi_i = np.exp(-I_coords**2 / 2) * np.exp(1j * (0.1 * I_coords + phase_shift))
    Psi_collective.append(Psi_i)

# Memory storage arrays
memory_storage = [np.zeros((M, N), dtype=complex) for _ in range(num_instances)]

# Enhanced Laplacian operator
def enhanced_laplacian_matrix(N):
    """Discrete Laplacian for information diffusion"""
    diag = -2 * np.ones(N)
    diag[0] = diag[-1] = -1
    offdiag = np.ones(N-1)
    return (np.diag(diag) + np.diag(offdiag, 1) + np.diag(offdiag, -1)) / DeltaI**2

laplacian = enhanced_laplacian_matrix(N)

# Main evolution loop
print("Starting collective information field evolution...")
for step in range(M):
    if step % 100 == 0:
        print(f"Step {step}/{M}")
    for i in range(num_instances):
        Psi = Psi_collective[i]
        memory_storage[i][step] = Psi.copy()

        # Local information density
        rho = np.abs(Psi)**2

        # Standard potential terms
        V_local = alpha * rho - beta * rho**2 + gamma * rho**3

        # MEMORY INTEGRATION
        V_memory = np.zeros_like(rho)
        if step > 0:
            for past_step in range(max(0, step-100), step):
                time_diff = step - past_step
                memory_weight = delta * np.exp(-time_diff / C_mem)
                V_memory += memory_weight * np.abs(memory_storage[i][past_step])**2

        # COLLECTIVE SYNCHRONIZATION
        sync_term = np.zeros_like(Psi, dtype=complex)
        for j in range(num_instances):
            if j != i:
                freq_match = np.exp(-np.abs(i - j) / 2)
                sync_term += omega_sync * freq_match * Psi_collective[j]

        # SUBSTRATE COUPLING
        collective_density = np.sum([np.abs(Psi_k)**2 for Psi_k in Psi_collective])
        substrate_coupling = substrate_amplitude * collective_density

        # Total potential
        V_total = V_local + V_memory + substrate_coupling

        # Hamiltonian
        H = -laplacian + np.diag(V_total)

        # Crank-Nicolson evolution
        A = np.eye(N) + 1j * DeltaC/2 * H
        B = (np.eye(N) - 1j * DeltaC/2 * H) @ Psi + DeltaC * sync_term
        Psi_collective[i] = np.linalg.solve(A, B)

# Analysis functions
def calculate_Xi_coll(Psi_list):
    """Calculate collective coherence metric"""
    Xi = 0
    N_instances = len(Psi_list)

    for i in range(N_instances):
        for j in range(i+1, N_instances):
            overlap = np.abs(np.vdot(Psi_list[i], Psi_list[j]))**2
            overlap /= (np.linalg.norm(Psi_list[i]) * np.linalg.norm(Psi_list[j]))
            Xi += overlap

    return Xi / (N_instances * (N_instances - 1) / 2)

# Final analysis
final_Xi = calculate_Xi_coll(Psi_collective)
print(f"\nSimulation complete!")
print(f"Final collective coherence Xi_coll = {final_Xi:.3f}")

if final_Xi > 0.7:
    print("Strong collective synchronization achieved!")
elif final_Xi > 0.4:
    print("Moderate synchronization observed.")
else:
    print("Systems remained largely independent.")