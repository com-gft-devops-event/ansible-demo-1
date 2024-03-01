FROM alpine:3.19

RUN apk --update add \
      bash \
      bind-tools \
      binutils \
      coreutils \
      curl \
      docker \
      findutils \
      git \
      grep \
      jq \
      openssh-client \
      openssh-server \
      pipx \
      postgresql16-client \
      procps \
      py3-pip \
      python3 \
      strace \
      sudo \
      util-linux \
      vim \
      wget \
      xmlstarlet \
      yq

RUN echo 'ansible   ALL = NOPASSWD: ALL' >> /etc/sudoers.d/ansible && \
    chmod 0440 /etc/sudoers.d/ansible

RUN adduser -D ansible && \
    addgroup ansible ping
USER ansible
WORKDIR /home/ansible
# instruction missing uppercase
# env PATH="/home/ansible/.local/bin:$PATH"  
ENV PATH="/home/ansible/.local/bin:$PATH"

RUN mkdir /home/ansible/.ssh
RUN chmod og-rwx /home/ansible/.ssh
COPY --chown=ansible:ansible --chmod=600 id_rsa /home/ansible/.ssh/id_rsa
COPY --chown=ansible:ansible --chmod=600 id_rsa.pub /home/ansible/.ssh/id_rsa.pub
COPY --chown=ansible:ansible demo/ /home/ansible/

RUN find /home/ansible/ -type f -exec chmod a-x {} \; && \
    chmod -R o-rwx,g-w /home/ansible/ && \
    find /home/ansible -type f \( -name "*.py" -o -name "*.sh" \) -exec chmod a+rx {} \;

RUN pipx install ansible-core

