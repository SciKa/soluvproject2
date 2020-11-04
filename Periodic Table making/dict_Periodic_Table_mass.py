pero = open('periodic_table.txt','r',encoding='UTF8')
pero_list = pero.read()
print(pero_list)

atom_list = pero_list.split('\n')
for i in range(len(atom_list)):
    atom_list[i] = atom_list[i].split('\t')

for i in range(len(atom_list)):
    atom_list[i] = [atom_list[i][0],atom_list[i][8]]

for i in range(len(atom_list)):
    atom_list[i][1] = atom_list[i][1].strip("[]qwertyuiopasdfghjklzxcvbnm")
    atom_list[i][1] = atom_list[i][1].replace(')','')
    atom_list[i][1] = atom_list[i][1].replace('(', '')
    atom_list[i][1] = float(atom_list[i][1])
    atom_list[i][0] = int(atom_list[i][0])

atom_dict_1H = dict(atom_list)

for i in range(len(atom_list)):
    index0 = atom_list[i][0]
    index1 = atom_list[i][1]
    atom_list[i][0] = index1
    atom_list[i][1] = index0

atom_dict_H1 = dict(atom_list)

print(atom_dict_1H)
print(atom_dict_H1)

#result
{1: 1.008, 2: 4.0026022, 3: 6.94, 4: 9.01218315, 5: 10.81, 6: 12.011, 7: 14.007, 8: 15.999, 9: 18.9984031636, 10: 20.17976, 11: 22.989769282, 12: 24.305, 13: 26.98153857, 14: 28.085, 15: 30.9737619985, 16: 32.06, 17: 35.45, 18: 39.9481, 19: 39.09831, 20: 40.0784, 21: 44.9559085, 22: 47.8671, 23: 50.94151, 24: 51.99616, 25: 54.9380443, 26: 55.8452, 27: 58.9331944, 28: 58.69344, 29: 63.5463, 30: 65.382, 31: 69.7231, 32: 72.6308, 33: 74.9215956, 34: 78.9718, 35: 79.904, 36: 83.7982, 37: 85.46783, 38: 87.621, 39: 88.905842, 40: 91.2242, 41: 92.906372, 42: 95.951, 43: 98.0, 44: 101.072, 45: 102.905502, 46: 106.421, 47: 107.86822, 48: 112.4144, 49: 114.8181, 50: 118.7107, 51: 121.7601, 52: 127.603, 53: 126.904473, 54: 131.2936, 55: 132.905451966, 56: 137.3277, 57: 138.905477, 58: 140.1161, 59: 140.907662, 60: 144.2423, 61: 145.0, 62: 150.362, 63: 151.9641, 64: 157.253, 65: 158.925352, 66: 162.5001, 67: 164.930332, 68: 167.2593, 69: 168.934222, 70: 173.0451, 71: 174.96681, 72: 178.492, 73: 180.947882, 74: 183.841, 75: 186.2071, 76: 190.233, 77: 192.2173, 78: 195.0849, 79: 196.9665695, 80: 200.5923, 81: 204.38, 82: 207.21, 83: 208.980401, 84: 209.0, 85: 210.0, 86: 222.0, 87: 223.0, 88: 226.0, 89: 227.0, 90: 232.03774, 91: 231.035882, 92: 238.028913, 93: 237.0, 94: 244.0, 95: 243.0, 96: 247.0, 97: 247.0, 98: 251.0, 99: 252.0, 100: 257.0, 101: 258.0, 102: 259.0, 103: 266.0, 104: 267.0, 105: 268.0, 106: 269.0, 107: 270.0, 108: 277.0, 109: 278.0, 110: 281.0, 111: 282.0, 112: 285.0, 113: 286.0, 114: 289.0, 115: 290.0, 116: 293.0, 117: 294.0, 118: 294.0}
{1.008: 1, 4.0026022: 2, 6.94: 3, 9.01218315: 4, 10.81: 5, 12.011: 6, 14.007: 7, 15.999: 8, 18.9984031636: 9, 20.17976: 10, 22.989769282: 11, 24.305: 12, 26.98153857: 13, 28.085: 14, 30.9737619985: 15, 32.06: 16, 35.45: 17, 39.9481: 18, 39.09831: 19, 40.0784: 20, 44.9559085: 21, 47.8671: 22, 50.94151: 23, 51.99616: 24, 54.9380443: 25, 55.8452: 26, 58.9331944: 27, 58.69344: 28, 63.5463: 29, 65.382: 30, 69.7231: 31, 72.6308: 32, 74.9215956: 33, 78.9718: 34, 79.904: 35, 83.7982: 36, 85.46783: 37, 87.621: 38, 88.905842: 39, 91.2242: 40, 92.906372: 41, 95.951: 42, 98.0: 43, 101.072: 44, 102.905502: 45, 106.421: 46, 107.86822: 47, 112.4144: 48, 114.8181: 49, 118.7107: 50, 121.7601: 51, 127.603: 52, 126.904473: 53, 131.2936: 54, 132.905451966: 55, 137.3277: 56, 138.905477: 57, 140.1161: 58, 140.907662: 59, 144.2423: 60, 145.0: 61, 150.362: 62, 151.9641: 63, 157.253: 64, 158.925352: 65, 162.5001: 66, 164.930332: 67, 167.2593: 68, 168.934222: 69, 173.0451: 70, 174.96681: 71, 178.492: 72, 180.947882: 73, 183.841: 74, 186.2071: 75, 190.233: 76, 192.2173: 77, 195.0849: 78, 196.9665695: 79, 200.5923: 80, 204.38: 81, 207.21: 82, 208.980401: 83, 209.0: 84, 210.0: 85, 222.0: 86, 223.0: 87, 226.0: 88, 227.0: 89, 232.03774: 90, 231.035882: 91, 238.028913: 92, 237.0: 93, 244.0: 94, 243.0: 95, 247.0: 97, 251.0: 98, 252.0: 99, 257.0: 100, 258.0: 101, 259.0: 102, 266.0: 103, 267.0: 104, 268.0: 105, 269.0: 106, 270.0: 107, 277.0: 108, 278.0: 109, 281.0: 110, 282.0: 111, 285.0: 112, 286.0: 113, 289.0: 114, 290.0: 115, 293.0: 116, 294.0: 118}