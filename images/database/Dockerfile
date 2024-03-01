FROM postgres:16.1
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y 
RUN apt-get install -y openssh-server python3 bash sudo

# copy the startup script to start sshd and postgresql
COPY --chmod=0555 startup.sh /usr/local/bin/startup.sh

# Copy the ssh server keys
COPY ssh_host_* /etc/ssh/
RUN chmod -R go-rwx /etc/ssh

# Allow ansible to sudo -u root ... without a password
RUN echo 'ansible   ALL = NOPASSWD: ALL' >> /etc/sudoers.d/ansible && \
    chmod 0440 /etc/sudoers.d/ansible

# Create the ansible user
RUN useradd --create-home --user-group ansible
USER ansible

# Add the amsible user authorized_keys
RUN  mkdir /home/ansible/.ssh
COPY --chown=ansible:ansible --chmod=0600 authorized_keys /home/ansible/.ssh/authorized_keys
RUN chmod -R og-rwx /home/ansible/.ssh

USER root
ENTRYPOINT [ "/usr/local/bin/startup.sh" ]
