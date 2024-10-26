# 使用官方的 Gazebo 镜像作为基础镜像
FROM gazebo:latest

# 安装基础工具和添加软件源的必需工具
RUN apt-get update && \
    apt-get install -y wget gnupg2 lsb-release software-properties-common curl

# 添加 ROS 2 Humble 源
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2-latest.list


# 设置默认命令
CMD ["gazebo"]
