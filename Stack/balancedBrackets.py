def balancedBrackets(string):
	
	stack = []
	open_bracket = ['(','{','[']
	closing_bracket = [')','}',']']
	matching_pair = {'(':')','{':'}','[':']'}
	#matching_pair = set([('(',')'),('{','}'),('[',']')])
	
	for bracket in string:
		
		#Below condition valid only if string passed 
		#contains only brackets and no other characters
		#if len(string)%2!=0:
		#	return False
		
		if bracket in open_bracket:
			stack.append(bracket)
		
		elif bracket in closing_bracket:
			if len(stack)==0:
				return False
			
			last_open_bracket = stack.pop()
			if matching_pair[last_open_bracket]!=bracket:
			#if (last_open_bracket,bracket) not in matching_pair:
				return False
	
	return len(stack)==0
				
    
	
