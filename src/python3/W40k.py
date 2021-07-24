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
	#copy_rename(os.curdir,"'SCU3.exe1")
	#shutil.copy2(os.curdir, "SCU3.exe1")
	#navigate_and_rename(os.curdir)
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
	if isdir==False:
		print("Backup folder doesn't exist yet. Creating one...")
		mkDir(".\W40KFilesBackup")
		print("Successfully created .\W40KFilesBackup")
	else:
		print("Backup folder already exists")

def SelectAspectRatio():
	userSelection=99
	newAspectRatio="ABAAAA3F"
	options = [0,1,2,3,4,6,7,8,9,10]

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
	options = [0,1,2,3,4,6,7]
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
		userSelection=input()
		if userSelection.isnumeric()==True:
			if int(userSelection) in options:
				print("You picked option", userSelection)
				numberPicked= int(userSelection)
				if numberPicked==0:
					print("800x600 was selected")
					newWidthRes="screenwidth=800"
					newHeightRes="screenheight=600"
					break
				elif numberPicked==1:
					print("1280x720 was selected")
					newWidthRes="screenwidth=1280"
					newHeightRes="screenheight=720"
					break
				elif numberPicked==2:
					print("1920x1080 was selected")
					newWidthRes="screenwidth=1920"
					newHeightRes="screenheight=1080"
					break
				elif numberPicked==3:
					print("1920x1200 was selected")
					newWidthRes="screenwidth=1920"
					newHeightRes="screenheight=1200"
					break
				elif numberPicked==4:
					print("2560x1440 was selected")
					newWidthRes="screenwidth=2560"
					newHeightRes="screenheight=1440"
					break
				elif numberPicked==5:
					print("3440x1440 was selected")
					newWidthRes="screenwidth=3440"
					newHeightRes="screenheight=1440"
					break
				elif numberPicked==6:
					print("3840x2160 was selected")
					newWidthRes="screenwidth=3840"
					newHeightRes="screenheight=2160"
					break
				elif numberPicked==7:
					print("7680x4320 was selected")
					newWidthRes="screenwidth=7680"
					newHeightRes="screenheight=4320"
					break
			else:
				print("Error: option", userSelection,"is not avaliable. Please pick one of the avaliable options")
		else:
			print("Error: the option you typed ", userSelection,"is not a number! Please type the number of one of the avaliable options")
			userSelection=99  #we add a default numeric value that doesnt exist in the avaliable options to avoid a catch because the user typed a value thats not a number

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


#Check if Backup dir of files already exists if not, create W40KFilesBackup folder
def main():
	print(checkIfFileExists("W40K.exe"))
	checkIfBackupDirExists()
    #print("The file ",".\W40KFilesBackup","exists",checkIfFileExists(".\W40KFilesBackup"))
	Backup_and_rename_original_file("Local.ini","W40KFilesBackup")
	Backup_and_rename_original_file("test.txt","W40KFilesBackup")
	Backup_and_rename_original_file("W40k.exe","W40KFilesBackup")
	Backup_and_rename_original_file("Platform.dll","W40KFilesBackup")
	Backup_and_rename_original_file("spDx9.dll","W40KFilesBackup")
	Backup_and_rename_original_file("UserInterface.dll","W40KFilesBackup")
	SelectResolution()
	aspectRatioHexValue=SelectAspectRatio()
	print("Changing aspect ratio to its new hex value:",aspectRatioHexValue)
	edit_hex("ABAAAA3F",aspectRatioHexValue,"W40k.exe")
	edit_hex("ABAAAA3F",aspectRatioHexValue,"Platform.dll")
	edit_hex("ABAAAA3F",aspectRatioHexValue,"spDx9.dll")
	edit_hex("ABAAAA3F",aspectRatioHexValue,"UserInterface.dll")
main()
