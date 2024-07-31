import time

# Scirpt to organize the donwloads and desktop path in real time

########################################################################################################################
def Organize_Downloads():
    print("dowloads")
    # .txt, .pdf, .docx, .exe, .html, .jpg, .jpeg, .png, .ppt, .zip
    # open path to dowloads folder / it can be anywhere so we should look for it first
    # parse extensions of each file
    # if extension folder doesnt exist create it and place it in documents folder
    # else directly place file in the associated folder in the documents


########################################################################################################################
def Organize_Desktop():
    print("desktop")


########################################################################################################################


if __name__ == '__main__':
    while True:
        Organize_Downloads()
        Organize_Desktop()
        time.sleep(600)  # Wait 600s (10 min) before re-entering the cycle