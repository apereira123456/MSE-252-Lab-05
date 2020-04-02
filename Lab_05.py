import numpy as np

g = 9.81

Width = 0.001 * np.mean([1.52,1.56,1.62])
Thickness = 0.001 * np.mean([0.89,0.97,0.86])

I = Width * Thickness ** 3 / 12

Mass_Penny = 0.001 * 2.755
Mass_Cup = 0.001 * 12.38

Control_Length = 0.001 * 29.90
Control_Pennies = np.array([150,300])
Control_Mass = Mass_Cup + Mass_Penny * Control_Pennies
Control_Deflection = 0.001 * np.array([15.53,27.91])

Annealed_Length = 0.001 * 30.94
Annealed_Pennies = np.array([10,20,30,150,300])
Annealed_Mass = Mass_Cup + Mass_Penny * Annealed_Pennies
Annealed_Deflection = 0.001 *  np.array([2.67,3.18,3.59,25.55,27.31])

Quenched_Length = 0.001 * 34.11
Quenched_Pennies = np.array([10,20,30,40])
Quenched_Mass = Mass_Cup + Mass_Penny * Quenched_Pennies
Quenched_Deflection = 0.001 * np.array([1.96,2.80,3.37,4.75])

E_Control = 10**(-9) * g * Control_Mass * Control_Length ** 3 \
          / (3 * I * Control_Deflection)
E_Annealed = 10**(-9) * g * Annealed_Mass * Annealed_Length ** 3 \
           / (3 * I * Annealed_Deflection)
E_Quenched = 10**(-9) * g * Quenched_Mass * Quenched_Length ** 3 \
           / (3 * I * Quenched_Deflection)

Control = np.array([np.mean(E_Control),np.std(E_Control)])
Annealed = np.array([np.mean(E_Annealed),np.std(E_Annealed)])
Quenched = np.array([np.mean(E_Quenched),np.std(E_Quenched)])

print(Control)
print(Annealed)
print(Quenched)