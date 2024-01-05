# Ophilia Picture RAW Selector

![Ophilia Picture RAW Selector](snapshot.png)

## Description
The Ophilia Picture RAW-Selector CLI is a specialized command-line interface designed to streamline the process of organizing and moving specific files between directories. This tool allows users to select files based on matching names from a source directory and copy them into a destination directory while filtering them by the desired extensions. It is particularly useful in scenarios where there is a need to sync or selectively migrate image files, document files, or any other types of files from one folder to another, ensuring that only files with specified names and extensions are transferred.

## Install
```bash
pip install git+https://github.com/KingSick/op-raw-selector.git
```

## Usage
To use the Ophilia Picture RAW Selector, you need to navigate to the directory where the script is located and run it with the necessary options. Here are the steps and options explained:

### Basic Command Structure:
```bash
op-raw-select [OPTIONS]
```

### Options:
- `-s` or `--source`: Specifies the source file path where the files to be copied are located.
- `-t` or `--target`: Indicates the target file path where the files are to be copied to.
- `-e` or `--extension`: Defines the target file extensions that should be considered when copying the files. This option can handle multiple extensions.
- `-d` or `--destination`: Designates the destination source file path where the selected files will be copied.

### Example Command:
```bash
op-raw-select -s ./images -t ./backup -e jpg -e png -d ./selected_images
```
This command will copy all files from the `./images` directory to the `./selected_images` directory, but only if the same file name (regardless of the extension) exists in the `./backup` directory and the file has an extension of either `.jpg` or `.png`.

### Required Steps for Python/bin Path Configuration

**1. Determine the Python/bin Path:**

- **For most standard Python installations:**
    - The `python/bin` directory is typically located within the main Python installation directory.
    - Use the following command to check its path:

    ```bash
    which python3  # Or `which python` for Python 2
    ```

- **If you have multiple Python versions:**
    - Specify the desired version (e.g., `python3.9`) in the `which` command.

**2. Add the Path to PATH (Bash):**

1. Add the following line, replacing `/path/to/python/bin` with the actual path:

    ```bash
    echo 'export PATH="/path/to/python/bin:$PATH"' > ~/.bashrc?
    ```
   
2. Apply the changes:

    ```bash
    source ~/.bashrc
    ```

**3. Add the Path to PATH (Zsh):**

1. Add the following line, replacing `/path/to/python/bin` with the actual path:

    ```bash
    echo 'export PATH="/path/to/python/bin:$PATH"' > ~/.zshrc
    ```

2. Apply the changes:

    ```bash
    source ~/.zshrc
    ```

**4. Verify the Path:**

- Use the following command to check if the path has been added successfully:

    ```bash
    echo $PATH
    ```

The output should include the `python/bin` directory path.
