# Ophilia Picture Row Selector

## Description
The Ophilia Picture Row-Selector CLI is a specialized command-line interface designed to streamline the process of organizing and moving specific files between directories. This tool allows users to select files based on matching names from a source directory and copy them into a destination directory while filtering them by the desired extensions. It is particularly useful in scenarios where there is a need to sync or selectively migrate image files, document files, or any other types of files from one folder to another, ensuring that only files with specified names and extensions are transferred.

## Usage
To use the Ophilia Picture Row Selector, you need to navigate to the directory where the script is located and run it with the necessary options. Here are the steps and options explained:

### Basic Command Structure:
```bash
op-row-select [OPTIONS]
```

### Options:
- `-s` or `--source`: Specifies the source file path where the files to be copied are located.
- `-t` or `--target`: Indicates the target file path where the files are to be copied to.
- `-e` or `--extension`: Defines the target file extensions that should be considered when copying the files. This option can handle multiple extensions.
- `-d` or `--destination`: Designates the destination source file path where the selected files will be copied.

### Example Command:
```bash
op-row-select -s ./images -t ./backup -e jpg -e png -d ./selected_images
```
This command will copy all files from the `./images` directory to the `./selected_images` directory, but only if the same file name (regardless of the extension) exists in the `./backup` directory and the file has an extension of either `.jpg` or `.png`.
