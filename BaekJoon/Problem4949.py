result = []
while(True):
    text = input()
    if(text == '.'):
        break
    stack =[]


    if(len(text)==0):
        break
    for x in range(len(text)):
        if(text[x] == "(" or text[x] == ")" or text[x] == "[" or text[x] == "]" ):
            if(text[x] == ')'):
                if(len(stack)==0):
                    stack.append("*")
                    break     
                if(stack[-1]=='('):       
                    stack.pop()
                else:
                    stack.append(")")
                    
            elif(text[x] ==']'):
                if(len(stack)==0):
                    stack.append("*")
                    break
                if(stack[-1]=='['):
                    stack.pop()
                else:
                    stack.append("]")
                
            else:
                stack.append(text[x])

    if(len(stack) == 0):
        result.append("yes")
    else:
        result.append("no")
            
for i in result:
    print(i)