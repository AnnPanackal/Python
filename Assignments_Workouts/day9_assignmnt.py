"""File Functions"""
#---------------------------------file.close()--------------------------
with open("C:/Users/ann/Desktop/Python_Acc/File_Fn","w") as rObj:
    rObj.write("Testing file for fileObj.close()\n")
    rObj.writelines(['Hello!','Nice to know you.'])
    rObj.close()
    #rObj.write("Hi") -> Throws an error
    
with open("C:\\Users\\ann\\Desktop\\Python_Acc\\File_Fn","r") as r_obj:
    print(r_obj.read())
#-----------------------------file.fileno()------------------------------
    print(r_obj.fileno())
#Integer used for i/o operations
#------------------file.seek(),file.seekable()---------------------------
    out = r_obj.read()
    print(out)
    print(r_obj.seekable())
    r_obj.seek(10)
    print(r_obj.read())
#---------------------------------file.tell()-----------------------------
    print(r_obj.tell())
    """The tell() method returns the current file position in a file stream.
        You can change the current file position with the seek() method."""
#--------------------------------file.truncate(size)-----------------------
with open("C:\\Users\\ann\\Desktop\\Python_Acc\\File_Fn","w") as wobj:
    wobj.truncate(10)
    wobj.close()
with open("C:\\Users\\ann\\Desktop\\Python_Acc\\File_Fn","r") as robj:
    print(robj.read())
    