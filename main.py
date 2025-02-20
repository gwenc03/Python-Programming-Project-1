def twos_compliment_plus(x,y):  
    result = ""
    carryNum = 0

    for i in range (len(x)):
      inputX = (ord(x[-(i + 1)]) - ord ("0")) 
      inputY = (ord(y[-(i + 1)]) - ord ("0"))
      
      sum = inputX + inputY + carryNum
      carryNum = sum // 2
      sum = str(sum % 2)
      
      result = sum + result

    if x[0] == y[0] and result[0] != x[0]:
      result = "Error Overflow"
    
    return result
    
   

#twos_compliment_plus("11111111","00000001")
#twos_compliment_plus("00011001","01001110")
#twos_compliment_plus('00111000','11101110')
#twos_compliment_plus('00110111','01011001')