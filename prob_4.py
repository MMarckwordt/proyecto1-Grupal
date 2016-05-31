def prob_4 (num, palabra):
	cas= (num -len(palabra))//2
	centrado= num*(cas + len (palabra))
	return "*"*cas+palabra+"*"cas2