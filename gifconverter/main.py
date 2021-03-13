import imageio
import os
import sys
import time
import shutil
import click
from click._compat import raw_input
import timeit
import datetime
from moviepy.editor import *
from os import startfile
user_input= raw_input("Enter path name: ")
user_input1 = raw_input("Enter file name: ")

path_name = os.path.abspath(user_input)

def clipMerger():
    name2 = raw_input("Enter second clip name(File has to be in same folder as other one): ")
    clip1 = VideoFileClip(user_input1)
    clip2 = VideoFileClip(name2)
    clip_name = os.path.splitext(user_input1)[0]
    clip_name1 = os.path.splitext(name2)[0]
    final = concatenate_videoclips([clip1, clip2])
    final.write_videofile('merged.mp4', threads=4, fps=24, codec='libx264', preset='ultrafast')
    Current_Date = datetime.datetime.today().strftime("%H.%M.%S")
    os.rename('merged.mp4', 'merged_' + str(clip_name) + '_' + str(clip_name1) + '_' + str(Current_Date) + '.mp4')
    def cls():
        print("\n" * 100)
    cls()
    print("Clip was created, you can find it at: " + path_name + " with file name: " + 'merged_' + str(clip_name) + '_' + str(clip_name1) + '_' + str(Current_Date))
    user_input6 = raw_input("Do you want to open that file?: ")
    if user_input6 == 'yes':
        startfile('merged_' + str(clip_name) + '_' + str(clip_name1) + '_' + str(Current_Date) + '.mp4')
    else:
        exit()


def textadder():
    name = os.path.splitext(user_input1)[0]
    clip = VideoFileClip(user_input1)
    desiredText = raw_input("What text you want to add?: ")
    txt = TextClip(desiredText, font='Courier', fontsize=120, color='white')
    txt = txt.set_pos('center').set_duration(5)

    Current_Date = datetime.datetime.today().strftime("%H.%M.%S")
    video = CompositeVideoClip([clip, txt])
    video.write_videofile('converted.mp4', threads=4, fps=24, codec='libx264', preset='ultrafast')
    os.rename('converted.mp4', 'new_' + str(name) + '_' + str(Current_Date) + '.mp4')
    def cls():
        print("\n" * 100)
    cls()
    print("Clip was created, you can find it at: " + path_name + " with file name: " + 'new_' + str(name))
    user_input6 = raw_input("Do you want to open that file?: ")
    if user_input6 == 'yes':
        startfile('new_' + str(name) + '_' + str(Current_Date) + '.mp4')
    else:
        exit()

def converter(): # converting function
    clip = VideoFileClip(user_input1)
    user_input2 = raw_input("How long the video should be?: ")
    clip = clip.subclip(0 , user_input2)

    name = os.path.splitext(user_input1)[0] # getting name of file without extension
    user_input4 = raw_input("Should I optimize clip?: ")
    if user_input4 == 'yes':
        start = timeit.default_timer()
        clip.write_videofile('converted.mp4', preset='ultrafast', codec='libx264') # creating new video file with following settings
        stop = timeit.default_timer()
        print('This took time: ', stop - start, ' seconds')
        Current_Date = datetime.datetime.today().strftime("%H.%M.%S")
        os.rename('converted.mp4', 'new_' + str(name) + '_' + str(Current_Date) + '.mp4') # renaming file to its original name
        def cls(): print ("\n" * 100)
        cls()
        print("Clip was created, you can find it at: " + path_name + " with file name: " + 'new_' + str(name))
        user_input6 = raw_input("Do you want to open that file?: ")
        if user_input6 == 'yes':
            startfile('new_' + str(name) + '_' + str(Current_Date) + '.mp4')
        else:
            exit()
    else:
        user_input5 = raw_input("Should I use 30 or 60fps mode?[60fps mode is faster]: ")
        if user_input5 == "30":
            clip.write_gif('converted.gif', fps=30, program='ffmpeg')
            Current_Date = datetime.datetime.today().strftime("%H.%M.%S")
            os.rename('converted.gif', 'new_' + str(name) + '_' + str(Current_Date) + '.gif')
            def cls(): print ("\n" * 100)
            cls()
            print("Clip was created, you can find it at: " + path_name + " with file name: " + 'new_' + str(name))
            user_input6 = raw_input("Do you want to open that file?: ")
            if user_input6 == 'yes':
                startfile('new_' + str(name) + '_' + str(Current_Date) + '.gif')
            else:
                exit()
        else:
            clip.write_gif('converted.gif', fps=60, program='ffmpeg')
            Current_Date = datetime.datetime.today().strftime("%H.%M.%S")
            os.rename('converted.gif', 'new_' + str(name) + '_' + str(Current_Date) + '.gif')
            def cls():print("\n" * 100)
            cls()
            print("Clip was created, you can find it at: " + path_name + " with file name: " + 'new_' + str(name))
            user_input6 = raw_input("Do you want to open that file?: ")
            if user_input6 == 'yes':
                startfile('new_' + str(name) + '_' + str(Current_Date) + '.gif')
            else:
                exit()





action = raw_input("What do you want to do? \n"
                   "1: Add text to a clip \n"
                   "2: Edit clip Answer \n"
                   "3: Merge two clips \n"
                   "Answer: ")
if path_name == 'C:\\Users\\rt\\PycharmProjects\\gifconverter':
    if action == "1":
        textadder()
    if action == "2":
        converter()
    else:
        clipMerger()
else:
    print("File is not in working directory! Do you want to move file?")
    user_input2 = raw_input()
    if user_input2 == 'yes':
        path = path_name + '/' + user_input1
        moveto = 'C:/Users/rt/PycharmProjects/gifconverter'
        src = path
        dst = moveto
        shutil.move(src, dst)
        print("File was moved, do you want to continue?")
        user_input3 = raw_input()
        if user_input2 == 'yes':
            converter()
    else:
        exit()



