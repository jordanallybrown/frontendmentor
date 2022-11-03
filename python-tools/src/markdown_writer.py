from distutils.command import clean
import logging
from multiprocessing.sharedctypes import Value
logger = logging.getLogger(__name__)

from pathlib import Path
from pprint import pprint

import src.constants as constants
from src.readers import ReadmeReader



'''
    ['| No.   | Challenge (repo link) | Live site | Solution url | Level |\n',
    '| :---  |   :---   |  :---   |:---   |:---   |\n',

    Check if table has at least 2 rows (any less, raise ValueError)
    nrows = len(rows) - 2
    new_row_num = nrows + 1 
    Add the row with the readme_obj info

    ['| No.   | Challenge (repo link) | Live site | Solution url | Level |\n',
    '| :---  |   :---   |  :---   |:---   |:---   |\n',
    '| 1 | QR Component | live link | solution link | newbie |\n']
'''


class TableWriter:

    def __init__(self, challenge_path, readme_path: Path) -> None:
        self._challenge_path = challenge_path
        self._readme_path = readme_path
        
    def _is_row(self, txt) -> bool:
        clean_txt = txt.strip()
        return False if not clean_txt else clean_txt[0] == '|' and clean_txt[-1] == '|'

    def _create_row(self, nrow: int, readme_obj: ReadmeReader) -> str:
        return f'| {nrow} | {readme_obj.challenge_name} | [Live link]({readme_obj.live_link}) | Solution link | {constants.LEVEL} |\n'

    def write(self) -> str:

        try: 
            logger.info(f'Read challenge README to get challenge name and repo link.')
            challenge_readme = ReadmeReader(self._challenge_path / constants.README)
            
            logger.info(f'Parse the {constants.TABLE_HEADER} table in {self._readme_path}')
            with self._readme_path.open('r+') as readme:

                is_table_section = False
                data = []
                rows = []

                for line in readme:

                    if constants.TABLE_HEADER in line:
                        is_table_section = True
                    
                    if is_table_section:
                        
                        if self._is_row(line):
                            rows.append(line)
                            continue

                        elif len(rows) > 0 and not self._is_row(line):
                            # reached the end of the table, process new data
                            logger.info(f'The current table is:\n{rows}')
                            nrows = len(rows) - 2 # exclude header and format rows
                            if nrows < 0:
                                logger.error(f'Invalid {constants.TABLE_HEADER} table. Ensure there is a table present to parse in README.')
                                raise ValueError
                            rows.append(self._create_row(nrows + 1, challenge_readme))
                            # add the new table to our data
                            logger.info(f'The new table is:\n{rows}')
                            data.extend(rows)
                            is_table_section = False

  
                    data.append(line)
                # pprint(''.join(data))
                logger.info(f'Write the new table back to {self._readme_path}')
                readme.seek(0, 0)
                readme.write(''.join(data))
                
        except FileNotFoundError:
            logger.info(f'Failed to find frontendmentor repo README.')