import os
import subprocess
import engine


if __name__ == "__main__":
    subprocess.run(["curl", os.environ["SNAPSHOT"], "-o", "snapshot.tar.xz"])
    os.mkdir("server")
    engine.init(quiet=True)
    subprocess.run(["tar", "xf", "snapshot.tar.xz"])
    with open("server/server.properties", "r") as f:
        prop = f.read()
    with open("server/server.properties", "w") as f:
        f.write(prop.replace("query.port=25565", f"query.port={os.environ['PORT']}"))
    engine.log.run_command_live_output("sh server/start.sh")