kappa_c = 1500
kappa_s = 1000
kappa_m = 1.9
k_c = 60
k_s = 10
k_l = 1.2
T = 800  # "[K]Temperature"
xH2 = 0.95
pfuel = 1.1
xO2 = 0.21
pair = 1.1
V_cell = 0.7    # [V]Cell voltage
kappa_p = 1e-13  # "[m^2]GDL permeability"
eta = 2.1e-5  # "[Pa*s]Fluid viscosity"
p_ref = 1.0133E5  # "[pa]Reference pressure"
drag = 3  # "Proton-Water drag coefficient through membrane"
E_eq_a = 0  # "[V]Equilibrium potential, anode"
E_eq_c = 1  # "[V]Equilibrium potential, cathode"
i0_a = 1e5  # "[A/m^2]Exchange current density, anode"
i0_c = 1  # "[A/m^2]Exchange current density, cathode"
S = 1e7  # "[m^2/m^3]Specific surface area"
R_agg = 0.1e-6  # "[um]Aggregate radius"
eps_mic = 0.2  # "Microscopic porosity inside agglomerates"
eps_mac = 0.4  # "Macroscopic porosity between agglomerates"
D_agg = 1.2e-10 * ((1 - eps_mac) * eps_mic) ** 1.5  # "Effective diffusion coefficient inside agglomerates[m^2/s]"
D_effH2_H2O = 0.915e-4 * (T / 307.1) ** 1.5 * (eps_mac) ** 1.5  # "Effective binary diffusivity, H2_H2O[m^2/s][K]"
D_effO2_N2 = 0.22e-4 * (T / 293.2) ** 1.5 * (eps_mac) ** 1.5  # "Effective binary diffusivity, O2_N2[m^2/s][K]"
D_effH2O_N2 = 0.256e-4 * (T / 307.5) ** 1.5 * (eps_mac) ** 1.5  # "Effective binary diffusivity, H2O_N2[m ^ 2 / s][K]"
D_effO2_H2O = 0.282e-4 * (T / 308.1) ** 1.5 * (eps_mac) ** 1.5  ##"Effective binary diffusivity, O2_H2O[m ^ 2 / s][K]"
wH2_in = 0.1  # "Inlet weight fraction H2"
wO2_in = 0.21 * 0.8  # "Inlet weight fraction O2"
wH2Oc_in = 0.2  # "Cathode inlet weight fraction, H2O"
MH2 = 2  # "[g/mol]Molar mass, H2"
MO2 = 32  # "[g/mol]Molar mass, O2"
MH2O = 18  # "[g/mol]Molar mass, H2O"
MN2 = 28  # "[g/mol]Molar mass, N2"
xH2_in = (wH2_in / MH2) / (wH2_in / MH2 + (1 - wH2_in) / MH2O)  # "Inlet molar fraction, H2"
xO2_in = (wO2_in / MO2) / (wO2_in / MO2 + wH2Oc_in / MH2O + (1 - wO2_in - wH2Oc_in) / MN2)  # "Inlet molar fraction, O2"
KH2 = 3.9e4  # "[Pa*m^3/mol]Henry's law constant, H2 in agglomerate"
KO2 = 3.2e4  # "[Pa*m^3/mol]Henry's law constant, O2 in agglomerate"
cH2_ref = xH2_in * p_ref / KH2  # "Reference concentration, H2"
cO2_ref = xO2_in * p_ref / KO2  # "Reference concentration, O2"
cH2O_ref = (1 - xH2_in) * p_ref / KH2  # "Reference concentration, H2"
l_act = 10e-6  # "[um]Active layer thickness"
F_const = 96485.33289
# F_const = 96485  
R_const = 8.31446261815324  
# R_const = 8.3145  
K = -6 * l_act * (1 - eps_mac) * F_const * D_agg / R_agg ** 2






