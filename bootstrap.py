import os
import subprocess
import engine
from pyngrok import conf, ngrok

if __name__ == "__main__":
    subprocess.run(["curl", os.environ["SNAPSHOT"], "-o", "snapshot.tar.xz"])
    os.mkdir("server")
    engine.init(quiet=True)
    os.chdir("server")
    subprocess.run(["tar", "xf", "../snapshot.tar.xz"])
    engine.log.run_command_live_output("cat server/server.properties")
    engine.log.run_command_live_output(f"ngrok authtoken {os.environ['NGROK']}")
    url = ngrok.connect(25565, 'tcp')
    print('Your server address is ' + ((str(url).split('"')[1::2])[0]).replace('tcp://', ''))
    os.chdir("..")
    engine.log.run_command_live_output("sh server/start.sh")