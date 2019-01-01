# Sentry Ansible Role

This role is based on [Sentry docker-compose example](https://github.com/Its-Alex/sentry-docker-example) repository.

This Ansible Role install [Sentry](https://sentry.io) with all its dependencies to work, this Docker Images:

- [`sentry:9.0.0`](https://hub.docker.com/_/sentry/)
- [`postgres:10.4-alpine`](https://hub.docker.com/_/postgres/)
- [`redis:4.0-alpine`](https://hub.docker.com/_/redis/)

Installation is based on [docker-compose.yml](templates/docker-compose.yml) file.

See [Ansible Role Sentry Example](https://github.com/harobed/ansible-role-sentry-example) to understand how to use this role.

See configuration variables in [`defaults/main.yml`](defaults/main.yml) or in [example](https://github.com/harobed/ansible-role-sentry-example/blob/master/inventory/group_vars/all.yml).
