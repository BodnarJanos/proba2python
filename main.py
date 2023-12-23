@namespace
class blokkproba:
    # %blockId = blokkprobaxor
    # %block="kizarovagy $a $b"
    # % color=5 weight=100 icon="\uf1ec"
    # % groups=['Led']
    # % a.min=0 a.max=255 a.defl=0
    def kizarovagy(a: number, b: number):
        return a ^ b