# Jellyfin media server

This the config for a self hosted media server which can be used even without internet connection if the person is on the LAN network.

## Instructions

- Step 1:
  change the directory to the jellyfin dir

```
cd ./jellyfin
```

- Step 2(optional):
  add folders for your server and put the path on the docker-compose.yaml in this way

```
- type: bind
  source: /path/to/the/dir/you/wanna/share
  target: /folder-name

- type: bind
  source: /path/to/the/2nd/dir/you/wanna/share
  target: /2nd-folder-name

```

- Step 3:
  add user and group id

```
user: <user_id>:<group_id>
```

- Step 4:
  start the container

```
docker compose up -d
```

**And that's it your server is live now**
**Setup and upload files to it as per your desire**

- Step 5:
  You can access the server on the localhost:8096 or if you can access it with another device the <ip_address>:8096
