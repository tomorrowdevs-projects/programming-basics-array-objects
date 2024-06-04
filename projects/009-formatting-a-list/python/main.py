def format_list(text_list):
   if len(text_list)>2:
        text_formatted=', '.join(text_list[:len(text_list)-2])
        text_formatted='{} and {}'.format(text_formatted,text_list[len(text_list)-1])
   elif len(text_list)==2:
        text_formatted=' and '.join(text_list)
   else:
       text_formatted=str(text_list[0])
   return text_formatted

def main():
   text_list=list()
   word=input('Enter a word:')
   while word!='':
        text_list.append(word)
        word=input('Enter another word:')
   text_formatted=format_list(text_list)
   print(text_formatted)

if __name__=='__main__':
    main() 