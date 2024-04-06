FROM debian
######################################## Debian-with-python3.11.4 ####################################################

# 安装编译工具和依赖项
RUN echo "deb http://mirrors.aliyun.com/debian stable main contrib non-free" > /etc/apt/sources.list && echo "deb http://mirrors.aliyun.com/debian stable-updates main contrib non-free" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libgdbm-dev \
    libdb5.3-dev \
    libbz2-dev \
    libexpat1-dev \
    liblzma-dev \
    tk-dev \
    wget

WORKDIR /app

# 下载并解压 Python 源代码
COPY ./Python-3.11.4.tgz /app/
RUN tar xzvf Python-3.11.4.tgz && rm -f Python-3.11.4.tgz

# 编译 Python
WORKDIR /app/Python-3.11.4
RUN ./configure --enable-optimizations && make && make install

# 设置 Python 环境变量
ENV PATH=/usr/local/bin:$PATH

# 设置pip源
RUN mkdir ~/.pip
RUN cat <<'EOF' > ~/.pip/pip.conf
[global] 
index-url=https://pypi.tuna.tsinghua.edu.cn/simple/
#proxy = [user:passwd@]proxy.server:port \
[install]
trusted-host=
        pypi.tuna.tsinghua.edu.cn
        pypi.douban.com
        mirrors.aliyun.com
ssl_verify: false
EOF
RUN pip3 install --upgrade pip && rm -rf /app/Python-3.11.4
