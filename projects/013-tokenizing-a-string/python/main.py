def tokenizing_expression(expression):
    operator_list=['*','/','^','-','+']
    expression=list(expression.replace(' ',''))
    expression_tokenized=[]
    token_collector=[]
    for element in expression:
        if element in operator_list:
            if len(token_collector)>0:
                expression_tokenized.append(''.join(token_collector))
                token_collector.clear()
            expression_tokenized.append(element)
        else:
            token_collector.append(element)
    expression_tokenized.append(''.join(token_collector)) #add last number token
    return expression_tokenized

def main():
    expression=input('Please enter a valid math expression:')
    token_list=tokenizing_expression(expression)
    print(token_list)

if __name__=='__main__':
    main()