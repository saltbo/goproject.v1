# Goproject

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), Goproject is a framework for jumpstarting production-ready go projects quickly.

## Usage

Alternatively, you can install `cookiecutter` with homebrew:
```console
$ brew install cookiecutter
```

Finally, to run it based on this template, type:
```console
$ cookiecutter https://github.com/saltbo/goproject.git
```

You will be asked about your basic info (name, project name, app name, etc.). This info will be used to customize your new project.

Warning: After this point, change 'Luis Morales', 'lacion', etc to your own information.

Answer the prompts with your own desired [options](). For example:
```console
author [saltbo]:
project_name [goproject-test]:
description [A Golang project.]:
use_cobra_cmd [y]:
Select web_framework:
1 - none
2 - github.com/gin-gonic/gin
Choose from 1, 2 [1]: 2
Select orm:
1 - none
2 - github.com/jinzhu/gorm
3 - github.com/go-xorm/xorm
Choose from 1, 2, 3 [1]: 2
Select redis:
1 - none
2 - github.com/go-redis/redis/v7
3 - github.com/go-redis/redis/v6
4 - github.com/go-redis/redis/v5
Choose from 1, 2, 3, 4 [1]: 2
```

Run `make help` to see the available management commands, or just run `make build` to build your project.
```console
$ make
$ make run
```

## Projects build with goproject

- [uptoc](https://github.com/saltbo/uptoc)