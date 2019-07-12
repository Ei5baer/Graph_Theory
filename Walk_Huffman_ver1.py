
import random

random.seed (10)

#inp_sym = []


Ht = [[7,4,2 ], [8, 0, 1], [9,7,5], [10,3,6],[11,8,9],[12,10,11]]

def findRoot(RT):
    S = set()
    for i in RT:
        for j in i:
            S.add( j )
    print (S)
    for i in RT :
        for j in i[1:]:
            S.remove( j )
    print (S)
    try :
        for i in S :
            retval = i
            break
        return retval
    except :
        print ("Not a tree")

#print ( findRoot (Rt))

def LocateNode(RT, nd):
    ret_tuple = None
    for i in RT:
        if ( i[0] == nd ):
            ret_tuple = i
            break
            #return i
    if (ret_tuple == None ):
        return False, ()
    else:
        return True, ret_tuple

def isLeaf (RT, nd):
    for i in RT:
        if ( i[0] == nd ):                                                       
            return False
        
    return True

    
    

preordered_list = []
"""
def walk_hc(RT, root, path):
    flag, rootTuple = LocateNode(RT, root)
    if (flag == False ):
        pass
    else:
        dirs = []
        files = []
        for ch in rootTuple[1:]:
            if (isLeaf (RT, ch) ):
                files.append(ch)
            else:
                dirs.append(ch)
            #endif
        #endfor
        preordered_list.append((path , dirs, files))
        for ch in rootTuple[1:]:
            walk_hc(RT, ch, path + [ch])
        #endfor
    #endif
"""    

            

HC = {}

idx_to_sym =['a', 'c', 'b', 'e', 'd', 'g' , 'f']
#hc_in_orig = { k : random.randint (1,100) for k in inp_syms }

#idx_to_sym = hc_in_orig.keys()

def walk_hc(HT, currnode, pathlabel):
    if (isLeaf (HT, currnode)):
        print( "currnode is ", currnode )
        print ( "idx is " , idx_to_sym[ currnode ] )
        HC[idx_to_sym[currnode]] = pathlabel
        return
        
    flag, rootTuple = LocateNode(HT, currnode)
    print ("currnode is " , currnode )
        
    preordered_list.append(pathlabel )
    print (rootTuple)
        
    walk_hc(HT, rootTuple[1], pathlabel + '0')
    walk_hc(HT, rootTuple[2], pathlabel + '1')

        
            
   
    

walk_hc (Ht, 12, '')
print (preordered_list)
