# script to rename multiple files
import os

def main():

	folder = "/Users/patrickburke/Library/CloudStorage/OneDrive-EmoryUniversity/ECON496RW/processedCSVs/big/factpcrvital_chunks/"

	# loop thru each file
	for file_name in os.listdir(folder):
		old_path = folder + file_name
		new_path = folder + file_name.replace("factpcrvital_chunks","")
		os.rename(old_path, new_path)
		
if __name__ == '__main__':
	main()



