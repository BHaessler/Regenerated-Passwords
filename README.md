# Regenerated-Passwords
A password Generator that asks the user for a number of passwords to create, difficulty they would like and the length of these passwords to be created. Then the program shows them their passwords, which are randomly generated. This output can be seen on the IDE and/or in a popup window.

## Running the Program
- Right now, running this program is as simple as downloading the Password-gen.py file and running it from the IDE or command line.

- _If running in the CLI (Command Line Interface) prompt follow these steps:_
  1. Ensure that pip3 is installed, then clone the entire repository and then enter the location where you cloned it (Details on how to do that can be found [Here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository "Github doc on how to clone"))
  2. In the root of the repo location, run the command `pip3 install -r requirements.txt` to ensure you have all the dependencies on the system you are using to run this program.
  3. After checking and updating the requirements, run the command `python3 Password-gen.py` to run the program. Follow the prompts from there. 
- _If running in an IDE follow these steps:_
  1. Download the zip of the repository and unzip it to a known location
  2. Open the IDE and navigate to where the files are unzipped. 
  3. Open the Password-gen.py file, and run it in the shell of the IDE

### Expected Outputs
The IDE output will look like the image below:

If the pop-up window is enabled the output will look like the image below: 

---
## NOTES
This was written in Visual Studio Code and does not have a fully fledged webpage GUI component yet. It does have a pop up window component.

## Upcoming additions
- A Django webframe that will give the user a GUI component to create these passwords and see them in a more user-friendly manner
- Also in the works is a component to give the user a file with these created passwords should they choose to do so
