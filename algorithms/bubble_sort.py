def bubble_sort():
  #EMPTY ARRAY 
  array = []
  
  #NUNBER OF VALUES YOU WANT IN YOUR ARRAY 
  n = int(input("Enter the number of values u want:  "))
  while n > 100 or n < 3: 
    print("Value should be between 3 and 100")
    try:
      n = int(input("Enter a value for n: "))
    except ValueError:
      print("NOT AN INTEGER: ")
      return
  
  #INPUTING N TIMES INTO ARRAY 
  for k in range(n):
    #checking if type is of int 
    try:
      item = int(input(f"Input enter an integer {k} : "))
    except ValueError:
      print("NOT AN INTERGER: ")
      return
    array.append(item)
    
  #UNSORTED ARRAY 
  print(f"UNSORTED ARRAY: {array}")
    
  for i in range(len(array)):
    #iterator 
    for b in range(len(array)-1):
      try:
        if(array[b+1] < array[b]):
          temp = array[b+1]
          array[b+1] = array[b]
          array[b] = temp
      except IndexError:
        pass
    
  #SORTED ARRAY
  print(f"SORTED ARRAY: {array}")
  
  
bubble_sort()
      
      