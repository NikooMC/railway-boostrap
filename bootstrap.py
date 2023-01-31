import os
import subprocess
import engine


if __name__ == "__main__":
	subprocess.run(["curl", os.environ["SNAPSHOT"], "-o", "snapshot.tar.xz"])
	engine.init(quiet=True)
	subprocess.run(["tar", "xf", "snapshot.tar.xz"])
	engine.log.run_command_live_output("sh server/start.sh")