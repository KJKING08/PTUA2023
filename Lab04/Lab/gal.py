'''
Author: Ziling Jiang
Functions: 
    Function 1. Read in "Lab04-1.gal" and return the data in a dict
    Function 2. 
'''

# Function 1: format gal into dictionary in format of {id: [neighbour ids]}
def gal_to_id_dict(filename):
    '''
    Function: format gal into dictionary in format of {id: [neighbour ids]}
    Input: directory of a gal file, string
    Output: dictionary, key = id, value = nl (neighbors list)
    '''

    # Read in the data line by line
    file = open(filename, "r")
    all_lines = file.readlines()

    # Initialize an dictionary
    gal_id_dict = {}

    # Generate dictionary according to the data structure of gal
    for i in range(1, int((len(all_lines)-1)/2)):
        gal_id_dict[i] = [int(s) for s in all_lines[2*i].split()]

    # # Print out 'Who is whose neighbour'
    # for i in range(1, len(gal_id_dict)+1):
    #     print('Spatial Object',i,'have these neighbours:',gal_id_dict[i])

    return gal_id_dict

# Function 2: generate second dictionary in format of {number of neighbours: [ids that have key neighbors]}
def gal_id_dict_to_neighbour_dict(gal_id_dict):
    '''
    Function: format gal_id_dict into dictionary in format of {number of neighbours: [ids that have key neighbors]}
    Input: dictionary, key = id, value = nl (neighbors list)
    Output: dictionary, key = nn (number of neighbours), value = idl (id list of SO that have nn neighbors)
    '''

    # Calculate nn (list of number of neighbours) and maxnn (the number of neighbors with the largest number of neighbors)
    nn = []
    for i in range(1, len(gal_id_dict)+1):
        nn.append(len(gal_id_dict[i]))
    maxnn = max(nn)

    # generate an empty dictionary with maxnn key-value pair where key range from 1 to maxnn+1
    gal_neighbour_dict = {}
    for i in range(1, maxnn+1):
        gal_neighbour_dict[i] = []

    # Group the points by there nn
    for i in range(1, len(gal_id_dict)+1):
        gal_neighbour_dict[len(gal_id_dict[i])].append(i)

    # # print out 'how many neighbours does each point have'
    # print('None of point have less than 1 neighbours')
    # for i in range(1, maxnn+1):
    #     if gal_neighbour_dict[i]==[]:
    #         print('None of point have',i,'neighbours')
    #     else:
    #         print('These point(s) have',i,'neighbours:',gal_neighbour_dict[i])
    # print('None of point have more than',maxnn,'neighbours')

    return gal_neighbour_dict

# Function 3: asymmetries test
def test_asymmetry(dictname):
    for i in range(1, len(dictname)+1):
        for j in range(1, len(dictname)+1):
            if (i in dictname[j]) and (j not in dictname[i]):
                print('An asymmetry occurs: ',i, 'is a neiboughr of',j,',but',j,'is not a neighbour of',i)
                return i,j
            # if (i in dictname[j]):
            #     print(i, 'is a neiboughr of',j,)
            # elif  (i not in dictname[j]):
            #     print(i,'is not a neighbour of',j)
            # elif i == j:
            #     pass
            # else:
            #     print(i, 'is a neiboughr of',j,',and',j,'is a neighbour of',i)

def main():
    # Read in Lab04-1.gal, store it into dict gal_id_dict and print it
    print('\n\n########################################Part 1:')
    print('\nGenerating the fitst dictionary...')
    dict1 = gal_to_id_dict("Lab04-1.gal")
    print('\nThis is the first dictionary where the key is the id of a spatial unit and the value is a list of the ids of its neighbors:')
    for item in dict1.items():
        print(item)

    # Calculate the number of neighbours and generate the second dictionary
    print('\n\n########################################Part 2:')
    print('\nGenerating the second dictionary...')
    dict2 = gal_id_dict_to_neighbour_dict(dict1)
    print('\nThis is the second dictionary where the key is the number of neighbors and the value is the list of ids that have key neighbors:')
    print('(in shape of a histogram)')
    for item in dict2.items():
        print(item)

    # Asymmetry test
    print('\n\n########################################Part 3:')
    print('\nSearching for asymmetry...')
    asy = test_asymmetry(dict1)
    print('\nIds of Asymmetry:',asy,'\n')





if __name__ == '__main__':
    main()

