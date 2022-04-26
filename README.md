# SimpleFileEncrypt
Just a very simple encryption program for non-critical files.

Note: Do not use this for critical files. This program is only for items you want to hide from non-programmers or other peering eyes with no experience in code.

Make sure you keep back ups of files you encrypt. Included are two ways to encrypt: One will leave the original file and create a new encrypted files. The other method will replace the original file with the encrypted file of the same name.

To run as an application the .exe file should be placed in the folder containing the file(s) you wish to encrypt.

To create an .exe file in terminal and install pyinstaller:

1. pip install pyinstaller
2. pyinstaller main.py --onefile
3. main.exe is located in new dist folder

Note: To encrypt multiple files simply add the files to a .zip folder and then encrypt.

Disclaimer: Use at your own risk.
