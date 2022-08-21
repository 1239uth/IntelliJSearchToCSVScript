# IntelliJ Search To CSV Python Script

This python script converts a given text file through the command line formatted by indentation outputted by IntelliJ Search tool to a CSV file.

## Steps to Use

1. Search for some text in IntelliJ (Ctrl/Cmd + Shift + F) and click on 'Open in Find Window'

<img src="README_photos/findInFiles.png" alt="Find in Files IntelliJ Popup" width="300px">

2. Right click anywhere and click 'Export to Text File'

<img src="README_photos/ExportToTextFile.png" alt="Export to Text File IntelliJ Option" width="300px">

3. Save it in the directory of this project

<img src="README_photos/saveTxt.png" alt="Save text file IntelliJ Popup" width="300px">

4. `cd` into the directory and run `python script.py <filename.txt>`
5. Open the generated .xlsx file with Microsoft Excel

## Example:

### Input:
![Text file used as input](README_photos/test_input.png)

### Output:
![Excel file produced as output](README_photos/test_output.png)
