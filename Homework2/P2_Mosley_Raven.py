# a)
#Loops through a,b,c,d from 1 to 10, keeeps if all four are different 
# a*a + b*b + c*c + d*d
#Reference: Chapter 7 and program 7-15
abcd_list = [(a, b, c, d) for a in range(1, 11) for b in range(1, 11)
             for c in range(1, 11) for d in range(1, 11)
             if len({a, b, c, d}) == 4 and a*a + b*b == c*c + d*d]
print(abcd_list)

# b)
#Creates  a tuple of the lowercase word and length and only keeps words shoter than five letters.
#Reference: chapter 6 and program 6-4
lst = ['One', 'SEVEN', 'three', 'two', 'Ten']

short_list = [(s.lower(), len(s)) for s in lst if len(s) < 5]
print(short_list)          

# c)
#Splits the names into 3 diferent parts - first, middle, and last
#puts back together with first letter of middle name
#Reference: chatper 8 and program 8-3
names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']

new_names = [parts[0] + " " + parts[1][0] + ". " + parts[2]
             for parts in [name.split() for name in names]]
print(new_names)         

# d)
#checks every word in 1st1 vs 1st2, two words are anagrams if the words are the same after being sorted.
# Reference: chatper 7 and program 7-19

lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

anagrams = [(w1, w2) for w1 in lst1 for w2 in lst2
            if sorted(w1.lower()) == sorted(w2.lower())]
print(anagrams)

# e)
#Make a dictionary each word is the key and its length is the value
#Reference: chatper 7 and program 7-7
s = ['one', 'two', 'three']
len_dict = {word: len(word) for word in s}
print(len_dict)           

# f)
#the position is the key and the letter is the value, only keep the letter if its a vowel.
#Refernece: chater 6 and program 6-5
text = "Hello world"

vowel_dict = {i: text[i] for i in range(len(text)) if text[i].lower() in "aeiou"}
print(vowel_dict)       

#Reference: Chapters 6, 7, and 8