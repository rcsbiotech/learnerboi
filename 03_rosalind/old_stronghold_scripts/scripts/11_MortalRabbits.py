#!/usr/bin/env python

#!/usr/bin/env python

# Necessário para importar arquivos
import sys
#from collections import defaultdict

# Capturar o arquivo
data_fh = open(sys.argv[1], 'r')

# Captura a string da primeira linha
intel = data_fh.readline()

# Remove newline
intel = str(intel.rstrip('\n'))

# Separa os elementos
split_intel = intel.split(' ')

# Cria uma variável cada
var_mo = int(split_intel[0])
var_li = 1
var_su = int(split_intel[1])

# AT
print("Months to cycle: ", var_mo)
print("Rabbits per litter: ", var_li)
print("Life expectancy: ", var_su)
print('\n')

## Number of rabbits, starting month
rab_no = {};
cur_mo = 1

while cur_mo < var_mo + 1:

	if (cur_mo == 1 or cur_mo == 2):
		rab_no[cur_mo] = 1
	elif cur_mo == 3:
		rab_no[cur_mo] = 2
	else:
		var_dsc = cur_mo - (var_su + 1)

		if var_dsc < 1: 
			var_dsc = 1

		if cur_mo <= var_su:
			var_dsc = 0

		prev_mo = cur_mo - 1
		prev_2_mo = cur_mo - 2

		if var_dsc <= 0:
			
			print("No one died this month.")
			print("Previous month : ", rab_no[prev_mo])
			print("Two months past: ", rab_no[prev_2_mo])
			print("Current month: ", cur_mo)

			rab_no[cur_mo] = \
					rab_no[prev_mo] + \
					rab_no[prev_2_mo]

		else:
			print("Discount: ", rab_no[var_dsc])
			print("Previous month : ", rab_no[prev_mo])
			print("Two months past: ", rab_no[prev_2_mo])
			print("Current month: ", cur_mo)

			rab_no[cur_mo] = \
					rab_no[prev_mo] + \
					rab_no[prev_2_mo] - \
					rab_no[var_dsc]

		print("Rabbits for this month: ", rab_no[cur_mo], "\n")

	# Atualiza o mês, reinicia o loop
	cur_mo = cur_mo + 1

print(rab_no)

	
