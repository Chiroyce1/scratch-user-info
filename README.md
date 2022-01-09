# scratch-user-data
Command line tool for getting information about a Scratch User

More info available [here](https://scratch.mit.edu/discuss/topic/542409/?page=1#post-5600424).

## How to add a PowerShell alias (On Windows)
1. Open PowerShell
2. Type `$PROFILE` and press enter
3. Create a new file called Microsoft.PowerShell_profile.ps1 in the directory it gives you
4. Add this to your profile, replacing `path\to\main.py` with the actual path:
```pwsh
Set-Alias "python C:\path\to\main.py" scratchuser
```
5. Run `scratchuser` in PowerShell. It should work!
