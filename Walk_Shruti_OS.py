Rt = [[1,2,3 ], [2, 4, 5], [3,6,7], [4,8,9],[5,10,11],[6,12,13],[7,14,15]]

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

print ( findRoot (Rt))

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

def walk(RT, root, path):
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
            walk(RT, ch, path + [ch])
        #endfor
    #endif
    

            
walk (Rt, 1, [1])
print (preordered_list)
