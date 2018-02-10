#usr/local/bin
def view_dir(path='.'):
	names = os.lisetdir(path)
	names.sort()
	for name in names:
		print(name,end =' ')
	print()
