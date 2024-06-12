#!/usr/bin/env bash
if [[ "$1" == "nan" ]]; then
  echo "您的性别是: 男"
fi

if [[ "$1" == "nan" ]]; then
  echo "您的性别是 男"
elif [[ "$1" == "nv" ]]; then
  echo "您的性别是 女"
else
  echo "您的性别，我不知道"
fi



if [[ "$1" == "start" ]]; then
  echo "服务启动中..."
elif [[ "$1" == "stop" ]]; then
  echo "服务关闭中... "
elif [[ "$1" == "restart" ]]; then
  echo "服务重启中..."
else
  echo "$0 脚本的启动方式： $0 [ start | stop | restart ]"
fi



case "$1" in
  "start" )
    echo "服务启动中..."
    ;;
  "stop" )
    echo "服务关闭中..."
    ;;
  "restart" )
    echo "服务重启中..."
    ;;
  *)
    echo "$0 脚本的使用方式：$0 [ start | stop | restart ]"
esac



for i in $(ls .)
do
  echo "${i}"
done


a=1
while [[ "${a}" -lt 5 ]]; do
  echo "${a}"
  a=$((a+1))
done


a=0
until [[ "$a" -eq 5 ]]; do
  a=$((a+1))
  echo "${a}"
done
