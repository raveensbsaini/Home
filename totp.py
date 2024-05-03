import pyotp
import time
import sys
from pathlib import Path

secret_key = Path(sys.argv[1]).read_text().strip() 

totp = pyotp.TOTP(secret_key)
print(totp.now()) # => '492039'
