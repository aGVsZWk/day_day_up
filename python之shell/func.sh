#!/usr/bin/env bash

arg=$1

usage(){
  echo "脚本 $0 的使用方式是： $0 [ start|stop|restart ]"
}

if [[ $# -eq 1 ]]; then
  case ${arg} in
    start)
      echo "服务启动中..."
      ;;
    stop)
      echo "服务关闭中..."
      ;;
    restart)
      echo "服务重启中..."
      ;;
    *)
      usage
      ;;
    esac
fi
