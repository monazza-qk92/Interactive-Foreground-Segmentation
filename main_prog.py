# -*- coding: utf-8 -*-
"""main_prog.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kiFQdGZS1AoLp4xcV3SVyMx5NRtxvTcm

The command below mounts the drive contents to google colab's files section. I created a folder named Assignment_2_folder and all the content related to this assignment resides in this folder, it contains all the images files and this notebook.
"""

from google.colab import drive
drive.mount('/content/gdrive')

"""Below command shows the contents that have been mounted to the files section of this notebook. It's just for confirmation."""

! ls

"""This is a magic command, it changes our working directory. As I would be working in my Assignment_2_folder, so, I use this command before I start working."""

# Commented out IPython magic to ensure Python compatibility.
# %cd gdrive/My Drive/Assignment_2_folder

"""This is a bit tricky part. Actually, I created a Github repository for this assignment as I was having some issue in file handling and reading directly from Google Colab.So, I created git repo and cloned it here. But we do it only once, when our required folder is cloned or copied in the destination folder it stays there unless you delete it yourself.

"""

! git clone https://github.com/monazza-qk92/project_folder.git

"""The git repo that I cloned here named "project_folder" has a file called functions. So, I use the command below to import that file. Actually, this was the file which created issue and I had to go through this process."""

from project_folder.functions import *

from PIL import Image

strokeimgs = ['dance stroke 1.png','dance stroke 2.png','dog stroke.png',
              'lady stroke 1.png','lady stroke 2.png','Mona-lisa stroke 1.png',
              'Mona-lisa stroke 2.png','van Gogh stroke.png']
oimgs = ['dance.PNG','dance.PNG','dog.PNG','lady.PNG','lady.PNG',
         'Mona-lisa.PNG','Mona-lisa.PNG','van Gogh.PNG']

for ii in range(8):
     strokeimg = Image.open(strokeimgs[ii])
     oimg = Image.open(oimgs[ii])
     k = 64

     r_df, b_df,xs = r_b_pixels(strokeimg)
    #for red pixels i.e foreground
     rdf, rcentroids = kmeans(k, r_df)
     rwk = Wk(rcentroids,k, rdf,xs)
     rCkval = Ck(k,oimg,rcentroids)
     r_prob,oxs,oys = p_of_oimPixels(oimg,k,rCkval,rwk)

    #for blue pixels i.e background
     bdf, bcentroids = kmeans(k, b_df)
     bwk = Wk(bcentroids,k, bdf,xs)
     bCkval = Ck(k,oimg,bcentroids)
     b_prob,oxs,oys = p_of_oimPixels(oimg,k,bCkval,bwk)

    #assigning
     assign = fg_bg_assign(r_prob,b_prob)

     fgImg_copy = oimg.copy()
     bgImg_copy = oimg.copy()
     #show foreground image
     fg_oimg = show_fg(oxs,oys,fgImg_copy,assign)
     fg_oimg.show()
    #show background image
     bg_oimg = show_bg(oxs,oys,bgImg_copy,assign)
     bg_oimg.show()