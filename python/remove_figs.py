import re


if __name__ == '__main__':
    with open('proof_main.tex', 'r') as f:
        tex = f.read()
    tex = tex.replace(r'\includegraphics', r'% \includegraphics')
    tex = tex.replace(r'\caption', r'% \caption')
    with open('submission_main.tex', 'w') as f:
        f.write(tex)
