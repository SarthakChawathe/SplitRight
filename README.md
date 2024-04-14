# SplitPDF
Splitting PDFs with ease.

## Table of Contents
- [Introduction](https://github.com/pbadhe/SplitPDF/tree/main/README.md#introduction)
- [General notes](https://github.com/pbadhe/SplitPDF/tree/main/README.md#general-notes)
- [Dependencies](https://github.com/pbadhe/SplitPDF/tree/main/README.md#dependencies)
- [Application Setup](https://github.com/pbadhe/SplitPDF/tree/main/README.md#application-setup)
- [Features](https://github.com/pbadhe/SplitPDF/tree/main/README.md#features)
- [How to use](https://github.com/pbadhe/SplitPDF/tree/main/README.md#how-to-use)
- [System requirements](https://github.com/pbadhe/SplitPDF/tree/main/README.md#system-requirements)
- [Screenshots](https://github.com/pbadhe/SplitPDF/tree/main/README.md#screenshots)
- [Link to Download Application](https://github.com/pbadhe/SplitPDF/edit/main/README.md#link-to-final-dashboard)

## Introduction 
This standalone desktop application is designed to split PDF files using Optical Character Recognition (OCR) technology. 
It provides a user-friendly interface for easily splitting PDF documents based on their content, making it a handy tool for organizing and managing PDF files efficiently.

## General notes

To run this app you need python and Tesseract installed on machine. 
- Link to install Tesseract on Windows: https://ironsoftware.com/csharp/ocr/blog/ocr-tools/install-tesseract/


## Dependencies

This assumes you've got installed:

- git
- tk
- numpy
- customtkinter
- pytesseract
- tesseract
- tesserocr


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
- Operating System: Windows 10/11, macOS, or Linux
- Processor: Dual-core processor or higher
- RAM: 2GB or more
- Disk Space: 100MB of free space

## Screenshots

![Linux build](/nodeploy/linux_todo.png?raw=true "Linux build")
![Windows build](/nodeploy/windows_todo.png?raw=true "Windows build")
![MacOS build](/nodeploy/macos_todo.png?raw=true "MacOS build")
![Android build](/nodeploy/android_todo.png?raw=true "Android build")
![iOS build](/nodeploy/ios_todo.png?raw=true "iOS build")
![Website](/Images/website.png)

## Link to Download Application
Link : https://lookerstudio.google.com/s/sQyFkRE_B0o

