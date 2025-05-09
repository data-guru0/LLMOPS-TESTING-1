# 1. Jenkins Setup Commands

```bash
docker build -t jenkins-dind .
````

```bash
docker run -d --name jenkins-dind \
  --privileged \
  -p 8080:8080 -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v jenkins_home:/var/jenkins_home \
  jenkins-dind
```

```bash
docker ps
```

```bash
docker logs jenkins-dind
```

```bash
ip addr show eth0 | grep inet
```

```bash
docker exec -u root -it jenkins-dind bash
apt update -y
apt install -y python3
python3 --version
ln -s /usr/bin/python3 /usr/bin/python
python --version
apt install -y python3-pip
exit
```

```bash
docker restart jenkins-dind
```


# 2. SonarQube Setup Commands

```bash
sysctl -w vm.max_map_count=524288
sysctl -w fs.file-max=131072
ulimit -n 131072
ulimit -u 8192
```

```bash
docker ps
```

```bash
docker restart jenkins-dind
```

```bash
docker network ls
```

```bash
docker network create dind-network
```

```bash
docker network connect dind-network jenkins-dind
```

```bash
docker network connect dind-network sonarqube-dind
```

```bash
-Dsonar.host.url=http://sonarqube-dind:9000
```

# 3. AWS CLI Setup Commands

```bash
docker exec -u root -it jenkins-dind bash
apt update
apt install -y unzip curl
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
./aws/install
aws --version
exit

