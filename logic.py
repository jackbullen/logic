import os
import glob
import shutil
import getpass
import datetime

user = getpass.getuser()
root = os.path.join("/Users", user, "Music/Logic")

def input_project(prompt="Project number: "):
	project_number = input(prompt)
	return 'Project ' + str(project_number) + '.logicx'

def create_checkpoint(project_name):
	'''
	Create a checkpoint (copy) of a .logicx directory
	'''
	# Check the project exists
	project_dir = os.path.join(root, project_name)
	if not os.path.exists(project_dir):
		print(f"Project {project_name} was not found.\n")


	# Get the projects checkpoint folder
	project_checkpoints_dir = os.path.join(root, 
		f"Checkpoints/{project_name.strip('.logicx')}")
	if not os.path.exists(project_checkpoints_dir):
		os.makedirs(project_checkpoints_dir)

	# Create the checkpoint
	timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
	checkpoint_dir = os.path.join(project_checkpoints_dir, f"{timestamp}.logicx")
	shutil.copytree(project_dir, checkpoint_dir)
	print(f"Checkpoint created at {checkpoint_dir}\n")

def list_checkpoints(project_name):
	'''
	List the contents of a projects checkpoint folder
	'''
	# Check the project exists
	project_dir = os.path.join(root, project_name)
	if not os.path.exists(project_dir):
		print(f"Project {project_name} was not found.\n")
		return

	checkpoint_dir = os.path.join(root, f"Checkpoints/{project_name.strip('.logicx')}")
	if not os.path.exists(checkpoint_dir):
		print("No checkpoints available.\n")
		return

	print("Available checkpoints:")
	for dir in os.listdir(os.path.join(checkpoint_dir)):
		print(dir)

def list_projects(num=5, size=False, recent=True):
	'''
	List the users projects in /Users/Music/Logic
	'''
	projects = map(lambda x: os.path.join(root, x), os.listdir(root))
	projects = filter(lambda x: x.endswith('.logicx'), projects)
	if recent:
		projects = list(reversed(sorted(projects, key=os.path.getmtime)))
	
	for project in projects[:num]:
		print(project.split('/')[-1])
	print()


if __name__ == "__main__":
	while True:
		print("1. Create Checkpoint")
		print("2. List Checkpoints")
		print("3. Open Checkpoint")
		choice = input("Enter a command: ")

		if choice == "1":# Create checkpoint
			create_checkpoint(input_project())

		elif choice == "2":# List checkpoints
			list_projects()
			list_checkpoints(input_project())

		elif choice == "3":# Open checkpoint
			project = input_project()
			os.system(f"open {os.path.join(root, project)}")

		elif choice == "4":# Exit
			exit(0)
		else:
			print("Invalid choice...")
