import os

root_folder = "E:/1Shruti/HaarCascadePython"
preord_fs_list = []
def walk_fs( path_name_of_cur_folder  ) :
  dir_contents = os.listdir( path_name_of_cur_folder ) 
  dirs_inside = []
  files_inside = []
  for item in dir_contents :
    path_name_of_item = os.path.join( path_name_of_cur_folder, item )
    if ( os.path.isdir( path_name_of_item ) ) :
      dirs_inside.append( item )
    elif ( os.path.isfile( path_name_of_item ) ) :
      files_inside.append( item )
    #end if 
  #end for
  preord_fs_list.append( ( path_name_of_cur_folder , dirs_inside, files_inside ) )
  for item in dir_contents :
    path_name_of_item = os.path.join( path_name_of_cur_folder, item )
    if ( os.path.isdir( path_name_of_item ) ) :
      walk_fs( path_name_of_item )
    #end if 
  #end for

"""
The hierarchy inside the sample test folder
/tmp/shrt/
/tmp/shrt/f_xyz
/tmp/shrt/d_456
/tmp/shrt/d_456/f_555
/tmp/shrt/f_abc
/tmp/shrt/d_123
/tmp/shrt/d_123/f_111
/tmp/shrt/d_123/d_222
"""

walk_fs( root_folder )

#print (preord_fs_list)
for item in preord_fs_list :
  print (item)

"""
This is how the walk_fs would print it
('/tmp/shrt', ['d_456', 'd_123'], ['f_xyz', 'f_abc'])
('/tmp/shrt/d_456', [], ['f_555'])
('/tmp/shrt/d_123', ['d_222'], ['f_111'])
('/tmp/shrt/d_123/d_222', [], [])
"""
