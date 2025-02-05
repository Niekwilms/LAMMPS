# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:50:51 2025

@author: wilms
"""

import numpy as np
import matplotlib.pyplot as plt

file_name = "C:/Users/wilms/Downloads/rdf_T0.5_rho0.4.txt"

# Functie om de data in te laden
def load_data(filename):
    # Lees alle regels
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Maak een lijst voor alle data
    data_list = []
    global n_timesteps
    n_timesteps = 0
    # Loop door de regels
    i = 0
    while i < len(lines):
        # Sla commentaar regels over
        if lines[i].startswith('#'):
            i += 1
            continue
        
        # Sla timestep header over
        if len(lines[i].split()) == 2:
            i += 1
            n_timesteps += 1
            continue
        
        # Voeg data regel toe
        values = [float(x) for x in lines[i].split()]
        if len(values) == 8:  # Alleen regels met 8 kolommen
            data_list.append(values)
        i += 1
        
    # Converteer naar numpy array
    return np.array(data_list)

# Laad de data
data = load_data(file_name)
  
# Zorgen nu dat we een iets mooiere data set hebben qua dataverwerking
# Hebben een aantal tijdsteps al in het doorlezen van het bestand toegevoegd
# Nu kunnen we de data uit elkaar halen daarmee en makkelijker gemiddeldes verwerken

rows_per_timestep = int(np.max(data[:,0]))
data_3d = data.reshape(n_timesteps, rows_per_timestep, 8)

# Bereken gemiddelde
avg_data = np.mean(data_3d, axis=0)

# Plot individuele timesteps 
#Nul is eruit gehaald gezien die een rare piek liet zien, vermoedelijk door nog het equilibirum vinden
#of het komt nog uit de potentiele energie gedeeltes. 
for timestep in range(n_timesteps):
    if timestep > 0: 
        plt.plot(data_3d[timestep,:,1], data_3d[timestep,:,2], 'b-', alpha=0.1, label='g++ (per timestep)' if timestep==1 else "")
        plt.plot(data_3d[timestep,:,1], data_3d[timestep,:,4], 'r-', alpha=0.1, label='g+- (per timestep)' if timestep==1 else "")
        plt.plot(data_3d[timestep,:,1], data_3d[timestep,:,6], 'g-', alpha=0.1, label='g-- (per timestep)' if timestep==1 else "")

# Plot gemiddelde RDF, nu alleen met wat mooiere lijn die niet zo dun is
plt.plot(avg_data[:,1], avg_data[:,2], 'b-', linewidth=2, label='g++ (gemiddeld)')
plt.plot(avg_data[:,1], avg_data[:,4], 'r-', linewidth=2, label='g+- (gemiddeld)')
plt.plot(avg_data[:,1], avg_data[:,6], 'g-', linewidth=2, label='g-- (gemiddeld)')

#maak t plaatje nog mooier  
plt.xlabel('r/σ', fontsize=12)
plt.ylabel('g(r)', fontsize=12)
plt.title('Radiale Distributie Functies\nGemiddeld over 10 timesteps', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

#%% c(r) bepalen

















