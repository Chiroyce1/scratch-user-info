# scratch-user-data
## BETA branch
### This version shouldn't be used unless you are contributing to this or providing feedback on the upcoming features.

Command line tool for getting information about a Scratch User

More info available [here](https://scratch.mit.edu/discuss/topic/542409/?page=1#post-5600424).

## Installation

```bash
git clone -b beta https://github.com/Chiroyce1/scratch-user-data
cd scratch-user-data
pip install -r requirements.txt
# run pip3 if pip doesn't work
```

If you don't have Git installed, click [here](https://github.com/Chiroyce1/scratch-user-data/archive/refs/heads/main.zip) to download a zip file, unzip it, and then run 
```bash
cd scratch-user-data
pip install -r requirements.txt
```

## Usage
```bash
python main.py Chiroyce
# returns data about the Scratch user Chiroyce
```

## Using it with alias
### Linux / macOS (bash)
```bash
cd ~
vi .bashrc
# or nano .bashrc
```

### Linux / macOS (zsh)
```zsh
cd ~
vi .zshrc
# or nano .zshrc
```

Then add this to the end of the file
```bashrc
alias scratchuser='python /path-to-scratch-user-data/main.py'
```
Make sure to use the actual path instead
