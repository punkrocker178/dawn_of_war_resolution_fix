import os
import shutil
import binascii

isdir = os.path.isdir(".\W40KFilesBackup") 
def checkIfFileExists(Filename):
    #checks if file exists in current directory this python script is located at
    tf=os.path.exists(Filename)
    return tf

def mkDir(pathName):
    os.mkdir(pathName)
def mkCopy(filename):
    print("Making a backup of", filename)

def Backup_and_rename_original_file(filename, folder):
	currentDir=str(os.getcwd())
	fileTolook="\\"+filename
	finalPath=currentDir+fileTolook
	print(finalPath)
	if os.path.isfile(finalPath)==True:
		src_file=os.path.join(os.curdir,filename)
		dst_file=os.path.join(os.curdir,".\{0}\{1}".format(folder,filename))
		print("final path: {0}".format(finalPath))
		print("source file: {0}".format(src_file))
		print("destiny file: {0}".format(dst_file))
		if os.path.exists(dst_file)!=True:
			shutil.copy2(src_file, dst_file)
		else:
			print("Error: Couldn't create a backup! It looks like a backup file named {0} in the directory {1} already exists".format(filename,folder))
	else:
		print("Error: Couldn't find {0} in the current directory. Please, before running this script make sure to put it inside your Warhammer 40k: Dawn Of War root folder and then try again".format(filename))
		exit()
def logHex_data_of_executable(filename):
	# Open in binary mode (so you don't read two byte line endings on Windows as one byte)
	# and use with statement (always do this to avoid leaked file descriptors, unflushed files)
	with open(filename, 'rb') as f:
	    # Slurp the whole file and efficiently convert it to hex all at once
	    hexdata = binascii.hexlify(f.read())
	    #print(hexdata)
	    text_file = open(filename, "wb")
	    text_file.write(hexdata)
	    text_file.close()


def edit_hex(currentHexString, replcementHexString,filename):# changes the resolution options avaliable in the binary executable file of the game
	    #replaces hex string to new hex string, thus allowing bigger resolutions in the game
	    #logHex_data_of_executable("original_hexdata.txt")# Logs an hex data of the file before the changes
	    oldhexstring=currentHexString
	    newhexstring=replcementHexString
	    replace_hex_chunk(oldhexstring, newhexstring,filename)
	    #logHex_data_of_executable("modified_hexdata.txt")# Logs an hex data of the file after the changes

def replace_hex_chunk(oldhexstring, newhexstring,filename):
	oldbinstring=binascii.unhexlify(oldhexstring)
	newbinstring=binascii.unhexlify(newhexstring)
	f = open(filename,'rb')
	contents = f.read().replace(oldbinstring, newbinstring)
	f.close()
	f = open(filename,'wb')
	f.write(contents)
	f.close()

def checkIfBackupDirExists():
#Checks if Backup dir of files already exists if not, create W40KFilesBackup folder
	tf=False
	if isdir==False:
		print("Backup folder doesn't exist yet. Creating one...")
		mkDir(".\W40KFilesBackup")
		print("Successfully created .\W40KFilesBackup")
	else:
		print("Backup folder already exists")
		tf=True
	return tf

