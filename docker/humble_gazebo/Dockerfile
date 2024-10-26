# 使用 Ubuntu 基础镜像
FROM ubuntu:22.04

# 安装基础工具和添加软件源的必需工具
RUN apt-get update && \
    apt-get install -y wget gnupg2 lsb-release software-properties-common

# 添加 OSRF 的 Gazebo 源
RUN echo "deb [arch=amd64] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/gazebo-stable.list && \
    wget https://packages.osrfoundation.org/gazebo.key -O /usr/share/keyrings/gazebo-archive-keyring.gpg

# 添加 ROS 2 Humble 源
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository universe && \
    add-apt-repository restricted && \
    add-apt-repository multiverse && \
    apt-get install -y curl && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2-latest.list

# 安装 Gazebo 和 ROS 相关的依赖包
RUN apt-get update && \
    apt-get install -y \
    gazebo11 \
    ros-humble-gazebo-ros-pkgs && \
    rm -rf /var/lib/apt/lists/*

# 设置默认命令
CMD ["gazebo"]
