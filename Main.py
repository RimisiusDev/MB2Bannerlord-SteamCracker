import PyBass.bass as b
import os
from os import _exit as exit
import os.path as p
import pathlib as zg
import shutil as mn
def Main():
    b.BASS_INIT(-1, 44100, 0, 0, 0)
    if(b.BASS_START() == True):
        if(zg.Path("TitForTat.mp3")):
            handle_v = b.BASS_StreamCreateFile(mem=0, filename=bytes("TitForTat.mp3", "utf-8"), offset=0, length=0, flags=0x4)
            b.BASS_ChannelPlay(handle_v, False)
            bannerlord_path = input("Please Write Bannerlord(ONLY STEAM VERSION) Folder: ")
            if(zg.Path("steam_api64.dll")):
                os.rename(str("{}".format(bannerlord_path + "\\steam_api64.dll")), str("{}".format(bannerlord_path + "\\steam_api64_orig.dll")))
                mn.copyfile("steam_api64.dll", "{}".format(bannerlord_path + "\\steam_api64.dll"))
                print("Successfully Cracked Mount and Blade 2: Bannerlord!!! Created by RikkoMatsumatoOfficial!!!")
                exit(330)
            else:
                print("Please Restore steam_api64.dll(MrGoldBerg Steam Emulator) in Recycle Bin!!!")
                exit(443)
        else:
            print("Not Founded TitForTat.mp3!!! Please Restore this File in Recycle Bin!!!")
            exit(32)
    else:
        print("Failed to Init BASS!!!")
        exit(243)

if __name__ == "__main__":
    Main()