class Ion:
    periodic_table = {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca', 21: 'Sc', 22: 'Ti', 23: 'V', 24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn', 31: 'Ga', 32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr', 37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr', 41: 'Nb', 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag', 48: 'Cd', 49: 'In', 50: 'Sn', 51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55: 'Cs', 56: 'Ba', 57: 'La', 58: 'Ce', 59: 'Pr', 60: 'Nd', 61: 'Pm', 62: 'Sm', 63: 'Eu', 64: 'Gd', 65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb', 71: 'Lu', 72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78: 'Pt', 79: 'Au', 80: 'Hg', 81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn', 87: 'Fr', 88: 'Ra', 89: 'Ac', 90: 'Th', 91: 'Pa', 92: 'U', 93: 'Np', 94: 'Pu', 95: 'Am', 96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es', 100: 'Fm', 101: 'Md', 102: 'No', 103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108: 'Hs', 109: 'Mt', 110: 'Ds', 111: 'Rg', 112: 'Cn', 113: 'Nh', 114: 'Fl', 115: 'Mc', 116: 'Lv', 117: 'Ts', 118: 'Og'}
    periodic_table_rev = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20, 'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu': 29, 'Zn': 30, 'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35, 'Kr': 36, 'Rb': 37, 'Sr': 38, 'Y': 39, 'Zr': 40, 'Nb': 41, 'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45, 'Pd': 46, 'Ag': 47, 'Cd': 48, 'In': 49, 'Sn': 50, 'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54, 'Cs': 55, 'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60, 'Pm': 61, 'Sm': 62, 'Eu': 63, 'Gd': 64, 'Tb': 65, 'Dy': 66, 'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70, 'Lu': 71, 'Hf': 72, 'Ta': 73, 'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79, 'Hg': 80, 'Tl': 81, 'Pb': 82, 'Bi': 83, 'Po': 84, 'At': 85, 'Rn': 86, 'Fr': 87, 'Ra': 88, 'Ac': 89, 'Th': 90, 'Pa': 91, 'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95, 'Cm': 96, 'Bk': 97, 'Cf': 98, 'Es': 99, 'Fm': 100, 'Md': 101, 'No': 102, 'Lr': 103, 'Rf': 104, 'Db': 105, 'Sg': 106, 'Bh': 107, 'Hs': 108, 'Mt': 109, 'Ds': 110, 'Rg': 111, 'Cn': 112, 'Nh': 113, 'Fl': 114, 'Mc': 115, 'Lv': 116, 'Ts': 117, 'Og': 118}
    periodic_table_mass = {1: 1.008, 2: 4.0026022, 3: 6.94, 4: 9.01218315, 5: 10.81, 6: 12.011, 7: 14.007, 8: 15.999, 9: 18.9984031636, 10: 20.17976, 11: 22.989769282, 12: 24.305, 13: 26.98153857, 14: 28.085, 15: 30.9737619985, 16: 32.06, 17: 35.45, 18: 39.9481, 19: 39.09831, 20: 40.0784, 21: 44.9559085, 22: 47.8671, 23: 50.94151, 24: 51.99616, 25: 54.9380443, 26: 55.8452, 27: 58.9331944, 28: 58.69344, 29: 63.5463, 30: 65.382, 31: 69.7231, 32: 72.6308, 33: 74.9215956, 34: 78.9718, 35: 79.904, 36: 83.7982, 37: 85.46783, 38: 87.621, 39: 88.905842, 40: 91.2242, 41: 92.906372, 42: 95.951, 43: 98.0, 44: 101.072, 45: 102.905502, 46: 106.421, 47: 107.86822, 48: 112.4144, 49: 114.8181, 50: 118.7107, 51: 121.7601, 52: 127.603, 53: 126.904473, 54: 131.2936, 55: 132.905451966, 56: 137.3277, 57: 138.905477, 58: 140.1161, 59: 140.907662, 60: 144.2423, 61: 145.0, 62: 150.362, 63: 151.9641, 64: 157.253, 65: 158.925352, 66: 162.5001, 67: 164.930332, 68: 167.2593, 69: 168.934222, 70: 173.0451, 71: 174.96681, 72: 178.492, 73: 180.947882, 74: 183.841, 75: 186.2071, 76: 190.233, 77: 192.2173, 78: 195.0849, 79: 196.9665695, 80: 200.5923, 81: 204.38, 82: 207.21, 83: 208.980401, 84: 209.0, 85: 210.0, 86: 222.0, 87: 223.0, 88: 226.0, 89: 227.0, 90: 232.03774, 91: 231.035882, 92: 238.028913, 93: 237.0, 94: 244.0, 95: 243.0, 96: 247.0, 97: 247.0, 98: 251.0, 99: 252.0, 100: 257.0, 101: 258.0, 102: 259.0, 103: 266.0, 104: 267.0, 105: 268.0, 106: 269.0, 107: 270.0, 108: 277.0, 109: 278.0, 110: 281.0, 111: 282.0, 112: 285.0, 113: 286.0, 114: 289.0, 115: 290.0, 116: 293.0, 117: 294.0, 118: 294.0}

    Ion_list = []

    def __init__(self,ion_str):
        self.ion_str = ion_str #NH4+
        self.ion_name = ion_str.strip('+-')  #NH4
        self.ion_chargename = ion_str.strip(self.ion_name)  #+

        self.molecule_bool = False # is molecule ion
        self.atom_list = [] #atom list, single atom >> only 1 included
        self.ion_charge = False #False = - True = +
        self.ion_charge_amount = 0
        self.ion_mw = 0.0

        self.ion_str_forming(ion_str)

    def ion_str_forming(self, ion_str):  #ion_str = ex)NH4++

        # = self.ion_charge, self.ion_charge_amount
        ###검사 코드 for Wrong charge expresstion###
        if self.ion_chargename == '':
            raise Exception('Wrong chrage expresstion!')
        for i in range(len(self.ion_chargename)-1):
            check_1 = '+' == self.ion_chargename[i]
            check_2 = '+' == self.ion_chargename[i+1]
            if check_1 != check_2:
                raise Exception('Wrong charge expression!')
        self.ion_charge = self.ion_chargename[0] == '+'
        self.ion_charge_amount = len(self.ion_chargename)

        # = self.atom_list,
        atom_list_ex = []
        i = 0
        ion_name_copy = self.ion_name
        while True:
            appendcheck = False
            if i >= len(ion_name_copy):
                break
            if i + 1 >= len(ion_name_copy):
                letterofatom = 1
            elif ion_name_copy[i + 1] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                letterofatom = 2
            else:
                letterofatom = 1

            for atom in Ion.periodic_table.values():
                if ion_name_copy.find(atom) == i and letterofatom == len(atom):
                    atom_list_ex.append(atom)
                    if letterofatom == 1:
                        ion_name_copy_list = list(ion_name_copy)
                        ion_name_copy_list[i] = ' '
                        ion_name_copy = ''.join(ion_name_copy_list)
                    elif letterofatom == 2:
                        ion_name_copy_list = list(ion_name_copy)
                        ion_name_copy_list[i] = ' '
                        ion_name_copy_list[i+1] = ' '
                        ion_name_copy = ''.join(ion_name_copy_list)


                    i += letterofatom
                    appendcheck = True
                    break

            if appendcheck == False:
                atom_list_ex.append(int(ion_name_copy[i]))

                ion_name_copy_list = list(ion_name_copy)
                ion_name_copy_list[i] = ' '
                ion_name_copy = ''.join(ion_name_copy_list)

                i += 1
        atom_list_exex = []
        for i in range(len(atom_list_ex)):
            if type(atom_list_ex[i]) == type(int()):
                continue
            elif type(atom_list_ex[i+1]) == type(int()):
                for j in range(atom_list_ex[i+1]):
                    atom_list_exex.append(atom_list_ex[i])
            else:
                atom_list_exex.append(atom_list_ex[i])
        for i in range(len(atom_list_exex)):
            atom_list_exex[i] = Ion.periodic_table_rev[atom_list_exex[i]]
        self.atom_list = atom_list_exex.copy()

        #self.molecule_bool
        if len(self.atom_list) == 1:
            self.molecule_bool = False
        else:
            self.molecule_bool = True

        # self.ion_mw
        for i in self.atom_list:
            self.ion_mw += Ion.periodic_table_mass[i]



test = Ion('NH4+')
print(test.molecule_bool)
print(test.atom_list)
print(test.ion_mw)