def SelectAspectRatio():
	userSelection=99
	newAspectRatio="ABAAAA3F"
	options = [0,1,2,3,4,5,6,7,8,9,10,11]

	while int(userSelection) not in options:
		print("Pick the Aspect Ratio in which you would like to play Warhammer 40k: Dawn Of War. \n Warhammer 40k: Dawn Of War's default aspect ration is 4:3")
		print("0 - 15:9")#5555D53F
		print("1 - 16:9")#398EE33F 
		print("2 - 16:10")#CCCCCD3F
		print("3 - 3x15:9")#0000A040
		print("4 - 3x16:9")#ABAAAA40
		print("5 - 3x16:10")#9A999940
		print("6 - 21:9 (2560x1080)")#26B41740
		print("7 - 21:9 (3440x1440)")#8EE31840
		print("8 - 21:9 (3840x1600)")#9A991940
		print("9 - 32:9")#398E6340
		print("10 - 32:10")#CCCCCD3F
		print("11 - Dont change Aspect Ratio")#CCCCCD3F
		userSelection=input()
		if userSelection.isnumeric()==True:
			if int(userSelection) in options:
				print("You picked option", userSelection)
				numberPicked= int(userSelection)
				if numberPicked==0:
					print("Aspect Ratio 15:9 selected")
					newAspectRatio="5555D53F"
					break
				elif numberPicked==1:
					print("Aspect Ratio 16:9 selected")
					newAspectRatio="398EE33F"
					break
				elif numberPicked==2:
					print("Aspect Ratio 16:10 selected")
					newAspectRatio="CCCCCD3F"
					break
				elif numberPicked==3:
					print("Aspect Ratio 3x15:9 selected")
					newAspectRatio="0000A040"
					break
				elif numberPicked==4:
					print("Aspect Ratio 3x16:9 selected")
					newAspectRatio="ABAAAA40"
					break
				elif numberPicked==5:
					print("Aspect Ratio 3x16:10 selected")
					newAspectRatio="9A999940"
					break
				elif numberPicked==6:
					print("Aspect Ratio 21:9 (2560x1080) selected")
					newAspectRatio="26B41740"
					break
				elif numberPicked==7:
					print("Aspect Ratio 21:9 (3440x1440) selected")
					newAspectRatio="8EE31840"
					break
				elif numberPicked==8:
					print("Aspect Ratio 21:9 (3840x1600) selected")
					newAspectRatio="9A991940"
					break
				elif numberPicked==9:
					print("Aspect Ratio 32:9 selected")
					newAspectRatio="398E6340"
					break
				elif numberPicked==10:
					print("Aspect Ratio 32:10 selected")
					newAspectRatio="CCCCCD3F"
					break
				elif numberPicked==11:
					print("You opted to not change the aspect ratio of the game")
					newAspectRatio="No"
					break
			else:
				print("Error: option", userSelection,"is not avaliable. Please pick one of the avaliable options")
		else:
			print("Error: the option you typed ", userSelection,"is not a number! Please type the number of one of the avaliable options")
			userSelection=99 #we add a default numeric value that doesnt exist in the avaliable options to avoid a catch because the user typed a value thats not a number
	return newAspectRatio

def SelectResolution():
	newWidthRes="screenwidth=800"
	newHeightRes="screenwidth=600"
	userSelection=99
	options = [0,1,2,3,4,5,6,7,8]

	while int(userSelection) not in options:
		print("Pick the resolution in which you would like to play Warhammer 40k: Dawn Of War. \n Warhammer 40k: Dawn Of War's default resolution is 800x600")
		print("0 - 800x600")#5555D53F
		print("1 - 1280x720")#398EE33F 
		print("2 - 1920x1080")#CCCCCD3F
		print("3 - 1920x1200")#CCCCCD3F
		print("4 - 2560x1440")#0000A040
		print("5 - 3440x1440")#ABAAAA40
		print("6 - 3840 x 2160")#9A999940
		print("7 - 7680 x 4320")#26B41740
		print("8 - Don't change the game resolution")#26B41740
		userSelection=input()
		if userSelection.isnumeric()==True:
			if int(userSelection) in options:
				print("You picked option", userSelection)
				numberPicked= int(userSelection)
				if numberPicked==0:
					if IsResolutionAlreadyBeingUsed("Local.ini","screenwidth=800","screenheight=600")==False:
						print("800x600 was selected")
						newWidthRes="screenwidth=800"
						newHeightRes="screenheight=600"
						break
					else:
						userSelection=99 #makes while not break
				elif numberPicked==1:
					if IsResolutionAlreadyBeingUsed("Local.ini","screenwidth=1280","screenheight=720")==False:
						print("1280x720 was selected")
						newWidthRes="screenwidth=1280"
						newHeightRes="screenheight=720"
						break
					else:
						userSelection=99 #makes while not break
				elif numberPicked==2:
					if IsResolutionAlreadyBeingUsed("Local.ini","screenwidth=1920","screenheight=1080")==False:
						print("1920x1080 was selected")
						newWidthRes="screenwidth=1920"
						newHeightRes="screenheight=1080"
						break
					else:
						userSelection=99 #makes while not break
				elif numberPicked==3:
					if IsResolutionAlreadyBeingUsed("Local.ini","screenwidth=1920","screenheight=1200")==False:
						print("1920x1200 was selected")
						newWidthRes="screenwidth=1920"
						newHeightRes="screenheight=1200"
						break
					else:
						userSelection=99 #makes while not break
				elif numberPicked==4: 
					if IsResolutionAlreadyBeingUsed("Local.ini","screenwidth=2560","screenheight=1440")==False:
						print("2560x1440 was selected")
						newWidthRes="screenwidth=2560"
						newHeightRes="screenheight=1440"
						break
					else:
						userSelection=99 #makes while not break
				elif numberPicked==5:
					if IsResolutionAlreadyBeingUsed("Local.ini","screenwidth=3440","screenheight=1440")==False:
						print("3440x1440 was selected")
						newWidthRes="screenwidth=3440"
						newHeightRes="screenheight=1440"
						break
					else:
						userSelection=99 #makes while not break
				elif numberPicked==6: 
					if IsResolutionAlreadyBeingUsed("Local.ini","screenwidth=3840","screenheight=2160")==False:
						print("3840x2160 was selected")
						newWidthRes="screenwidth=3840"
						newHeightRes="screenheight=2160"
						break
					else:
						userSelection=99 #makes while not break
				elif numberPicked==7: 
					if IsResolutionAlreadyBeingUsed("Local.ini","screenwidth=7680","screenheight=4320")==False:
						print("7680x4320 was selected")
						newWidthRes="screenwidth=7680"
						newHeightRes="screenheight=4320"
						break
					else:
						userSelection=99 #makes while not break
				elif numberPicked==8: 
					print("You opted to not change the resolution")
					break
			else:
				print("Error: option", userSelection,"is not avaliable. Please pick one of the avaliable options")
		else:
			print("Error: the option you typed ", userSelection,"is not a number! Please type the number of one of the avaliable options")
			userSelection=99  #we add a default numeric value that doesnt exist in the avaliable options to avoid a catch because the user typed a value thats not a number
	if userSelection != 8:# If user picked option to not change anything then dont change anything	
		ChangeResolution(newWidthRes,newHeightRes)

