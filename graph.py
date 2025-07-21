import os
path = "FTIRAnalysis/data/"

filenames = [i for i in os.listdir(path) if i.endswith(".txt")]

import matplotlib.pyplot as plt
def plot_spectrum(filename):
    filepath = os.path.join(path, filename)
    
    with open(filepath, 'r') as file:
        lines = file.readlines()

    for i in range(4):
        if lines[i].startswith("#"):
            lines.pop(i)

    
    wavenumbers = []
    transmittance = []
    for line in lines:
        if line.strip():
            parts = line.split()
            if len(parts) == 2:
                wavenumbers.append(float(parts[0]))
                transmittance.append(float(parts[1]))
    plt.figure(figsize=(10, 6))
    plt.plot(wavenumbers, transmittance, label=filename)
    plt.xlabel("Wavenumber (cm⁻¹)")
    plt.ylabel("Transmittance (%)")
    plt.title("FTIR Spectrum")
    plt.legend()
    plt.grid()
    plt.show()

def plot_all_spectra():
    for filename in filenames:
        plot_spectrum(filename)

plot_all_spectra()