import sys
import subprocess
songName = "epic study playlist"
result = subprocess.check_output(["mpc", "find", "any", songName])
first_result = result.split('\n')[0]  
subprocess.call(["mpc", "clear", "--wait"])
find_add_query = "yt:https://www.youtube.com/watch?v=" + first_result[-11:]
subprocess.call(["mpc", "insert", find_add_query])  
subprocess.call(["mpc", "volume", "4"])
subprocess.call(["mpc", "play"])

mood = sys.argv[1]
if "relax" in mood:
  subprocess.call(["mpc", "insert", find_add_query])  
