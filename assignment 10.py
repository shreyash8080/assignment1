#!/usr/bin/env python
# coding: utf-8
Number 1 -

Question -
How do you distinguish between shutil.copy() and shutil.copytree()?

Answer -
"shutil.copy()" will copy a single file."shutil.copytree()" will copy an entire folder and every folder and file contained in it.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
What function is used to rename files?

Answer -
shutil.move will rename files.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 3 -

Question -
What is the difference between the delete functions in the send2trash and shutil modules?

Answer -
shutil.rmtree() function irreversibly deletes files and folders. send2trash will send folders and files to computer's trash or recycle bin instead of permanently deleting them

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 4 -

Question -
ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

Answer -
ZipFile method is equivalant to File objects' open() method. For example,
# In[1]:


import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')

Number 5 -

Question -
Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

Answer -
# In[2]:


import os, shutil

def selectiveCopy(folder, extensions, destFolder):
    folder = os.path.abspath(folder)
    destFolder = os.path.abspath(destFolder)
    print('Looking in', folder, 'for files with extensions of', ', '.join(extensions))
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
                fileAbsPath = foldername + os.path.sep + filename
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.php', '.py']
folder = 'randomFolder'
destFolder = 'selectiveFolder'
selectiveCopy(folder, extensions, destFolder)


# In[ ]:




