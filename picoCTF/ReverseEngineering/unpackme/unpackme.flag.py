import base64
from cryptography.fernet import Fernet

payload = b'gAAAAABkESVSqaVt_Rr7ZWm8oMyQZzCyuIh-fhOSlYsq0k-3R_sxDK-j90C8avSXKunva5YmnMrRYc8cYBZjckwH5TqfiHYB3msFdywhtxSmoWdGZIwlSyj5n__ftZ24T1zUSy5JPaHFGfVZ0W7KTYa5ACZ0Y58y_q2Xfd0wiQWccYNQNtXpPE8S4RljGq_Vby6TTuqeXxZ_U7IsVmcmdswAwJGMcR61ib9-6GgxjdL3j34RuVW-8lnhmU27_sePRNe7YqWnN_NAxRurE2qya-_lurWZEnVNuQ=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
