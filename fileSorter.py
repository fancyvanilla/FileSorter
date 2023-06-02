#! /usr/bin/python3
import os
import shutil
import argparse


art="""
  _______  __    ___       _______   ________   ______     _______  ___________  _______   _______      
 /"     "||" \  |"  |     /"     "| /"       ) /    " \   /"      \("     _   ")/"     "| /"      \     
(: ______)||  | ||  |    (: ______)(:   \___/ // ____  \ |:        |)__/  \\__/(: ______)|:        |    
 \/    |  |:  | |:  |     \/    |   \___  \  /  /    ) :)|_____/   )   \\_ /    \/    |  |_____/   )    
 // ___)  |.  |  \  |___  // ___)_   __/  \\(: (____/ //  //      /    |.  |    // ___)_  //      /     
(:  (     /\  |\( \_|:  \(:      "| /" \   :)\        /  |:  __   \    \:  |   (:      "||:  __   \     
 \__/    (__\_|_)\_______)\_______)(_______/  \"_____/   |__|  \___)    \__|    \_______)|__|  \___)    
                                                                                                        
"""

def createDestinationFolders(source_dir):
    with open("config.json","r") as f:
        destinationFolders=json.load(f)
        for folder in destinationFolders["folders"]:
          folder_path=os.path.join(source_dir,folder)
        if not (os.path.exists(folder_path)):
            os.makedirs(folder_path)
        return destinationFolders
                         

def organizeFiles(source_dir):
    destinationFolders=createDestinationFolders(source_dir)
    for filePath in os.scandir(source_dir):
        if filePath.is_file():
            ext = os.path.splitext(filePath.name)[1][1:].lower()
            destinationFolder=None
            for folder,extentions in destinationFolders.items():
                if ext in extentions:
                    destinationFolder=folder
                    break
            if destinationFolder==None:
                destinationFolder="Others"
            destPath=os.path.join(source_dir,destinationFolder)
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

