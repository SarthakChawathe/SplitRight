# SplitPDF
Splitting PDFs with ease


## General notes

To run this app you need python and Tesseract installed on machine.
Elixir 1.11.4.

## Dependencies

This example assumes you've got installed:

- git
- Elixir, at least 1.11.4
- Erlang, at least OTP 24
- npm
- C compiler (make/nmake) for SQLite

If you want to build for iOS you'll also need xcode and in order to build for Android you'll need the
Android Studio.

## Application set-up

Run:

```bash
cd assets
npm install
cd ..
mix assets.deploy
```

## Features
1) PDF Splitting: Split PDF files into multiple documents based on text content.
2) OCR Technology: Utilizes Optical Character Recognition to accurately identify text in PDF files.
3) User-Friendly Interface: Intuitive design for easy navigation and operation.
4) Customizable Settings: Adjust settings for OCR accuracy and PDF splitting preferences.
5) Save Options: Choose where to save split PDF files for convenient access.

## How to Use
- Open PDF: Click on the "Browse" button to select the PDF file you want to split.
- OCR Processing: The application will process the PDF using OCR to identify text content.
- Set Splitting Parameters: Define the criteria for splitting the PDF (e.g. by Labels, by Location).
- Split PDF: Click on the "Convert" button to initiate the splitting process.
- Save Split PDFs: Choose the destination folder or path for the split PDF files and click "Save".


## System Requirements
- Operating System: Windows 7/8/10, macOS, or Linux
- Processor: Dual-core processor or higher
- RAM: 2GB or more
- Disk Space: 100MB of free space

## Screenshots

![Linux build](/nodeploy/linux_todo.png?raw=true "Linux build")
![Windows build](/nodeploy/windows_todo.png?raw=true "Windows build")
![MacOS build](/nodeploy/macos_todo.png?raw=true "MacOS build")
![Android build](/nodeploy/android_todo.png?raw=true "Android build")
![iOS build](/nodeploy/ios_todo.png?raw=true "iOS build")


