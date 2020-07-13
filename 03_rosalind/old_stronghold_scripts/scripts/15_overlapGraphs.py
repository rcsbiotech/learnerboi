#!/usr/bin/env python

"""
-------------------------------------------------------------------------------
Rosalind Problem No: 15
Title: Overlap Graphs

A graph whose nodes have all been labeled can be represented by an adjacency list,
in which each row of the list contains the two node labels corresponding to a 
unique edge.

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
(Na prática, quer o grafo correspondente a strings com overlap mínimo de 3)

-------------------------------------------------------------------------------
rc.silva@unesp.br
"""

# Libraries
import sys
from Bio import SeqIO

# Variables
## Inicializa o dicionário de nucleotídeos FASTA;
fasta_records = {}

## Inicializa o contador de pontuação do alinhamento;
align_score = 0

## Inicializa a lista de sucesso e gatilho de repetição de cabeçalhos
sus = []
seqpair1 = []
seqpair2 = []
repeated_flag = 0

## K_score: sobreposição necessária para formar uma ponta no grafo
k_score = 3

# Input fasta file (argv[1])
fasta_fh = open(sys.argv[1], 'r')

# Captura os fastas como dicionário
for entry in SeqIO.parse(fasta_fh, "fasta"):
	fasta_records[entry.id] = entry.seq
	# print(entry.id)
	# print(entry.seq)

""" Lógica do grafo

1. Para cada entrada no dicionário de fastas;
2. Para cada entrada no dicionário que não seja a entrada acima;
3. Faça o alinhamento entre as duas:
	a. Para cada nucleotídeo da primeira sequência:
		b. Para cada nucleotídeo da segunda sequência:
			Se o primeiro for igual ao segundo, some 1;
				Se o segundo for igual ao segundo, some 1;
					Se o terceiro for igual ao terceiro, some 1;
			Se não for, resete a soma para zero e passe para o próximo;
			Se a soma chegar a 3, salve os dois registros separados por espaços;
"""

# print("\nStarting loop over fasta...\n")

# Laço sobre dicionário
## Para cada chave de consulta (cabeçalho fasta)
for key_query, value_query in fasta_records.items():

	# print("Query: ", key_query)
	
	## Para cada chave de referência (subject)
	for key_subject, value_subject in fasta_records.items():

		# Zera o alinhamento
		align_score = 0

		# print("Subject capturado...")
		# print("Subject: ", key_subject, "\n")

		## Se eles não forem os mesmos
		if (key_query != key_subject):

			# print("Not equal!\n")
			while (align_score < k_score and align_score != -1):

				""" Sequência como dicionário (loop while):
				--------------------------------------------------------------

				O trecho abaixo foi removido pois tratava as seqs.
				como dicionários, vou tentar processar como sequências
				ou tuplas (indexadas por inteiro) para acessar os nucleotídeos
				numericamente.

				--------------------------------------------------------------
				## Execute o alinhamento com soma
				for nucl_query in fasta_records[key_query]:

					# print(nucl_query)
					for nucl_subject in fasta_records[key_subject]:

						# Compara os nucleotídeos
						if nucl_query == nucl_subject:

							# Soma 01 à pontuação do alinhamento
							align_score = align_score + 1
				-------------------------------------------------------------
				"""

				# Captura o tamanho das strings
				query_size = len(value_query)
				subject_size = len(value_subject)

				# Percorrer a query
				travel_length_query = 0
				travel_length_subject = len(value_subject) - k_score

				""" Sobre o contador interno (internal_counter) e gatilho de alinhamento (align_flag)
				-----------------------------------------------
				O contador interno serve para movimentar a subject,
				caso nenhum nucleotídeo da query tenha dado match.
				Assim, se configuram as situações para avançar a sequência:

				1. Hit no primeiro nucleotídeo, avançam ambas (query & subject)
				2. Não-hit no primeiro, avança a query uma vez;
				3. Hit no segundo, avançam ambos;
				4. Não-hit no segundo, avança a query novamente;

				O gatilho de alinhamento mantém o código em modo de alinhamento até
				que ocorra mismatch, quando ele reinicia o alinhamento para a próxima query
				-----------------------------------------------
				"""
				
				## Inicializa o contador interno
				internal_counter = 0

				## Gatilho de alinhamento: ao zerar, para de alinhar
				## Deve ser reiniciado a cada sequência
				align_flag = 1

				## Zera a pontuação do alinhamento antes de começar
				align_score = 0

				## Informes do alinhamento
				# print("Query:\n>",key_query,"\n",value_query)
				# print("Subject:\n>",key_subject,"\n",value_subject)

				while (internal_counter < query_size - 1 and
						align_score < k_score and
						align_flag == 1):

					# print("Iniciando loop maior")
					# print("Contador interno: ", internal_counter)
					# print("Tamanho da query: ", query_size)
					# print("Pontuação do alinhamento: ", align_score)
					# print("Pontuação alvo: ", k_score)
					
					# No primeiro alinhamento, começa com passo zero
					align_step = 0

					# print("Deve alinhar? ", align_flag, "\n")
					while (align_flag == 1):

						# print("Iniciando loop menor")

						# Se os nucleotídeos são iguais
						if ( value_query[travel_length_query] == value_subject[travel_length_subject] and
						travel_length_query <= k_score - 1 and
						travel_length_subject <= subject_size and
						align_score < k_score):

							# Registra a posição do nucleotídeo inicial
							if (align_step == 0):
								internal_counter = travel_length_query
							
							# Soma o alinhamento
							align_score = align_score + 1

							## MT: Tamanho da query e subject
							# print("Percorrendo a query, posição: ", travel_length_query)
							# print("Percorrendo o subject, posição: ", travel_length_subject)
							# print("Pontuação: ", align_score)
							# print("Pontuação alvo: ", k_score)
	
							# Avança query e subject
							travel_length_query = travel_length_query + 1
							travel_length_subject = travel_length_subject + 1

							# Avança um passo no alinhamento
							align_step = align_step + 1

							# Se o score já for o desejado, solicite parar de alinhar
							if (align_score == k_score):
								break
							
							# print("Deve continuar alinhando? 1 - Sim; 0 - Não, Resultado: ", align_flag)
							# print("E agora josé?\n")
						else:
							# print("Iniciada condição contrária!")

							# Percorre apenas a query, sem avançar a subject
							travel_length_query = internal_counter + 1
							internal_counter = internal_counter + 1
							travel_length_subject = 0
			
							# Zera a pontuação: não são aceitos mismatches
							align_score = 0

							# Zera o passo do alinhamento no máximo 7 vezes
							if (travel_length_query < query_size - k_score):
								align_step = 0
							else:
								align_flag = 0
								align_score = -1
							
				if (align_score == 3):
				
					# Crie as strings
					pair1 = key_query + " " + key_subject
					pair2 = key_subject + " " + key_query

					# Para cada elemento, marque se houver repetido
					for element in sus:
						if (pair1 == element):
							repeated_flag = 1

					# Grude os novos elementos
					sus.append(pair1)
					# sus.append(pair2)

					# Se não houver repetido, imprima
					if (repeated_flag == 0):
						print(key_subject, key_query)
					
					# Zere o gatilho
					repeated_flag = 0




					



