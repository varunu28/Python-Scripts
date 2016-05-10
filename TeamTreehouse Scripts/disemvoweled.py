#Program to remove all the vowels from a list of words and then to uppercase all the first letters of words in the array


#Function to remove all the vowels
def devowel(arr):  
    i = 0
    while i<len(arr):
        j=0
        arr[i] = list(arr[i])
        while j<len(arr[i]):
            if arr[i][j] == 'a' or arr[i][j] == 'e' or arr[i][j] == 'i' or arr[i][j] == 'o' or arr[i][j] == 'u':
                del arr[i][j]
                j-=1
            j+=1
        arr[i] = ''.join(arr[i])
        i+=1
    return arr

#Function to capitalize first letter of every word
def caps_on(arr):
    i = 0
    while i<len(arr):
        arr[i] = ' '.join(word[0].upper() + word[1:] for word in arr[i].split())
        i+=1
    return arr

arr = ['aegfd', 'wjq' , 'wjwqa', 'wuksi']

#Original string list
print(arr)

#Changed string list
print(caps_on(devowel(arr))) 
