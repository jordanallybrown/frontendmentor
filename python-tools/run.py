import argparse
from pathlib import Path

ROOT_PATH  = Path(__file__).parents[1] # walk up 2 dirs to reach top level
PARENT_PATH = Path(__file__).parent
# setup logging NOTE logging must be defined before any submodules that will share the same loggger and logger.config 
import logging
import logging.config
logging.config.fileConfig(PARENT_PATH / 'logging.conf')
logger = logging.getLogger(__name__)

import src.constants as constants
from src.template_builder import TemplateBuilder
from src.markdown_writer import TableWriter

def is_yes(answer: str) -> bool:
    return answer.lower() == 'y'

if __name__ == "__main__":
    # Get frontendmentor challenge folder with command line args
    parser = argparse.ArgumentParser(description='Generate starter files for frontendmentor challenges.')
    parser.add_argument(
        'foldername', 
        help='the foldername of the frontendmentor challenge')
    parser.add_argument(
        'mode',
        help='Set the mode for what to run, choices are template and table',
        type=str,
        choices=['template', 'table']
    )
    args = parser.parse_args()

    challenge_folder_path = ROOT_PATH / args.foldername
    
    if args.mode == 'template':
        answer = input(f'By running template, README.md, styles folder, and index.html will be overwritten in: {challenge_folder_path}.\nPlease confirm  and enter (y) to continue:')
        if is_yes(answer):
            template_builder = TemplateBuilder(challenge_folder_path)
            template_builder.run()
    if args.mode == 'table':
        readme_path = ROOT_PATH / constants.README
        answer = input(f'By running table, the table in {readme_path} will append the challenge info from: {challenge_folder_path}.\nPlease confirm  and enter (y) to continue:')
        if is_yes(answer):
            table_writer = TableWriter(challenge_folder_path, readme_path)
            table_writer.write()
