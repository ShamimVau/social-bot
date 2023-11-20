from flask import Flask
from threading import Thread
app=Flask("")
@app.route("/")
def main():
    return "<h1>***SERVER RUNNING***</h1>"
Thread(target=app.run,args=("0.0.0.0",8080)).start()
if __name__ == '__main__':
  main ()
