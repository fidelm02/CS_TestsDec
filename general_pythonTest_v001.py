#
# Cinesite test 01
#
#   Fidel Moreno Miranda
#     fidelm02@gmail.com
#	       December 2018
#
# ----------------------------------------------------------
#
# General Python test:
#    write a function that finds all animated sequences 
#    in a given directory and prints their frame ranges 
#    in the following format: 
#        'name: 1001-2000' if there are no gaps
#        'name: 1001, 1003-1500, 1600-2000' if there are gaps
#    the format for an animated sequence is name.####.ext 
#    e.g. /job/.../my_render_v001.1001.jpg


def getSequences(s_path):
	from os import listdir, path
	from os.path import isfile

	# Get all images that match with the format
	imgs = [f for f in listdir(s_path) if isfile(path.join(s_path, f)) and 
		len(f.split('.')) == 3]

	# Identify sequences and divided files by extension
	sequences = []
	for img in imgs:
		reg = img.split('.')
		found = False
		for seq in sequences:
			if seq[0] == reg[0]:
				found = True
				foundExt = False
				for ext in seq[1]:
					if ext[0] == reg[2]:
						foundExt = True
						ext[1].append(reg[1])
				if not foundExt:
					seq[1].append( (reg[2], [reg[1]]) )
		if not found:
			newSeq = ( reg[0], [( reg[2], [reg[1]] )] )
			sequences.append(newSeq)

	# Identify gaps
	for seq in sequences:
		# Verify gaps by extension
		for ext in seq[1]:
			ranges = []
			initial = final = None
			# Avoid rare cases that files are not sorted by name
			ext[1].sort()
			for i in range(len(ext[1])):
				frame = ext[1][i]
				if not initial:
					initial = final =  int(frame)
					if i == len(ext[1]) -1:
						ranges.append([final])
				else:
					if final != int(frame) -1:
						if initial != final:
							ranges.append([initial, final])
						else:
							ranges.append([final])
						initial = final = int(frame)
						if i == len(ext[1]) -1:
							ranges.append([final])
					else:
						final = int(frame)
						if i == len(ext[1]) -1:
							if initial != final:
								ranges.append([initial, final])
							else:
								ranges.append([final])
			gaps = None
			for r in ranges:
				gap = '{0}'.format(r[0]) if len(r) == 1 else '{0}-{1}'.format(r[0], r[1])
				gaps = gap if not gaps else '{0}, {1}'.format(gaps, gap)
			
			# Identify if more than one sequence match but with different extension
			# If not multiple extension, then print the normal line description
			if len(seq[1]) > 1:
				print '{0} ({1}): {2}'.format(seq[0], ext[0], gaps)
			else:
				print '{0}: {1}'.format(seq[0], gaps)

			#'name: 1001-2000' if there are no gaps
        	#'name: 1001, 1003-1500, 1600-2000' if there are gaps
        	#'name (ext): 1001, 1003-1500, 1600-2000' if there are 
        	#        gaps and multiple extensions

# getSequences('/your_path')

