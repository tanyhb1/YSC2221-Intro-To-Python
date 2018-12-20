import csv
import numpy as np

#==============================================================================#
#                                  Question 1                                  #
#==============================================================================#

# Input: < string > file path
# Output: < sequence of sequences > 2D array
# Hint: This is a helper function.
def read_csv_into_2d_array(file_path):
    ## FILL IN HERE
    return list(csv.reader(open(file_path)))


# Input: < string > file path to treasure map csv
# Output: < tuple > coordinates of treasure.
def find_treasure(file_path_map):
    ## FILL IN HERE
    data = np.array(read_csv_into_2d_array(file_path_map))
    ans = ()
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if data[i,j] == "x":
                ans = (i,j)
    return ans


# Uncomment code below to test (DO NOT paste into Coursemology!)
print("*** QUESTION 1 ***")
print(find_treasure('treasure.csv'))


#==============================================================================#
#                                  Question 2                                  #
#==============================================================================#

# Input: < string > file path to translation guide csv
# Output: < dict >  translation guide
def read_translation_guide_into_dictionary(file_path_translation):
    ## FILL IN HERE
    data = np.array(read_csv_into_2d_array(file_path_translation))
    cipher = {}
    for i in range(1, len(data)):
        cipher[data[i,0]] = data[i,1]
    return cipher



# Uncomment code below to test (DO NOT paste into Coursemology!)
print("*** QUESTION 2 ***")
print(read_translation_guide_into_dictionary('translation.csv'))



#==============================================================================#
#                                  Question 3                                  #
#==============================================================================#

# NOTE: There is a difference between ' and " in a string.

# RECALL THAT:
# >>> print("foo")
# 3
# >>> print('"foo"')
# "foo"


# Input: < string > file path to encrypted message csv
# Output: < string > encrypted message
# Hint: This is a helper function.
def read_message(file_path_message):
    ## FILL IN HERE
    with open(file_path_message, 'r') as f:
        x = f.readlines()
    return(x[0])

read_message("message.txt")

# Input 1: < dict > translation guide
# Input 2: < string > encrypted message
# Output: < string > decrypted message

def decipher_message(translation_guide, message):
    new_message = ""
    for i in range(0,len(message)):
        if message[i] in translation_guide:
            new_message += translation_guide[message[i]]
        else:
            new_message += message[i]
    return(new_message)


# Uncomment code below to test (DO NOT paste into Coursemology!)
print("*** QUESTION 3 ***")
my_translation_guide = read_translation_guide_into_dictionary('translation.csv')
my_encrypted_message = read_message('message.txt')
print(decipher_message(my_translation_guide, my_encrypted_message))


#==============================================================================#
#                                  Question 4                                  #
#==============================================================================#

# Input 1: < string > file path to encrypted map
# Input 2: < string > file path to translation guide csv
# Output: < None >
def decrypt_map(file_path_encrypted_map, file_path_translation_guide):
    #read translation guide in
    translation_guide = read_translation_guide_into_dictionary(file_path_translation_guide)
    
    #read encrypted map in
    with open(file_path_encrypted_map, "r") as f:
        my_map = []
        for line in f:
            my_map.append(line)
    my_map = np.array(my_map)
    
    #decrypt the map
    new_map = ""
    for i in range(0, len(my_map)):
        st = my_map[i]
        for j in range(0, len(st)):
            if st[j] == '':
                new_map += '\n'
            elif st[j] in translation_guide:
                new_map += translation_guide[st[j]]
            else:
                new_map += st[j]
    
    #write to a new .txt file
    with open("decrypted_map.txt", "w") as f:
        for line in new_map:
            f.write(line)




# Uncomment code below to test (DO NOT paste into Coursemology!)
print("*** QUESTION 4 ***")
decrypt_map('encrypted_map.txt', 'map_code.csv')
