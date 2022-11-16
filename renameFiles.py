# script to rename multiple files
import os

def main():

	inputFolder = '/home/gratt/repos/leetcode/neetcodeAll/'
	outputFolder = '/home/gratt/repos/leetcode/neetcode/'

	# loop thru each file
	for cat in os.listdir(inputFolder):
		old_folder = inputFolder + cat
		for file in os.listdir(old_folder):
			old_path = old_folder + '/' + file
			new_path = outputFolder + cat + '/' + file
			os.rename(old_path, new_path)
		
if __name__ == '__main__':
	main()