def ChangeResolution(newWidthRes,newHeightRes):
	removeLineifStringIsFound("Local.ini","screenwidth")
	removeLineifStringIsFound("Local.ini","screenheight")
	removeLineifStringIsFound("Local.ini","\n")#truncateDocument
	writeAtTheEndOfFile("Local.ini",newWidthRes)
	writeAtTheEndOfFile("Local.ini","\n"+newHeightRes)

def removeLineifStringIsFound(filename,string):
	with open(filename,'r+') as f:
		data= ''.join([i for i in f if not i.lower().startswith(string)])
		f.seek(0)
		f.write(data)
		f.truncate()

def writeAtTheEndOfFile(filename, newLine):
	# Open a file with access mode 'a'
	file_object = open(filename, 'a')
	# Append 'hello' at the end of file
	file_object.write(newLine)
	# Close the file
	file_object.close()

def mainMenu():
	userSelection=99
	options = [0,1,2,3,4]
	while int(userSelection) not in options:
		print("\n Dawn of War Resolution Fix python Script Main Menu \n What would you like to do?\n 0: Change Aspect Ratio of The Game  \n 1: Change Resolution of the game \n 2: Change Aspect Ratio and Resolution of The Game \n 3: Restore original files \n 4: Exit Script")
		userSelection=input()
		if userSelection.isnumeric()==True:
			if int(userSelection) in options:
				print("You picked option", userSelection)
				numberPicked= int(userSelection)
				if numberPicked==0:
					print("Change Aspect Ratio of The Game selected \n")
					ChangeAspectRatio()
					userSelection=99
				elif numberPicked==1:
					print("Change Resolution of the game selected \n")
					SelectResolution()
					userSelection=99
				elif numberPicked==2:
					print("Change Aspect Ratio and Resolution of The Game")
					ChangeAspectRatioAndResolution()
					userSelection=99
				elif numberPicked==3:
					print("Restore original files selected")
					restoreAllOriginalFilesW40K()
					userSelection=99
				elif numberPicked==4:
					print("Exit selected")
					print("Thanks for using this script! \n Until next time!")
					break
			else:
				print("Error: option", userSelection,"is not avaliable. Please pick one of the avaliable options")
		else:
			print("Error: the option you typed ", userSelection,"is not a number! Please type the number of one of the avaliable options")
			userSelection=99 #we add a default numeric value that doesnt exist in the avaliable options to avoid a catch because the user typed a value thats not a number
def IsExecutablePatched(filename,originalHexString):
	#check if executable had its aspect ratio values already edited by this script or another one
	tf=False
	originalBinaryString=binascii.unhexlify(originalHexString)#converts hexstring to binary string
	print("Checking if Dawn of War executable is already patched...")
	with open(filename,"rb") as file:
		contents = file.read()
		searchString = originalBinaryString
		if searchString in contents:
			print("{0} executable aspect ratio  is not patched yet".format(filename))
			tf=False
		else:
			print("{0} executable aspect ratio  has been patched already".format(filename))
			tf=True
	return tf

def IsResolutionAlreadyBeingUsed(filename, currentResolutionWidth, currentResolutionHeight):
	#check if executable had its aspect ratio values already edited by this script or another one
	tf=False
	print("Checking if Dawn of War's {0} is already using this resolution...".format(filename))
	with open(filename,"r") as file:
		contents = file.read()
		searchStringWidth = currentResolutionWidth
		searchStringHeight = currentResolutionHeight
		if searchStringWidth in contents and searchStringHeight in contents:
			print("Error: It looks like Dawn of War {0} is already using {1} by {2} resolution".format(filename,currentResolutionWidth, currentResolutionHeight))
			print("Please select another resolution or pick the option to not change any resolution at all")
			tf=True
		else:
			tf=False
	return tf

