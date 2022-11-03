''' REPO '''
REPO_LINK = 'https://jordanallybrown.github.io/frontendmentor/'

''' FRONTENDMENTOR '''
LEVEL = 'Newbie'

''' FILE EXTENSIONS '''
README_TEMPLATE = 'README-template.md'
README = 'README.md'
STYLE_GUIDE = 'style-guide.md'
STYLESHEET = 'styles/style.css'
INDEX = 'index.html'

''' FOLDER NAMES '''
STARTER_FOLDER = 'starter'
STYLES_FOLDER = 'styles'

''' PLACEHOLDERS '''
CHALLENGE_PLACEHOLDER = '{%challenge%}'
COLORS_PLACEHOLDER = '/* {%colors%} */'

''' MARKDOWN SYMBOLS '''
# {'h1': 1, 'h2': 2, 'h3': 3, 'h4': 4, 'h5': 5, 'h6': 6}
MARKDOWN_HEADERS = {"h"+str(num): num for num in range(1, 6+1)}
COLOR_HEADER = '## Colors'
TABLE_HEADER = '## Solutions'

''' HTML STARTER CONTENT '''
STYLE_LINKS = '''
  <link rel="stylesheet" href="./styles/normalize.css">
  <link rel="stylesheet" href="./styles/style.css">
'''
FOOTER_CONTENT = '''
  <footer>
    Challenge by <a href="https://www.frontendmentor.io?ref=challenge" target="_blank">Frontend Mentor</a>. 
    Coded by <a href="https://github.com/jordanallybrown/">Jordan</a>.
  </footer>
'''
MAIN_H1_CONTENT = '''
<main>
    <h1 class="sr-only">Frontend Mentor Order Summary component solution.</h1>
</main>
'''

HTML_CONTENT = {
    'head' : [STYLE_LINKS],
    'body' : [MAIN_H1_CONTENT, FOOTER_CONTENT]
}
