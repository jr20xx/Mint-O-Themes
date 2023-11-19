import os, shutil, argparse
from types import NoneType

RED = "\033[91m"; GREEN = "\033[92m"; YELLOW = "\033[93m"; BLUE = "\033[94m"; RESET = "\033[0m"

def generateTheme(color, light=True):
    template = ""
    file = open("templates/light-template", "r") if light else open("templates/dark-template", "r")
    for line in file.readlines():
        template += line
    file.close()
    print(GREEN + '\n' + ("Light template loaded" if light else "Dark template loaded"))
    print(YELLOW + "Generating " + color + " theme")
    export_path = ""

    if color == "standard":
        template = template.replace("$WINDOW_ACTIVE_CLOSE_BUTTON_UNPRESSED_FG","#35A854") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_HOVERED_FG","#68BE7F") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_PRESSED_FG","#287E3F")
    elif color == "aqua":
        template = template.replace("$WINDOW_ACTIVE_CLOSE_BUTTON_UNPRESSED_FG","#1F9EDE") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_HOVERED_FG","#57B6E6") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_PRESSED_FG","#1776A6")
    elif color == "blue":
        template = template.replace("$WINDOW_ACTIVE_CLOSE_BUTTON_UNPRESSED_FG","#0C75DE") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_HOVERED_FG","#4998E6") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_PRESSED_FG","#0958A6")
    elif color == "grey":
        template = template.replace("$WINDOW_ACTIVE_CLOSE_BUTTON_UNPRESSED_FG","#70737A") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_HOVERED_FG","#94969B") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_PRESSED_FG","#54565B")
    elif color == "orange":
        template = template.replace("$WINDOW_ACTIVE_CLOSE_BUTTON_UNPRESSED_FG","#FF7139") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_HOVERED_FG","#FF956B") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_PRESSED_FG","#BF552B")
    elif color == "pink":
        template = template.replace("$WINDOW_ACTIVE_CLOSE_BUTTON_UNPRESSED_FG","#E54980") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_HOVERED_FG","#EC77A0") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_PRESSED_FG","#AC3760")
    elif color == "purple":
        template = template.replace("$WINDOW_ACTIVE_CLOSE_BUTTON_UNPRESSED_FG","#8C5DD9") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_HOVERED_FG","#A986E3") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_PRESSED_FG","#6946A3")
    elif color == "red":
        template = template.replace("$WINDOW_ACTIVE_CLOSE_BUTTON_UNPRESSED_FG","#E82127") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_HOVERED_FG","#EE595D") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_PRESSED_FG","#AE1910")
    elif color == "sand":
        template = template.replace("$WINDOW_ACTIVE_CLOSE_BUTTON_UNPRESSED_FG","#C5A07C") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_HOVERED_FG","#D4B89D") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_PRESSED_FG","#94785D")
    elif color == "teal":
        template = template.replace("$WINDOW_ACTIVE_CLOSE_BUTTON_UNPRESSED_FG","#199CA8") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_HOVERED_FG","#53B5BE") \
            .replace("$WINDOW_ACTIVE_CLOSE_BUTTON_PRESSED_FG","#13757E")

    if light:
        if color == "standard":
            template = template.replace("$MENU_TITLE_BG","#71d28b") \
                .replace("$MENU_ITEM_ACTIVE_BG","#98deab")
        elif color == "aqua":
            template = template.replace("$MENU_TITLE_BG","#77c5ec") \
                .replace("$MENU_ITEM_ACTIVE_BG","#a4d8f2")
        elif color == "blue":
            template = template.replace("$MENU_TITLE_BG","#5aa8f6") \
                .replace("$MENU_ITEM_ACTIVE_BG","#8ac2f9")
        elif color == "grey":
            template = template.replace("$MENU_TITLE_BG","#a4a7ac") \
                .replace("$MENU_ITEM_ACTIVE_BG","#bfc0c4")
        elif color == "orange":
            template = template.replace("$MENU_TITLE_BG","#ffba9f") \
                .replace("$MENU_ITEM_ACTIVE_BG","#ffdfd2")
        elif color == "pink":
            template = template.replace("$MENU_TITLE_BG","#f2a2be") \
                .replace("$MENU_ITEM_ACTIVE_BG","#f8cfdd")
        elif color == "purple":
            template = template.replace("$MENU_TITLE_BG","#c7b0ec") \
                .replace("$MENU_ITEM_ACTIVE_BG","#e4d9f6")
        elif color == "red":
            template = template.replace("$MENU_TITLE_BG","#f27d81") \
                .replace("$MENU_ITEM_ACTIVE_BG","#f6acae")
        elif color == "sand":
            template = template.replace("$MENU_TITLE_BG","#e4d3c3") \
                .replace("$MENU_ITEM_ACTIVE_BG","#f4ede6")
        elif color == "teal":
            template = template.replace("$MENU_TITLE_BG","#44d6e3") \
                .replace("$MENU_ITEM_ACTIVE_BG","#70e0ea")
        export_path = "generated/Mint-O" + (("-" + color.capitalize()) if color != "standard" else "") + "/openbox-3"
    else:
        if color == "standard":
            template = template.replace("$MENU_TITLE_BG","#298141") \
                .replace("$MENU_ITEM_ACTIVE_BG","#35a854")
        elif color == "aqua":
            template = template.replace("$MENU_TITLE_BG","#197eb1") \
                .replace("$MENU_ITEM_ACTIVE_BG","#1f9ede")
        elif color == "blue":
            template = template.replace("$MENU_TITLE_BG","#095cae") \
                .replace("$MENU_ITEM_ACTIVE_BG","#0c75de")
        elif color == "grey":
            template = template.replace("$MENU_TITLE_BG","#585a5f") \
                .replace("$MENU_ITEM_ACTIVE_BG","#70737a")
        elif color == "orange":
            template = template.replace("$MENU_TITLE_BG","#ff4c06") \
                .replace("$MENU_ITEM_ACTIVE_BG","#ff7139")
        elif color == "pink":
            template = template.replace("$MENU_TITLE_BG","#dc1f62") \
                .replace("$MENU_ITEM_ACTIVE_BG","#e54980")
        elif color == "purple":
            template = template.replace("$MENU_TITLE_BG","#6f34cf") \
                .replace("$MENU_ITEM_ACTIVE_BG","#8c5dd9")
        elif color == "red":
            template = template.replace("$MENU_TITLE_BG","#c21419") \
                .replace("$MENU_ITEM_ACTIVE_BG","#e82127")
        elif color == "sand":
            template = template.replace("$MENU_TITLE_BG","#b58659") \
                .replace("$MENU_ITEM_ACTIVE_BG","#c5a07c")
        elif color == "teal":
            template = template.replace("$MENU_TITLE_BG","#12737c") \
                .replace("$MENU_ITEM_ACTIVE_BG","#199ca8")
        export_path = "generated/Mint-O-Dark" + (("-" + color.capitalize()) if color != "standard" else "") + "/openbox-3"
    
    print(BLUE + "Saving generated theme to /" + export_path + "/themerc")
    os.makedirs(export_path, exist_ok=True)
    generated_theme_file = open(export_path + "/themerc", "w")
    generated_theme_file.write(template);
    generated_theme_file.close();
    print(GREEN + "Generated theme saved  to /" + export_path + "/themerc")

    print(BLUE + "Copying theme resources to /" + export_path)
    resources_files = os.listdir("templates/buttons")
    for file in resources_files:
        shutil.copy("templates/buttons/" + file, os.path.join(export_path, file))
    print(GREEN + "Theme resources copied to /" + export_path)

