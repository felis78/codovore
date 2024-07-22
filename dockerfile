FROM debian:12-slim

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias fr_FR.UTF-8

ENV LANG fr_FR.utf8

RUN apt-get update && apt-get install -y openssh-server curl wget git
RUN mkdir /var/run/sshd
RUN echo 'root:Anapurna01' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN apt-get -y  install build-essential libssl-dev libffi-dev python3-dev\
	&& apt-get install -y python3 python3-pip \
	&& apt-get install -y python3-venv
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash
RUN apt-get update && apt-get install nodejs
RUN wget https://r.mariadb.com/downloads/mariadb_repo_setup \
	&& chmod +x mariadb_repo_setup \
	&& ./mariadb_repo_setup \
	--mariadb-server-version="mariadb-11.5.1" \
	&& apt-get install -y libmariadb3 libmariadb-dev
RUN git config --global user.name "Guillaume ROUCHEUX" \
	&& git config --global user.email guillaume.roucheux@gmail.com

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]