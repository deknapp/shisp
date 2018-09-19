import os 
import stat

st = os.stat('sampler')
os.chmod('sampler', st.st_mode | stat.S_IEXEC)
