from pdb_manipulation import *
from plotting_functions import *
from minecraft_functions import *
import PySimpleGUI as sg
from variables import *
import ast
import json

if __name__ == '__main__':
    # Check if the config file exists
    if not os.path.isfile("config.json"):
        # If it doesn't exist, create it
        config = {
            "scale": 1.0,
            "atoms": {
                "C": "black_concrete",
                "O": "red_concrete",
                "N": "blue_concrete",
                "S": "yellow_concrete",
                "backbone_atom": "gray_concrete",
                "sidechain_atom": "gray_concrete",
                "other_atom": "pink_concrete"
            },
            "mode": "Default",
            "backbone": True,
            "sidechain": True,
            "pdb_file": "",
            "save_path": ""
        }
        with open("config.json", "w") as f:
            json.dump(config, f)

    # Define the layout of the window
    layout = [
        [sg.Text("Select C atom"), sg.DropDown(decorative_blocks, key="C", default_value="black_concrete")],
        [sg.Text("Select O atom"), sg.DropDown(decorative_blocks, key="O", default_value="red_concrete")],
        [sg.Text("Select N atom"), sg.DropDown(decorative_blocks, key="N", default_value="blue_concrete")],
        [sg.Text("Select S atom"), sg.DropDown(decorative_blocks, key="S", default_value="yellow_concrete")],
        [sg.Text("Select backbone atom"),
         sg.DropDown(decorative_blocks, key="backbone_atom", default_value="gray_concrete")],
        [sg.Text("Select side chain atom"),
         sg.DropDown(decorative_blocks, key="sidechain_atom", default_value="gray_concrete")],
        [sg.Text("Select other atom"), sg.DropDown(decorative_blocks, key="other_atom", default_value="pink_concrete")],
        [sg.Text("Select mode"), sg.DropDown(["Default", "Skeleton"], key="mode", default_value="Default")],
        [sg.Checkbox("Backbone", default=True, key="backbone"), sg.Checkbox("Sidechain", default=True, key="sidechain")],
        [sg.Text("Scale"), sg.InputText(default_text="1.0", key="scale")],
        [sg.Button("Select PDB file"), sg.Button("Select Minecraft Save")],
        [sg.Button("Calculate", bind_return_key=True)]
    ]

    # Create the window
    window = sg.Window("My Window", layout)

    # Loop to keep the window open
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Select PDB file":
            pdb_file = sg.popup_get_file("Select PDB file")
            # Save the pdb_file path to config.json
            with open("config.json", "r+") as f:
                config = json.load(f)
                config["pdb_file"] = pdb_file
                f.seek(0)
                json.dump(config, f, indent=4)
                f.truncate()

        if event == "Select Minecraft Save":
            home_dir = os.path.expanduser("~")
            appdata_dir = os.path.join(home_dir, "AppData\Roaming\.minecraft\saves")

            save_path = sg.popup_get_folder("Select Minecraft 'datapacks' in your save", initial_folder=appdata_dir)

            directory_path = os.path.join(save_path, "mcPDB/data/protein/functions")
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)

            # Save the save_path to config.json
            with open("config.json", "r+") as f:
                config = json.load(f)
                config["save_path"] = directory_path
                f.seek(0)
                json.dump(config, f, indent=4)
                f.truncate()

        if event == "Calculate":
            # Execute further code here
            print("It's working!")

            ## actual code goes here

            with open('config.json') as f:
                config_data = json.load(f)
            #pdb_file = choose_file()

            pdb_file = config_data['pdb_file']

            pdb_df = read_pdb(pdb_file)
            pdb_name = get_pdb_code(pdb_file)

            scalar = 5.0
            #scalar = config_data['scale']
            clipped = clip_coords(pdb_df)
            scaled = scale_coordinates(clipped, scalar)
            moved = move_coordinates(scaled)
            rounded = round_df(moved)

            branches = sidechain(rounded)

            backbone = atom_subset(rounded, ['C', 'N', 'CA'], include=True)

            # sidechain = atom_subset(rounded_two, ['C', 'N', 'CA'], include=False)
            intermediate = find_intermediate_points(backbone)

            coord = rasterized_sphere((2, 2, 2), 1.5, (5, 5, 5))

            shortened = shorten_atom_names(rounded)
            spheres = add_sphere_coordinates(coord, (2, 2, 2), shortened)

            #mcfunctions = choose_subdir("")

            mcfunctions = config_data['save_path']

            pdb_backbone = pdb_name + "_backbone"
            create_minecraft_functions(intermediate, pdb_backbone, False, mcfunctions)

            pdb_sidechain = pdb_name + "_sidechain"
            create_minecraft_functions(branches, pdb_sidechain, False, mcfunctions)

            pdb_atoms = pdb_name + "_atoms"
            create_minecraft_functions(spheres, pdb_atoms, False, mcfunctions)

            mcfiles = find_mcfunctions(mcfunctions, pdb_name.lower())
            print(mcfiles)

            create_master_function(mcfiles, pdb_name, mcfunctions)

            sg.popup("Finished! Remember to /reload in your world and /function protein:drop_###")



    # Close the window
    window.close()






    #mc_backbone = create_minecraft_functions(intermediate)
    #mc_atoms = create_minecraft_functions(spheres)

    #print(mc_backbone.head(20))
    #print(mc_atoms.head(20))

    #combined = pd.concat([spheres.head(1500), intermediate.head(300), branches.head(500)])
    #combined = combined.reset_index(drop=True)
    #print(combined.head(20))
    #print(combined.tail(20))

    #plot_3d_coordinates(clip_coords(combined), 2300)
    #plot_3d_coordinates(clip_coords(spheres), 1900)
    #plot_cube(spheres, 300)

