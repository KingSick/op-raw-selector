import os
import shutil

import rich_click as click

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_FILE = f"{BASE_DIR}/temp.py"


@click.group()
@click.rich_config(help_config=click.RichHelpConfiguration(use_markdown=True))
def cli():
    """
    ```
     ██████╗ ██████╗ ██╗  ██╗██╗██╗     ██╗ █████╗       ██████╗ ██╗ ██████╗████████╗██╗   ██╗██████╗ ███████╗
    ██╔═══██╗██╔══██╗██║  ██║██║██║     ██║██╔══██╗      ██╔══██╗██║██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
    ██║   ██║██████╔╝███████║██║██║     ██║███████║█████╗██████╔╝██║██║        ██║   ██║   ██║██████╔╝█████╗
    ██║   ██║██╔═══╝ ██╔══██║██║██║     ██║██╔══██║╚════╝██╔═══╝ ██║██║        ██║   ██║   ██║██╔══██╗██╔══╝
    ╚██████╔╝██║     ██║  ██║██║███████╗██║██║  ██║      ██║     ██║╚██████╗   ██║   ╚██████╔╝██║  ██║███████╗
     ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚═╝  ╚═╝      ╚═╝     ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
    ██████╗  ██████╗ ██╗    ██╗      ███████╗███████╗██╗     ███████╗ ██████╗████████╗ ██████╗ ██████╗
    ██╔══██╗██╔═══██╗██║    ██║      ██╔════╝██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
    ██████╔╝██║   ██║██║ █╗ ██║█████╗███████╗█████╗  ██║     █████╗  ██║        ██║   ██║   ██║██████╔╝
    ██╔══██╗██║   ██║██║███╗██║╚════╝╚════██║██╔══╝  ██║     ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
    ██║  ██║╚██████╔╝╚███╔███╔╝      ███████║███████╗███████╗███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
    ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝       ╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

    ```

    🦋 Ophilia Picture Row-Selector CLI 입니다. 🦋
    """


@cli.command()
@click.option("-s", "--source", required=True, help="Source file path")
@click.option("-t", "--target", required=True, help="Target file path")
@click.option(
    "-e", "--extension", required=True, help="Target file extension", multiple=True
)
@click.option("-d", "--destination", required=True, help="Destination source file")
def row_selector(source: str, target: str, extensions: list[str], destination: str):
    """source 폴더 파일과 같은 이름의 파일을 target 폴더에서 찾아서 destination 폴더에 복사합니다."""
    source_files = os.listdir(source)
    target_files = os.listdir(target)

    for source_file in source_files:
        source_file_name = source_file.split(".")[0]
        add_extension_file_name_list = [
            f"{source_file_name}.{extension}" for extension in extensions
        ]
        for target_file in target_files:
            if target_file in add_extension_file_name_list:
                shutil.copy(f"{target}/{target_file}", destination)
                break


if __name__ == "__main__":
    cli()
