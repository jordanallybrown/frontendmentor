# setup logging
import logging
logger = logging.getLogger(__name__)

from pathlib import Path
import shutil

def copy_dir(src: Path, dest: Path, folder_name: str) -> None:
    src_folder = src / folder_name
    dest_folder = dest / folder_name
    
    # copy and overwrite all contents from src directory to dest
    shutil.copytree(src_folder, dest_folder, dirs_exist_ok=True)

def copy(src: Path, dest: Path, file_name: str) -> None:
    # build paths based on the file name
    src_file = src / file_name
    dest_file = dest / file_name

    # copy the file from src to dest folder
    logger.info(f"Replacing {dest_file} with a copy of {src_file}")
    shutil.copy(src_file, dest_file)

def update(path: Path, prepend_txt: str = "", append_txt: str = "", replace_txt: tuple[str, str] = None) -> None:
    try:
        content = []
        if prepend_txt:
            logger.info(f"Saving the following text to prepend at beginning of file: {prepend_txt}")
            content.append(prepend_txt)
        with path.open("r+") as file:
            if replace_txt:
                old_txt, new_txt = replace_txt
                logger.info(f"Begin searching for occurences of {old_txt} to replace with {new_txt}.")
                for line in file:
                    if old_txt in line:
                        logger.debug(f"Found {old_txt} in {line}, replacing with {new_txt}")
                        line = line.replace(old_txt, new_txt)
                    content.append(line)
            else:
                logger.info(f"Reading in all content from {path}")
                old_data = file.read()
                content.append(old_data)
            if append_txt:
                logger.info(f'Saving the {append_txt} to the content.')
                content.append(append_txt)

            logger.info(f"Writing back all updated content to {path}.")
            file.seek(0, 0) # start back at beginning of file to overwrite
            content_txt = ''.join(content)
            file.write(content_txt)
    except FileNotFoundError:
        logger.error(f"Failed to update because could not find file: {path}")
        raise

def delete(path: Path):
    logger.info(f"Deleting {path}.")
    path.unlink()