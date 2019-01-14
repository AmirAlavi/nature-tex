import re


if __name__ == '__main__':
    with open('processed_main.tex', 'r') as f:
        main_tex = f.read()
    with open('tex/naturetex.sty', 'r') as f:
        preamble_tex = ''.join(f.readlines()[1:])
    with open('processed_main.bbl', 'r') as f:
        bib_tex = f.read()
    main_tex = main_tex.replace(r'\usepackage{naturetex}', preamble_tex)
    main_tex = main_tex.replace(r'\bibliography{bibliography}', bib_tex)

    with open('proof_main.tex', 'w') as f:
        f.write(main_tex)
