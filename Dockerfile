FROM mongo
COPY mongodb/security.key /data/security.key
RUN chmod 400 /data/security.key && chown 999:999 /data/security.key