# Docker compose

Docker compose é uma ferramenta para definir e executar aplicativos Docker multi-container. Com o Docker Composer, você usa um arquivo YAML para configurar seus serviços. Em seguida, com um único comando, você cria e inicia todos os serviços a partir de sua configuração.

# Conceitos
- **Version**: Versão do docker-compose.yml. Define quais funcionalidades estão disponíveis. Deve ser a primeira linha do arquivo.
- **Volumes**: Cria um volume nomeado para armazenar dados. É uma forma de persistir dados entre containers.
  - Os volumes não são restritos a nehum serviço, ou seja, qualquer serviço pode acessar um volume.
  - Eles são criados na máquina host e não são removidos quando o container é removido.
  - Ao mapear um volume, o Docker cria um diretório na máquina host com o mesmo nome do volume. Sendo esse diretório um espelho do diretório do container.
  - Ser um espelho significa que qualquer alteração feita em um diretório será refletida no outro.
  - Para saber onde o volume foi criado, execute o comando `docker volume inspect {volume_name}`. O caminho estará na propriedade `Mountpoint`.
- **Services**: São os containers que compõem a aplicação. Cada serviço é uma imagem Docker que será executada.
    - **container_name**: Nome do container. Equivalente ao comando `docker run --name`.
    - **image**: Imagem Docker que será utilizada para criar o container do serviço. Equivalente ao comando `docker run`.
    - **ports**: Mapeia uma porta do host para uma porta do container. Equivalente ao comando `docker run -p`.
    - **environment**: Define variáveis de ambiente. Equivalente ao comando `docker run -e`.
    - **depends_on**: Define dependências entre serviços. O serviço dependente só será iniciado após o serviço de que depende.
    - **networks**: Define a rede que o container fará parte. Equivalente ao comando `docker network connect`.
    - **restart**: Define a política de reinicialização do container. Valores possíveis: 
      - `no`: nunca
      - `always`: sempre
      - `on-failure`: apenas em caso de falha
      - `unless-stopped`: a menos que seja parado manualmente
    - **command**: Comando que será executado ao iniciar o container. Equivalente ao comando `docker run`.
    - **volumes**: Mapeia um volume para o container.
      - **volumes nomeados:** `{volume_name}:{container_path}`: Mapeia um volume declarado fora do serviço para o container.
        - São gerenciados pelo Dcoker, sendo acesssíveis pelo comando `docker volume`.
      - **Volumes anônimos(Bind Mount):** `{host_path}:{container_path}`: Mapeia um diretório do host para o container.
        - Não são gerenciados pelo Docker, não são acessíveis pelo comando `docker volume`.
        - Ideal apenas para arquivos de configuração ou scripts.
    - working_dir: Define o diretório de trabalho do container. Equivalente ao comando `docker run -w`.
    - depends_on: Define a ordem de inicialização dos serviços. O serviço dependente só será iniciado após o serviço de que depende.
    - build: Define o caminho do Dockerfile para construir a imagem do serviço.
# Docker composer override
O Docker Compose permite que você use vários arquivos de configuração para definir seus serviços. Isso é útil para criar diferentes ambientes (desenvolvimento, teste, produção) com base na mesma configuração.

Uma possibilidade é usar o arquivo `docker-compose.override.yml`. Esse arquivo é carregado automaticamente pelo Docker Compose e pode ser usado para substituir ou adicionar configurações ao arquivo principal `docker-compose.yml`.

# Comandos

- **`docker compose up`**: Cria e inicia os containers. Deve ser executado na pasta onde está o arquivo docker-compose.yml.
    - **`-d`**: Executa os containers em segundo plano (detached mode).
    - **`--build`**: Força a reconstrução das imagens.
    - **`--force-recreate`**: Força a recriação dos containers, mesmo que não haja alterações.
    - **`--remove-orphans`**: Remove containers que não estão definidos no arquivo docker-compose.yml.
    - **`--scale`**: Escala um serviço para o número de instâncias desejadas.
    - **`--no-deps`**: Não inicia os serviços dependentes.
    - **`--no-recreate`**: Não recria os containers, mesmo que haja alterações.
    - **`--abort-on-container-exit`**: Para todos os containers se um deles parar.
    - **`--timeout`**: Define o tempo limite para parar os containers.

```bash
  docker compose up -d --scale web=3
```
- **`docker compose down`**: Para e remove os containers.
- **`docker compose start`**: Inicia os containers.
- **`docker compose stop`**: Para os containers.
- **`docker compose ps`**: Lista os containers.
- **`docker compose logs`**: Exibe os logs dos containers.
  - `-f`: Exibe os logs em tempo real.
  - `-t`: Exibe o timestamp.
  - **Obs.:** Se não for passado o nome do serviço, exibe os logs de todos os serviços.
```bash
  docker compose logs -f -t
```
- **`docker compose top`**: Exibe os processos rodando nos containers.
- **`docker compose exec`**: Executa um comando dentro de um container.

## Configurando serviço de imagem personalizada

Serviços de imagem personalizadas, são serviços que utilizam um Dockerfile para criar a imagem do serviço. Para isso, é necessário adicionar a propriedade `build` no serviço desejado.

```yaml
  worker:
    build: worker
    volumes:
      # Worker
      - ./worker:/worker
    working_dir: /worker
    command: worker.py
    networks:
      - fila
    depends_on:
      - queue
```