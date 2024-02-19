import sys
import os

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__)) #表示当前路径
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #表示上一级目录
sys.path.insert(0,BASE_DIR+"/keywords")  #也可以用os.path.join(BASE_DIR,'/keywords')
