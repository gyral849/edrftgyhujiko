import time
from directschet import gop_stop as gop
def main (terget):
    tic = time.perf_counter()
    res = terget()
    toc = time.perf_counter()
    print(f'resultat= {toc-tic:0.4f}')

if __name__ == '__main__' :
    main(gop)
