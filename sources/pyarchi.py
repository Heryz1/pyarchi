from interactive_mode import InteractiveMode
from argconfig import ArgConfig


# pyArchi is a tool to design arrange components to make architecture
# User can create functions
# User can create class
# User can create object
# User can load a pyArchi file
if __name__ == "__main__":
    config = ArgConfig().get_config()

    if config.interactive == True:
        interactive_mode = InteractiveMode()
        interactive_mode.run()
    else:
        print("titi")
