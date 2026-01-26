# En el shell (terminal):
# echo 'export NOMBRE="Bryan Glot"' >> ~/.bashrc
# source ~/.bashrc
import os

print(os.environ.get("NOMBRE"))
