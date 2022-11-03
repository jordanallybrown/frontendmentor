# setup logging
import logging
logger = logging.getLogger(__name__)

import src.constants as constants
import src.utils as writer
from src.readers import ReadmeReader, StylesReader
from src.html_writer import HTMLWriter

from pathlib import Path
PARENT_PATH = Path(__file__).parent

class TemplateBuilder:

    def __init__(self, challenge_path: Path) -> None:
        self._challenge_path = challenge_path
        self._starter_path = PARENT_PATH / constants.STARTER_FOLDER

    def generate_readme(self) -> None:
        logger.info(f'Read frontendmentor README-template to get header content, challenge name and repo.')
        readme = ReadmeReader(self._challenge_path / constants.README_TEMPLATE)

        logger.info(f'Copy the starter README file to the frontendmentor challenge folder.')
        writer.copy(self._starter_path, self._challenge_path, constants.README)

        logger.info(f'Write the README header content to the new README file.')
        writer.update(self._challenge_path / constants.README, readme.header_content, replace_txt=(constants.CHALLENGE_PLACEHOLDER, readme.challenge_repo_name))

        logger.info(f'Deleting the README-template, since this file is no longer needed.')
        writer.delete(self._challenge_path / constants.README_TEMPLATE)

    def generate_index(self) -> None:
        html_writer = HTMLWriter(self._challenge_path / constants.INDEX)
        html_writer.update()
    
    def generate_styles(self) -> None:
        styles = StylesReader(self._challenge_path / constants.STYLE_GUIDE)
        
        logger.info(f'Copy the starter styles folder to the frontendmentor challenge folder.')
        writer.copy_dir(self._starter_path, self._challenge_path, constants.STYLES_FOLDER)
        writer.update(self._challenge_path / constants.STYLESHEET, 
                replace_txt=(constants.COLORS_PLACEHOLDER, styles.colors))
        


    def run(self) -> None:
        try:
            if not self._challenge_path.is_dir():
                raise NotADirectoryError

            self.generate_readme()
            self.generate_styles()
            self.generate_index()


        except NotADirectoryError:
            logger.error(f'The folder name you entered is not a directory.')
        except FileNotFoundError:
            logger.error(f'A file or directory does not exist, ensure all needed files are present.')
        except BaseException as err:
            logger.error(f'Unexpected {err=}, {type(err)=}')
        finally:
            logger.info(f'Exit template builder.')

    def __str__(self) -> str:
        return f'TemplateBuilder challenge folder: {self._challenge_path}'
