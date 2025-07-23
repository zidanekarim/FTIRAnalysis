import os
import matplotlib.pyplot as plt

path = "FTIRAnalysis/data/"
graphpath = "graphs/"
filenames = [i for i in os.listdir(path) if i.endswith(".txt")]

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

#plot_all_spectra()

def plot_spectrum_overlayed(filenames):
    plt.figure(figsize=(10, 6))
    for filename in filenames:
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
        
        plt.plot(wavenumbers, transmittance, label=filename)
    
    plt.xlabel("Wavenumber (cm⁻¹)")
    plt.ylabel("Transmittance (%)")
    plt.title("Overlayed FTIR Spectra")
    plt.legend()
    plt.grid()
    plt.show()

fleece_natural = ["FleeceControl1.txt", "FleeceNatural1Weeks_11.txt", "FleeceNatural2Weeks_11.txt", 
                 "FleeceNat3Week11.txt"]
fleece_synthetic = ["FleeceControl1.txt", "FleeceUV3Weeks_11.txt", "FleeceUV2Weeks_11.txt",   "FleeceUV1Weeks_11.txt"]

nylon_natural = ["NylonControl1.txt", "NylonNatural1Weeks_11.txt", "NylonNatural2Weeks_11.txt", 
                 "NylonNat3Weeks_11.txt"]
nylon_synthetic = ["NylonControl1.txt", "NylonUV3Weeks_11.txt", "NylonUV2Weeks_11.txt",   "NylonUV1Weeks_11.txt"]

polyester_natural = ["PolyesterControl1.txt", "PolyesterNatural1Weeks_11.txt", "PolyesterNatural2Weeks_11.txt", 
                 "PolyesterNat3Week1.txt"]

polyester_synthetic = ["PolyesterControl1.txt", "PolyesterUV3Weeks_11.txt", "PolyesterUV2Weeks_11.txt",   "PolyesterUV1Weeks_11.txt"]


plot_spectrum_overlayed(fleece_natural)
plot_spectrum_overlayed(fleece_synthetic)
plot_spectrum_overlayed(nylon_natural)
plot_spectrum_overlayed(nylon_synthetic)
plot_spectrum_overlayed(polyester_natural)
plot_spectrum_overlayed(polyester_synthetic)
