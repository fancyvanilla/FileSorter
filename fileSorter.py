#! /usr/bin/python3
import json
import os
import shutil
import argparse
from PIL import Image
import magic


art="""
  _______  __    ___       _______   ________   ______     _______  ___________  _______   _______      
 /"     "||" \  |"  |     /"     "| /"       ) /    " \   /"      \("     _   ")/"     "| /"      \     
(: ______)||  | ||  |    (: ______)(:   \___/ // ____  \ |:        |)__/  \\__/(: ______)|:        |    
 \/    |  |:  | |:  |     \/    |   \___  \  /  /    ) :)|_____/   )   \\_ /    \/    |  |_____/   )    
 // ___)  |.  |  \  |___  // ___)_   __/  \\(: (____/ //  //      /    |.  |    // ___)_  //      /     
(:  (     /\  |\( \_|:  \(:      "| /" \   :)\        /  |:  __   \    \:  |   (:      "||:  __   \     
 \__/    (__\_|_)\_______)\_______)(_______/  \"_____/   |__|  \___)    \__|    \_______)|__|  \___)    
                                                                                                        
"""
def is_image(file_path):
    try:
        Image.open(file_path).close()
        return True
    except (OSError, IOError):
        return False

def createDestinationFolders(source_dir):
    with open("config.json","r") as f:
        destinationFolders=json.load(f)
        return destinationFolders
                         
def organizeFiles(source_dir):
    destinationFolders=createDestinationFolders(source_dir)
    for filePath in os.scandir(source_dir):
        if filePath.is_file():
            ext = os.path.splitext(filePath.name)[1][1:].lower()
            if ext in destinationFolders["ignore"]:
                break
            destinationFolder=None
            for folder,extentions in destinationFolders["folders"].items():
                if ext in extentions:
                    destinationFolder=folder
                    break
            if destinationFolder==None:
                destinationFolder="Others"
            destPath=os.path.join(source_dir,destinationFolder)
            if not (os.path.exists(destPath)):
              os.makedirs(destPath)
            shutil.move(filePath.path,destPath)
 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", help="Path to the source directory")
    args = parser.parse_args()
    source_dir = args.source_dir    
    if not os.path.isdir(source_dir):
        print("Invalid destination directory!")
        exit()
    print(art)
    print("Organizing files...")
    organizeFiles(source_dir)
    print(f'Done! You can check now your organized files in {source_dir}.')


if __name__ == '__main__':
    main()

