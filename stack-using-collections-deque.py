from collections import deque 
  
stack = deque() 
  
stack.append('1') 
stack.append('2') 
stack.append('3') 
  
print('Initial stack:') 
print(stack) 

print('\nElements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
  
print('\nStack after elements are poped:') 
print(stack) 