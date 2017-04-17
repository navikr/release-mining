import os
class RAUtilities:
    def FileHandle(self, directory, filename, overwrite):
        os.chdir(directory)
        if (os.path.exists(filename)==True and overwrite==False):
            fp= open(filename,'ab')
        else:
            fp= open(filename, 'wb')
        return fp
    def sortFileIndex(self,fNameA,fNameB):
        s1=s2=[]
        s1=fNameA.rsplit('.')
        s2=fNameB.rsplit('.')
        if len(s1) == len(s2)==3:
            if(int(s1[2])<int(s2[2])):
                return -1
            elif (int(s1[2])>int(s2[2])):
                return 1
