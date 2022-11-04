# setup logging
import logging
logger = logging.getLogger(__name__)

from itertools import takewhile
from pathlib import Path
import src.constants as constants

from pprint import pprint

class BaseReader:

    def __init__(self, path: Path) -> None:
        self._path = path


class ReadmeReader(BaseReader):

    def __init__(self, path: Path) -> None:
        super().__init__(path)
        self._full_challenge_name: str = None
        self._challenge_name: str = None
        self._challenge_repo_name: str = None
        self._header_content: list[str] = None
        self._live_link: str = None
        self._repo_path_link: str = None
        self._h1: str = None
        self._read()

    @property
    def repo_path_link(self) -> str:
        return constants.REPO_LINK_PATH + constants.SUB_REPO_PATH + self._challenge_repo_name

    @property
    def live_link(self) -> str:
        return constants.LIVE_LINK_PATH + self._challenge_repo_name + '/'

    @property
    def challenge_name(self) -> str:
        return self._challenge_name

    @property
    def challenge_repo_name(self) -> str:
        return self._challenge_repo_name
    
    @property
    def header_content(self) -> str:
        return ''.join(self._header_content)

    @property
    def h1(self) -> str:
        return self._h1

    def _read(self) -> None:

        try:
            with self._path.open() as readme:
                logger.info(f"Parsing the header content from {self._path}")
                # Get content from readme up until reaching an h2 header
                self._header_content = list(takewhile(lambda line: line.count("#") < constants.MARKDOWN_HEADERS["h2"], readme))
                if not self._header_content:
                    logger.error(f'Failed to read any header content from README.')
                    raise ValueError
                # old
                # self._h1 = self._header_content[0].strip(" #\n")
                # self._challenge_name = self._h1.replace("solution", "").strip()
                # self._challenge_repo_name = self._challenge_name.lower().replace("frontend mentor - ", "").replace(" ", "-")

                self._h1 = self._header_content[0].strip(" #\n")
                self._full_challenge_name = self._h1.replace("solution", "").strip()
                title = self._full_challenge_name.lower().replace("frontend mentor - ", "")
                self._challenge_name = title.capitalize()
                self._challenge_repo_name = title.replace(" ", "-")
                logger.info(f'Found "{self._h1}" as heading, the parsed challenge name is "{self._challenge_name}" and repo link "{self._challenge_repo_name}".')
        except FileNotFoundError:
            logger.error(f"Failed to read Frontendmentor README because could not find file: {self._path}")
            raise

class StylesReader(BaseReader):
    
    def __init__(self, path: Path) -> None:
        super().__init__(path)
        self._root: str = None
        self._colors: str = None
        self._read()

    @property
    def colors(self) -> str:
        return self._colors

    def _read(self) -> None:
        try:
            with self._path.open() as style_guide:
                logger.info(f'Begin parsing the styles guide {self._path}.')
                # content = list(takewhile(lambda line: not (constants.COLOR_HEADER in line), style_guide))
                # pprint(content)
                
                # temp - will do a better way
                for line in style_guide:
                    if constants.COLOR_HEADER in line:
                        break
                # Reached ## Colors, begin saving the color variables 
                logger.info(f'Reached the {line} heading, begin parsing colors.')
                colors = []
                color_var = '--color-'
                color_category = None
                for line in style_guide:
                    if line.count('#') == constants.MARKDOWN_HEADERS['h2']:
                        logger.debug(f'Stop, found a new h2: {line}')
                        break # stop, we've reached the next header and different style category
                    elif line == '\n':
                        logger.debug(f'Skip new lines.')
                        continue # don't process new lines
                    elif line.count('#') == constants.MARKDOWN_HEADERS['h3']:
                        logger.debug(f'Found a color category {line}, save down.')
                        h3 = '#'*constants.MARKDOWN_HEADERS['h3']
                        color_category = line.strip(f"{h3} \n").lower() + '__'
                    else:
                        logger.debug(f'Begin parsing the color txt {line}')
                        # parse the color name and value
                        color_name, color_value = line.strip('- \n').lower().split(':')
                        color_name = color_name.replace(' ', '-')

                        # build the final color variable and add to list
                        if color_category:
                            color_name = color_category + color_name
                        result = color_var + color_name + ':' + color_value + ';\n'
                        logger.debug(f'The final color variable is: {result}')
                        colors.append(result)
                logger.info(f'The colors found in the style guide are {colors}')
                # set the colors
                self._colors = ''.join(colors)

        # except ValueError:
        #     logger.error(f'')

        except FileNotFoundError:
            logger.error(f"Failed to read Frontendmentor styles because could not find file: {self._path}")
            raise
