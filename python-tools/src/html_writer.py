# setup logging
import logging
logger = logging.getLogger(__name__)

from pathlib import Path
import src.constants as constants
# <h1 class="sr-only">Frontend Mentor Order Summary component solution.</h1>

class HTMLTag:

    def __init__(self, name: str, content: str = '', cls: str = '') -> None:
        self._name = name
        self._content = content
        self._cls = cls # could have a list for multiple classes, but just need one for my script
        self._tag: str = None
        self._start_tag: str = None
        self._end_tag: str = None

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, txt) -> None:
        self._content = txt

    @property
    def tag(self) -> str:
        return f'{self.start_tag}{self._content}{self.end_tag}'

    @property
    def name(self) -> str: 
        return self._name

    @property
    def start_tag(self) -> str:
        return f'<{self._name}>' if not self._cls else f'<{self._name} class="{self._cls}">'

    @property
    def end_tag(self) -> str:
        return f'</{self._name}>'

class HTMLWriter:

    def __init__(self, path: Path) -> None:
        self._path = path

    def update(self) -> None:
        try:
            style = HTMLTag('style')
            footer = HTMLTag('footer')
            body = HTMLTag('body')
            title = HTMLTag('title')
            main = HTMLTag('main')
            h1 = HTMLTag('h1', cls='sr-only')
            
            with self._path.open('r+') as html_file:
                logger.info(f'Begin building new index file.')
                content = []
                ignore_tags = [style, footer]
                ignore_flag = False
                end_tags = [style, footer]
                for line in html_file:
                    if title.start_tag in line:
                        content.append(line)
                        h1.content = line.strip().replace(title.start_tag, '').replace(title.end_tag, ' solution')
                    elif body.start_tag in line:
                        content.extend([line, main.start_tag, '\n', h1.tag, '\n', main.end_tag, '\n'])
                    elif any(tag.start_tag in line for tag in ignore_tags):
                        ignore_flag = True
                    elif any(tag.end_tag in line for tag in end_tags):
                        if style.end_tag in line:
                            content.append(constants.STYLE_LINKS)
                        elif footer.end_tag in line:
                            content.append(constants.FOOTER_CONTENT)
                        ignore_flag = False
                    elif ignore_flag:
                        continue
                    else:
                        content.append(line)
                logger.info(f'Writing html content back to {self._path}')
                html_file.seek(0, 0)
                html_file.write(''.join(content))
                # print(''.join(content))


        except Exception as e:
            raise