parser = argparse.ArgumentParser(epilog="Mint O Themes are an adaptation of the Mint Y Themes for Openbox. To install the themes systemwide, run this script as root; otherwise the themes will only be installed for the current user running the script.", description="Script to setup the Mint O Themes.",usage="""
install.py [-h | --help]
install.py [--color [COLOR...]] [--mode MODE]
""")
parser.add_argument('--color', nargs='+', type=str, help='Color variant(s) to install separated by white spaces. Supported color variants are standard, aqua, blue, grey, orange, pink, purple, red, sand and teal.', required = False)
parser.add_argument('--mode', type=str, help='Choose the theme variant to install (light or dark).', required=False)

args = parser.parse_args()
colors = args.color
mode = args.mode

terminal_width = shutil.get_terminal_size().columns
ascii_art = """
\033[93m┌──────────────────────────────────────────────────────────────────┐
\033[92m│ ░░░░░░░█▄█░▀█▀░█▀█░▀█▀░░░░░█▀█░░░░░▀█▀░█░█░█▀▀░█▄█░█▀▀░█▀▀░░░░░░ │
\033[96m│ ░░░░░░░█░█░░█░░█░█░░█░░▄▄▄░█░█░▄▄▄░░█░░█▀█░█▀▀░█░█░█▀▀░▀▀█░░░░░░ │
\033[91m│ ░░░░░░░▀░▀░▀▀▀░▀░▀░░▀░░░░░░▀▀▀░░░░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░░░░░░ │
\033[95m└──────────────────────────────────────────────────────────────────┘
"""
print("\n".join(line.center(terminal_width) for line in ascii_art.splitlines()) + RESET)

all_colors = ["standard","aqua","blue","grey","orange","pink","purple","red","sand","teal"]
if not type(colors) is NoneType:
    tmpc = []
    colors = list(set(colors))
    for color in colors:
        if color in all_colors:
            tmpc.append(color)
        else:
            print(RED + "\033[1mERROR:\033[0m" + RED + " Color theme not supported: " + color)
    colors = tmpc
    if len(colors) == 0:
        exit(RED + "\033[1mERROR:\033[0m" + RED + " All the colors you inputted were not supported.")
else:
    colors = all_colors

for color in colors:
    if mode != None:
        generateTheme(color, mode == "light")
    else:
        for color in colors:
            generateTheme(color)
            generateTheme(color, False)

print(GREEN + "\nThemes generation finished")

export_path = os.path.expanduser('~') + "/.themes" if os.geteuid() != 0 else "/usr/share/themes"
os.makedirs(export_path, exist_ok=True)
print(YELLOW + "Transferring generated themes to " + export_path)

generated_themes = os.listdir("generated")
for folder in generated_themes:
    print(BLUE + "Transferring " + folder + " to " + export_path)
    destination_folder = os.path.join(export_path, folder)
    
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)
    
    shutil.move("generated/" + folder, destination_folder)

print(YELLOW + "Removing temporal folder...")
os.removedirs("generated")

print(GREEN + "\nGenerated themes transfered to " + export_path)

ascii_art = """
\033[95m┌──────────────────────────────────────────────────┐
\033[91m│ ░░░░░░░░█▀█░█░░░█░░░░░█▀▄░█▀█░█▀█░█▀▀░░░█░░░░░░░ │
\033[96m│ ░░░░░░░░█▀█░█░░░█░░░░░█░█░█░█░█░█░█▀▀░░░▀░░░░░░░ │
\033[92m│ ░░░░░░░░▀░▀░▀▀▀░▀▀▀░░░▀▀░░▀▀▀░▀░▀░▀▀▀░░░▀░░░░░░░ │
\033[93m└──────────────────────────────────────────────────┘
"""
print("\n".join(line.center(terminal_width) for line in ascii_art.splitlines()) + RESET)