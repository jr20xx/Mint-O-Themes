# Mint O Themes

### What is this?
Mint O Themes are an adaptation (made by myself) of the well known [Mint Y themes](https://github.com/linuxmint/mint-themes) with the hope to bring a similar appearance to those themes to [Openbox 3](https://github.com/danakj/openbox) users.

Ever since I started using Openbox, I always wanted themes like these ones. I never found any, so I researched a bit and decided to make them on my own and let other users enjoy them with ease.

This is still a work in progress and if you want to make some kind of contribution: please, do it! I'd love to receive some help and support to improve this project.

### How to use this project?
Instead of creating all the themes one by one, I decided to make two templates: one for light variations of the themes and another for dark ones. I also created a script to apply the aproppiated colors to those templates, generate the themes and transfer them to where they should be placed to later set them as the theme for Openbox.

To setup the themes, the first thing you need to do is clone this repo by executing:

```bash
git clone https://github.com/jr20xx/Mint-O-Themes
```

After that, open the `Mint-O-Themes` folder by executing:
```bash
cd Mint-O-Themes
```

Then, the only thing left for you to do is to run the Python script and wait until it finishes its execution:
```bash
python3 install.py
```

#### Script parameters
The Python script provided to setup the themes can take two optional parameters:

- **`--color`**: This parameter is used when you want to setup only a specific number of themes colors. You can pass a single color name or multiple colors separated by a whitespace. Admitted values are **`standard`**, **`aqua`**, **`blue`**, **`grey`**, **`orange`**, **`pink`**, **`purple`**, **`red`**, **`sand`** and **`teal`**.

- **`--mode`**: This parameter is used when you want to generate only one variant of the themes. Admitted values are **`light`** or **`dark`**.

#### Examples of usage:
```bash
# To setup the dark red theme
python3 install.py --color red --mode dark
```

```bash
# To setup all the light themes
python3 install.py --mode light
```

```bash
# To setup the light variants of the standard and aqua themes
python3 install.py --color standard aqua --mode light 
```

If no parameters are provided, then all the themes with their corresponding variants will be setted up.

### How to setup the themes for all users?
That's easy! All you got to do is run the script as root and the generated themes will be moved into a location where they can be accessed for every user.

For example, let's say that you want to setup the dark variants of the blue and pink themes systemwide. All you must do is execute the following command and that would be it:
```bash
sudo python3 install.py --color blue pink --mode dark
```

### Preview
![light-themes](/previews/light.png?raw=true)


![dark-themes](/previews/dark.png?raw=true)