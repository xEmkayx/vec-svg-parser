# INFO
You can also use the webeditor without downloading anything at 
https://xemkayx.github.io/vec-svg-parser-webapp/
[Link to other repo](https://github.com/xEmkayx/vec-svg-parser-webapp).

# Parse .vec files to .svg images
Render images from .vec files created by programs like "Pictures by PC" or "isycam". 
Syntax is limited to these languages.
If you're a student that has to use these programs in school but has no access to those 
at home, you can simply parse your code with this script and see the result.

# Example
![Example image](https://raw.githubusercontent.com/xEmkayx/vec-svg-parser/master/static/IMG/adv.svg)

https://github.com/xEmkayx/vec-svg-parser/blob/0584c7c990f1475d8f668c357dc22659e2a2f10c/input/adv_schild#L1-L49

# How to use
## Web Editor
There is a web-editor that works without having to create files. It's reachable via http://127.0.0.1:5000/editor
## GUI
Start the GUI/Webgui and select the input image and output image filename and hit submit. The images are saved
to the '/static/IMG/' folder
## CLI
Run the [parser.py](https://github.com/xEmkayx/vec-svg-parser/blob/master/parser.py) file with these arguments:
- -i, --input-file 'path/to/input/file'
- -o, --output-file 'output_filename'

# Installation
You need a valid python installation (I used Python3.11.2). If you want to use the webgui, you need to install the 
requirements via the [requirements.txt](https://github.com/xEmkayx/vec-svg-parser/blob/master/requirements.txt) file