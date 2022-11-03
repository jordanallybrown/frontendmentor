# Python automation tools

This is a python tool that automates generating starter files for Frontend Mentor challenges. 
 
## Overview

There are 2 main features of this tool -- template builder and table writer. 

### Template Builder

This class is responsible for using the `/starter` files to generate starting text and code for the README.md, stylesheets, and index.html.     

- The README.md is based on the README-template.md to find the challenge header and repo info
- The `style.css` gets the root colors from style-guide.md and copies over the starter code in both the `style.css` and `normalize.css`
- The tool generates starter tags and classes `index.html`

### Table Writer

This class is responsible for adding the challenge to the table in the main README i.e. frontendmentor/README.md. This will get the challenge info as a row and write to the README the challenge name, repo and live link. This adds the challenge as the last row in the existing table.

## How to run

### Installation requirements
python version 3

### Command line

`cd` to the root folder i.e. `frontendmentor`. 

To run template builder:
```
python3 python-tools/run.py challenge-folder-name template
```

To run table writer:
```
python3 python-tools/run.py challenge-folder-name table
```

Both run commands will prompt you for confirmation since the scripts will modify and delete files.