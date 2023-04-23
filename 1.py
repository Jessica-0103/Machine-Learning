# Jessica Chouhan (0827CI201087)  
# indentation example    branch = 'CSIT' if branch == 'CSIT':  
    print('Welcome to CSIT') else:      print('Other branch') print('All set !')  

Comments in Python  
# Jessica Chouhan (0827CI201087)    
print('This is python code')  
# this is single line comment  
"""  
This is a multiline comment in Python that spans several lines. This application is a Computer Science portal for geeks.   
"""  

If-else statement 
5.	# Jessica Chouhan(0827CI201087)
6.	#if example
7.	number = 10
8.	if number > 0:
9.	    print('Number is positive.')
10.	
11.	print('The if statement is easy')
12.	
13.	#if-else example
14.	number = 10
15.	if number > 0:
16.	    print('Positive number')
17.	else:
18.	    print('Negative number')
19.	
20.	print('This statement is always executed')
21.	
22.	#nested id-else example
23.	number = 5
24.	if (number >= 0):
25.	    # inner if statement
26.	    if number == 0:
27.	      print('Number is 0')
28.	    # inner else statement
29.	    else:
30.	        print('Number is positive')
31.	# outer else statement
32.	else:
33.	    print('Number is negative')
34.	    
35.	#if elif example
36.	number = 0
37.	if number > 0:
38.	    print("Positive number")
39.	elif number == 0:
40.	    print('Zero')
41.	else:
42.	    print('Negative number')
43.	
44.	print('This statement is always executed')

LIST
# Jessica Chouhan(0827CI201087)  
#List Data structure   fruits 	= 	['mango','apple',1000,'banana','orange',True,58.50] 
print(fruits)                           
print('element at index 3 '+fruits[3])  
print('length of list ',len(fruits))    #print length of list fruits.append(2020.55);          
#append to the list fruits.insert(2,False);                 
fruits.extend([8,'potato']);            
fruits.reverse(); 	 	 	
fruits.remove('apple'); 	
fruits.pop(3);          
#remove at index 3 fruits.clear();  
# fruits.sort();                        
print(fruits);  

Tuple 
# Jessica Chouhan(0827CI201087)    
# myTuple = ('banana', 'apple', 'orange', 'pineapple');   #creating tuple using tuple constructor myTuple = tuple(('banana', 'apple', 'orange', 'pineapple'))  
  print(myTuple)  print('length of tuple : ',len(myTuple));       
print('element at 2 ',myTuple[2]);              #access element using indexing  print(myTuple[1:3])                             #slicing from index 1 to 2  print(myTuple.count('banana'))                  #count occurrence of banana  print('banana' in myTuple)                      # print true if present mylist = ['banana', 'apple', 'orange', 'pineapple']; convertedTuple = tuple(mylist);                     #convert list into tuple   

Strings in Python  
# Jessica Chouhan(0827CI201087) 
#string data structure  
 str = 'Welcome to the CSIT Department' print(str[0])                   #accessing using index print(str.capitalize())         #capitalize the string print(''.join(reversed(str)))   #reverse the string print(str[2:8])                 
#string slicing print(list(str))                #convert string to list  #delete entire string String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print(str.count('to'))            #count the word to print(str.split('the'))           #split into list based on word 'the' print(str.upper())                #convert into uppercase print(str.lower())                #convert into lowercase print(str.find('the'))            #return the starting index of 'the' print(str.index('to'))            #return the index of 'to'   

Dictionary in Python  
# Jessica Chouhan (0827CI201087)   #Dictionary data structure   myDict = {100:'Sahil' ,
200:'Jessica',300:'Palak',400:'',500:'Jeet',600:'Shivansh'}; print(myDict)  print(myDict.get(400))          #get value using key print(myDict.values())          #prints only values print(myDict.keys())            #prints only keys print(myDict.pop(400))          #pop item which has key 400 print(myDict.popitem())         #pop last item  del(myDict[100])                #delete item which has key 100 myDict.update({10000:"Gitu"})      #add new element at last print(myDict.__sizeof__())  

Lambda Functions  
# Jessica Chouhan (0827CI201087)   
#lamda function   square = lambda x:x*2  
  
List = [1,2,3,4,5,6,7,8] newList = list(map(square , List)) print(newList)   

Class and Object  
# Jessica Chouhan (0827CI201087)  
#class and object   
#declaring class student class Student:  
    def __init__(self, name, age, grade):  
        self.name = name         self.age = age         self.grade = grade  
      
     
  
    def details(self):  
        print('name is : ',self.name)                 print('age is : ',self.age)                 print('grade is : ',self.grade)                   def get_name(self):         
return self.name           def get_age(self):         
return self.age           def get_grade(self):         
return self.grade           def set_name(self, name):          self.name = name           def set_age(self, age):          self.age = age           def set_grade(self, grade):          self.grade = grade  
  
#initializing object s1      s1 = Student('kuldeep',20,92) s1.details()  
  
