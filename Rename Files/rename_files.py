import os

def rename_files():
    # (1) Get file names from the folder
    file_list=os.listdir(r"F:\GITHUB\Scripts For Daily Use\Rename Files\prank")
    #print file_list
    saved_path=os.getcwd()
    os.chdir(r"F:\GITHUB\Scripts For Daily Use\Rename Files\prank")
    
    # (2) For each file,rename file
    for filename in file_list:
        print("Old Name of file: "+filename+"\n")
        os.rename(filename,filename.translate(None,'0123456789'))
        print("New Name of file: "+filename)

    os.chdir(saved_path)
    
rename_files()
