import re, collections

Token = collections.namedtuple('Token', ['type', 'value', 'lineNumber', 'column'])

class Lexer:

    __token_specification = [
        ('OPEN_BRACE', r'{'),
        ('CLOSE_BRACE', r'}'),
        ('OPEN_PARENTHESIS', r'\('),
        ('CLOSE_PARENTHESIS', r'\)'),
        ('SEMICOLON', r';'),
        ('KEYWORD_INT', r'int'),
        ('KEYWORD_RETURN', r'return'),
        ('IDENTIFIER', r'[a-zA-Z]\w*'),
        ('INTEGER', r'[0-9]+'),
        ('SKIP', r'[ \t]+'), # Skip spaces and tabs
        ('NEWLINE', r'\n'), # Line ending
        ('MISMATCH', r'.')  # Any other character
    ]
    __tokenPatternObject = 0

    def __init__(self):
        self.__initialiseTokens()

    def __initialiseTokens(self):        
        token_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.__token_specification)
        self.__tokenPatternObject = re.compile(token_regex)

    def run(self, source_file):
        self.__lex(source_file)
        pass

    def __lex(self, source_file):
        tokens = []

        lineNumber = 1
        lineStart = 0
        with open(source_file, 'r') as f:
            for mo in self.__tokenPatternObject.finditer(f.read()):
                tokenType = mo.lastgroup
                tokenValue =  mo.group(tokenType)
                if tokenType == 'SKIP':
                    pass
                elif tokenType == 'NEWLINE':
                    lineStart = mo.end()
                    lineNumber += 1
                elif tokenType == 'MISMATCH':
                    raise RuntimeError('{tokenValue!r} unexpected on line {lineNumber}')
                else:
                    column = mo.start() - lineStart
                    tokens.append(Token(tokenType, tokenValue, lineNumber, column))
                # print 1/0
            # print line
        
        print tokens
        print 1/0
    def __parseWord(self, word):
        return "TOKEN"
    