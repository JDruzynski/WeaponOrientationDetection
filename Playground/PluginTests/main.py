import loader
import netFactory as netFactory
from tkinter import filedialog
import json

def main() -> None:
    configPath, = filedialog.askopenfilenames()

    # read data from a JSON file
    with open(configPath) as file:
        data = json.load(file)

        # load the plugin
        loader.load_plugins(data["plugins"])

        # create the Network
        Net = netFactory.create(data["network"])

        # set up model with parameters
        Net.createModel(**data["parameters"])

        # do something with the network:





if __name__ == "__main__":
    main()
