import subprocess


def build_docker_image():
    try:
        process = subprocess.Popen(
            ["docker","build","-t","my-nginx-html","-f","./Dockerfile","."],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print("Docker image built successfully!")
            print(stdout.decode("utf-8"))
        else:
            print("Error building Docker image:")
            print(stderr.decode("utf-8"))
    except Exception as e:
            print("Unexpected error:",str(e))

if __name__ == "__main__":
     build_docker_image()