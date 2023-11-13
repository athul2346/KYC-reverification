# KYC Reverification System
# Overview

The KYC Reverification project is designed to validate whether the uploaded image of a KYC document matches the claimed document type. Primarily used in financial industries, this system helps prevent discrepancies where customers or field employees assert a specific KYC document but upload a different one. Such inconsistencies can lead to regulatory issues, especially concerning RBI regulations.

The project employs Google's Vision API and a series of regular expressions to extract text from the uploaded image, determining the type of KYC document. The system is capable of recognizing various document types such as driving licenses, Aadhar cards, etc.
Usage

    Input Processing: Images are provided in the input folder, and the system transforms them into a standardized format, consolidating them into the realinput folder.

    Document Type Recognition: The main_code.py file serves as the main Python script, utilizing the new_vision_test.py module. This module contains functions to identify the type of KYC document based on the extracted text. It is important to specify the expected document type for reverification.

    Output: The system processes each image and prints the recognized document type. If the image does not match the expected document type, it indicates a potential discrepancy.

# Prerequisites

    Google Vision API Key: The program relies on Google's Vision API for text extraction. Ensure you have the necessary API key for the system to function correctly.

# Code Structure

The project consists of two Python files:

    main_code.py: The main script for running the KYC reverification system.
    new_vision_test.py: A module containing functions for identifying the KYC document type based on text extraction.

# Important Note

This project is designed for reverification, meaning the expected KYC document type should be communicated to the program. The system will then validate whether the uploaded image matches the specified document type and provide the actual document type detected.

If you only wish to identify the type of KYC document without reverification, make the necessary modifications to the code accordingly.

Feel free to contribute, report issues, or suggest improvements to enhance the accuracy and functionality of the KYC reverification system.