def promptToRestoreFiles():#Prompt asking if the user would like to restore the original files of the game
	userSelection=99
	options = [0,1]
	while int(userSelection) not in options:
		print("It appears that your Warhammer 40K executable and dlls have already been modified before to play in a different aspect ratio.\n In order to change the aspect ratio of Warhammer 40k: Dawn Of War again \n We need to restore them before allowing you to modify it again. \n 0 - No) \n 1 - Yes")
		userSelection=input()
		if userSelection.isnumeric()==True:
			if int(userSelection) in options:
				print("You picked option", userSelection)
				numberPicked= int(userSelection)
				if numberPicked==0:
					print("You picked No, so the files wont be restored, therefore, you wont be able to change the resolution.")
					break
				elif numberPicked==1:
					print("You picked Yes, so the files will be restored to the original ones before you can change the aspect ratio of the game again.")
					restoreAllOriginalFilesW40K()
			else:
				print("Error: option", userSelection,"is not avaliable. Please pick one of the avaliable options")
		else:
			print("Error: the option you typed ", userSelection,"is not a number! Please type the number of one of the avaliable options")
			userSelection=99  #we add a default numeric value that doesnt exist in the avaliable options to avoid a catch because the user typed a value thats not a number

def ChangeAspectRatio():
	if IsExecutablePatched("W40k.exe","ABAAAA3F")==True: #check if executable has already been patched
		promptToRestoreFiles()
	if IsExecutablePatched("W40k.exe","ABAAAA3F")==False: #Checks if the exetuable is already patched before trying to modify its aspect ratio again in order to avoid mistakes
		aspectRatioHexValue=SelectAspectRatio()
		if aspectRatioHexValue!="No":
			print("Changing aspect ratio to its new hex value:",aspectRatioHexValue)
			edit_hex("ABAAAA3F",aspectRatioHexValue,"W40k.exe")
			edit_hex("ABAAAA3F",aspectRatioHexValue,"Platform.dll")
			edit_hex("ABAAAA3F",aspectRatioHexValue,"spDx9.dll")
			edit_hex("ABAAAA3F",aspectRatioHexValue,"UserInterface.dll")
	else:
		print("Error: It appears that your Warhammer 40K executable and dlls have already been modified before to play in a different aspect ratio \n Please restore the original files before trying to change the aspect ratio again.")


def ChangeAspectRatioAndResolution():
	SelectResolution()
	ChangeAspectRatio()

def restoreAllOriginalFilesW40K():
	print("Restoring original files of the game..")
	restoreOriginalFile("W40KFilesBackup","","W40k.exe")
	restoreOriginalFile("W40KFilesBackup","","Platform.dll")
	restoreOriginalFile("W40KFilesBackup","","spDx9.dll")
	restoreOriginalFile("W40KFilesBackup","","UserInterface.dll")
	ChangeResolution("screenwidth=800","screenheight=600")
	print("Restoration of all files succesfully completed!")

def restoreOriginalFile(src,dst,filename):#Restores original files
	print("Restoring {2} in {0} to {1}...".format(src,dst,filename))
	shutil.copy(os.path.join(src, filename), os.path.join(dst, filename))
	print("Restoration of unmodified {0} was successfully completed!".format(filename))

def firstTimeRunningSteps():
	checkIfBackupDirExists()
	Backup_and_rename_original_file("Local.ini","W40KFilesBackup")
	Backup_and_rename_original_file("test.txt","W40KFilesBackup")
	Backup_and_rename_original_file("W40k.exe","W40KFilesBackup")
	Backup_and_rename_original_file("Platform.dll","W40KFilesBackup")
	Backup_and_rename_original_file("spDx9.dll","W40KFilesBackup")
	Backup_and_rename_original_file("UserInterface.dll","W40KFilesBackup")
	SelectResolution()
	ChangeAspectRatio()

def main():
	if checkIfFileExists("W40K.exe") ==True: 
		if checkIfBackupDirExists() ==False:
			firstTimeRunningSteps()
		else :
			mainMenu()
	else:
		input("Error: Couldnt detect a W40k.exe in this folder! \n\n It Appears that you have placed this script in the wrong directory. \n Please insert this in the root folder of your Dawn of War 1 installation \n and then try to run it again. \n Press any button to exit this script")
main()
