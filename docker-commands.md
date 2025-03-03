# Comandos docker

## Sintaxe geral dos comandos Docker:

```bash
  docker <comando> <opções> <argumentos> <imagem>
```

## **Comandos**

### **ps**
Lista os containers em execução.
```bash
    docker ps
```

ou 
```bash
  docker container ps
```

Pode ser combinado com as opções `-a`, `-q`, `-s`, `--no-trunc`, `--latest`. Ver em [Opções comuns](#opções).

### **ls**

```bash
  docker container ls
```

``docker container ls``: Lista os containers em execução.

`docker container ls` é um alias para `docker container ps`.

``docker image ls``: Lista as imagens disponíveis.

``docker network ls``: Lista as redes disponíveis.

``docker volume ls``: Lista os volumes disponíveis.

Pode ser combinado com as opções `-a`, `-q`, `-s`, `--no-trunc`, `--latest`. Ver em [Opções comuns](#opções).

### **run**

```bash
  docker container run <docker-image>
```

O comando ``docker container run`` concatena os seguintes comandos:
1. [`docker image pull`](#pull)
2. [`docker container create`](#create)
3. [`docker container start`](#start)
4. [`docker container exec`](#exec)

Pode ser combinado com as opções `-i`, `-t`, `-it`, `-rm`, `-p`, `-d`, `--name`. Ver em [Opções comuns](#opções).


### **pull**

Baixa uma imagem do registry para a máquina local.

```bash
  docker image pull <docker-image>
```


### **create**
Cria um container a partir de uma imagem.
```bash
  docker container create <docker-image>
```


### **start**
Inicializa um container.
```bash
  docker container start <container-id>
```
Pode ser combinado com as opções `-a`, `-i`, `-d`. Ver em [Opções comuns](#opções).

### **stop**
Para um container em execução.
```bash
  docker container stop <container-id>
```

### **rm**
Remove um container.
```bash
  docker container rm <container-id>
```

### **exec**
Executa um comando em um container em execução.
```bash
  docker container exec <container-id> <comando>
```

## **Opções comuns**

- `-h` | `--help`: Exibe a ajuda do comando.
```bash
  docker --help
```

- `-p` | `--port`: Mapeia uma porta.
```bash 
    -p <porta-host>:<porta-container>
```

- `-v` | `--volume`: Mapeia um volume.
```bash
  -v <caminho-diretorio-host>:<caminho-diretorio-container>
```

- `-i` | `--interactive`: Modo interativo.
```bash
  docker container run -i <container-id>
```

- `-t` | `--tty`: Acesso ao terminal.
```bash
  docker container run -t <container-id>
```

- `-it`: Modo interativo e terminal.
```bash
  docker container run -it <container-id>
```


- `-f` | `--force`: Força a execução do comando.
```bash
  docker container rm -f <container-id>
```

- `-q` | `--quiet`: Exibe apenas o ID do recurso.
```bash
  docker container ls -q
```

- `-l` | `--latest`: Exibe o último recurso criado.
```bash
  docker container ls -l
```

- `-n` | `--no-trunc`: Exibe o nome completo do recurso.
```bash
  docker container ls -n
```

- `-s` | `--size`: Exibe o tamanho do recurso.
```bash
  docker container ls -s
```

- `-a` | `--all`: Exibe todos os recursos.
```bash
  docker container ls -a
```

- `-q` | `--quiet`: Exibe apenas o ID do recurso.
```bash
  docker container ls -q
```

- `-d` | `--detach`: Modo detached.
```bash
  docker container run -d <container-id>
```

- `--name`: Atribui um nome ao container.
```bash
  docker container run --name <nome> <container-id>
```
