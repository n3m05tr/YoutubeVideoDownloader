import time
import colorama
from colorama import Fore, Back, Style
from pytube import YouTube
link = input(Fore.RED + Back.WHITE + "Paste the link here: ")
yt = YouTube(link)

try:
    ys = yt.streams.get_highest_resolution()
except:
    print(Fore.RED + "Connection Error")

print(Fore.BLUE + "\nTitle: ", yt._title)
print(Fore.BLUE + "Length: ", yt.length, "seconds")
print(Fore.BLUE + "Rating:", yt.rating)

def DownloadConfirmation():
    print(Fore.RED + Back.WHITE + "\nYou are sure about dowloading this video?")
    SureNot = input(Fore.RED + Back.WHITE + "Yes or No?: ")
    if (SureNot == "Yes" or "yes"):
        SureNot_Bool = True
    elif (SureNot == "No" or "no"):
        SureNot_Bool = False
    if SureNot_Bool == True:
        ys.download()
        print(Fore.BLUE + "\nDownloading...")
        print(Fore.BLUE + "Download Complete")
    elif SureNot_Bool == False:
        print(Fore.BLUE + "Ok then, bye!")
        time.sleep(3)

DownloadConfirmation()

time.sleep(4)
