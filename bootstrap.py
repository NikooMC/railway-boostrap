import os
import subprocess
import engine
from pyngrok import conf, ngrok

if __name__ == "__main__":
    try:
        os.mkdir("server")
        subprocess.run(["curl", os.environ["SNAPSHOT"], "-o", "snapshot.tar.xz"])
    except FileExistsError:
        pass
    engine.init(quiet=True)
    os.chdir("server")
    subprocess.run(["tar", "xf", "../snapshot.tar.xz"])
    engine.log.run_command_live_output("cat server/server.properties")
    engine.log.run_command_live_output(f"ngrok authtoken {os.environ['NGROK']}")
    os.system("killall ngrok")
    url = ngrok.connect(25565, 'tcp')
    print('Your server address is ' + ((str(url).split('"')[1::2])[0]).replace('tcp://', ''))
    os.chdir("..")
    engine.log.run_command_live_output("sh server/start.sh")
    with open("server/eula.txt", "r") as f:
        content = f.read()
    with open("server/eula.txt", "w") as f:
        f.write(content.replace("eula=false", "eula=true"))
    engine.log.run_command_live_output("sh server/start.sh")