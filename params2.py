p_atm = 1 * 101325  # "Atmospheric pressure"[pa]
T = 800 + 273.15  # [K] Temperature
mu = 3e-5  # "Viscosity, air"[Pa*s]
dp_a = 2  # "Pressure drop, anode"[Pa]
dp_c = 6  # "Pressure drop, cathode"[Pa]
i0_a = 0.1  # "Exchange current density, anode"[A/m^2]
i0_c = 0.01  # "Exchange current density, cathode"[A/m^2]
Sa_a = 1e9  # "Specific surface area, anode"[1/m]
Sa_c = 1e9  # "Specific surface area, cathode"[1/m]
V_pol = 0.05  # "Initial cell polarization"[V]
perm_a = 1e-10  # "Anode permeability"[m^2]
perm_c = 1e-10  # "Cathode permeability"[m^2]
Eeq_a = 0  # "Equilibrium voltage, anode"[V]
Eeq_c = 1  # "Equilibrium voltage, cathode"[V]
V_cell = 0.7  # "Cell voltage"[V]
kleff_a = 1  # "Electrolyte effective conductivity, anode"[S/m]
kseff_a = 1000  # "Solid effective conductivity, anode"[S/m]
kleff_c = 1  # "Electrolyte effective conductivity, cathode"[S/m]
kseff_c = 1000  # "Solid effective conductivity, cathode"[S/m]
kl = 5  # "Electrolyte conductivity"[S/m]
ks = 5000  # "Current collector conductivity"[S/m]
vh2 = 6e-6  # "Kinetic volume, H2"
vo2 = 16.6e-6  # "Kinetic volume, O2"
vn2 = 17.9e-6  # "Kinetic volume, N2"
vh2o = 12.7e-6  # "Kinetic volume, H2O"
Mh2 = 2  # "Molar mass, H2"[g/mol]
Mo2 = 32  # "Molar mass, O2"[g/mol]
Mn2 = 28  # "Molar mass, N2"[g/mol]
Mh2o = 18  # "Molar mass, H2O"[g/mol]
kd = 3.16e-8  # "Reference diffusivity"[m^2/s]
e_por = 0.4  # Porosity
F_const = 96485.33289  # "法拉第常数[C/mol]"
R_const = 8.31446261815324  # "气体常数[J/(mol·K)]"
Dh2h2o = kd * (T) ** 1.75 / (p_atm * (vh2 ** (1 / 3) + vh2o ** (1 / 3)) ** 2) * (
            1e3 / Mh2 + 1e3 / Mh2o) ** 0.5  # "Diffusivity, H2-H2O"
Do2h2o = kd * (T) ** 1.75 / (p_atm * (vo2 ** (1 / 3) + vh2o ** (1 / 3)) ** 2) * (
            1e3 / Mo2 + 1e3 / Mh2o) ** 0.5  # "Diffusivity, O2-H2O"
Do2n2 = kd * (T) ** 1.75 / (p_atm * (vo2 ** (1 / 3) + vn2 ** (1 / 3)) ** 2) * (
            1e3 / Mo2 + 1e3 / Mn2) ** 0.5  # "Diffusivity, O2-N2"
Dn2h2o = kd * (T) ** 1.75 / (p_atm * (vh2o ** (1 / 3) + vn2 ** (1 / 3)) ** 2) * (
            1e3 / Mh2o + 1e3 / Mn2) ** 0.5  # "Diffusivity, N2-H2O"
w_h2ref = 0.4  # "Inlet weight fraction, H2 at anode"
w_o2ref = 0.15  # "Inlet weight fraction, O2 at cathode"
w_h2oref = 0.37  # "Inlet weight fraction, H2O at cathode"
c_tot = p_atm / (R_const * T)  # "Total molar concentration"
c_o2ref = c_tot * (w_o2ref / Mo2) / (w_o2ref / Mo2 + w_h2oref / Mh2o + (
            1 - w_o2ref - w_h2oref) / Mn2)  # "Reference concentration, O2 at cathode"
c_h2ref = c_tot * (w_h2ref / Mh2) / (w_h2ref / Mh2 + (1 - w_h2ref) / Mh2o)  # "Reference concentration, H2 at anode"
c_h2oref = c_tot * ((1 - w_h2ref) / Mh2o) / (
            w_h2ref / Mh2 + (1 - w_h2ref) / Mh2o)  # "Reference concentration, H2O at anode"
W_channel = 0.5e-3  # "Gas flow channel width"[m]
W_rib = 0.5e-3  # "Rib width"[m]
H_gde = 1e-4  # "Gas diffusion electrode thickness"[m]
H_electrolyte = 1e-4  # "Electrolyte thickness"[m]
H_channel = 0.5e-3  # "Gas flow channel height"[m]
L = 10e-3  # "Flow channel length"[m]
