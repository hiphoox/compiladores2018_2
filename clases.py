


def symbolss(piece):
	if piece == '(':
		return 'OpenParen'
	if piece == ')':
		return 'CloseParen'
	if piece == '{':
		return 'OpenBrace'
	if piece == '}':
		return 'CloseBrace'
	if piece == ';':
		return 'Semicolon'
	if piece == '-':
		return 'Negation'
	if piece == '~':
		return 'Bitwise'
	if piece == '!':
		return 'Logic_Neg'

def words(piece):
	if piece == 'int' or piece == 'return':
		return 'Keyword'
	else:
		return 'ID'