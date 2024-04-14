# SplitPDF
Splitting PDFs with ease

## Changes in 1.1

- Updated to Phoenix 1.7 and LiveView 0.18

## Changes in 1.0

- Updated to Phoenix 1.6 with esbuild+dart_scss
- Added iOS platform example wrapper (see https://github.com/elixir-desktop/ios-example-app)
- Added Android platform example wrapper (see https://github.com/elixir-desktop/android-example-app)

## General notes

To run this app you need at least Erlang 24 and recent builds of wxWidgets and at least
Elixir 1.11.4.

## Dependencies

Make sure to install the following dependecies:

- git
- tk
- numpy
- customtkinter
- pytesseract
- tesserocr
  

## Application set-up

Run:

```bash
cd assets
npm install
cd ..
mix assets.deploy
```


## Usage
1) Open PDF: Click on the "Open PDF" button to select the PDF file you want to split.
2) OCR Processing: The application will process the PDF using OCR to identify text content.
3) Set Splitting Parameters: Define the criteria for splitting the PDF (e.g.by keyword, by pixel location).
4) Split PDF: Click on the "Split" button to initiate the splitting process.
5) Save Split PDFs: Choose the destination folder for the split PDF files and click "Save".

## Screenshots

![Linux build](/nodeploy/linux_todo.png?raw=true "Linux build")
![Windows build](/nodeploy/windows_todo.png?raw=true "Windows build")
![MacOS build](/nodeploy/macos_todo.png?raw=true "MacOS build")
![Android build](/nodeploy/android_todo.png?raw=true "Android build")
![iOS build](/nodeploy/ios_todo.png?raw=true "iOS build")
