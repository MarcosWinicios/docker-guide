[**Voltar ao README**](README.md)

# Conceitos e extratégias de uso do Docker

## Conceitos
### **Docker**
Docker é uma plataforma de código aberto que facilita a criação, o deploy e a execução de aplicações em ambientes isolados chamados containers. Containers são unidades de software que empacotam código e todas as dependências necessárias para a execução de uma aplicação. Diferentemente das máquinas virtuais, containers não possuem um sistema operacional completo, o que os torna mais leves e rápidos.

### **Imagem**
Uma imagem é um pacote de software que contém tudo o que é necessário para executar uma aplicação, incluindo o código, um ambiente de execução e todas as dependências. Imagens são usadas para criar containers.

### **Container**
Um container é uma instância de uma imagem em execução. Containers são isolados uns dos outros e da máquina hospedeira, o que garante que a aplicação rode de forma consistente em diferentes ambientes.

### **Volume**
Volumes são mecanismos de persistência de dados que permitem compartilhar arquivos entre o host e o container. Volumes são usados para armazenar dados que precisam sobreviver ao ciclo de vida do container.

### **Dockerfile**
Um Dockerfile é um arquivo de configuração que contém instruções para a criação de uma imagem. Ele define o ambiente de execução da aplicação, incluindo as dependências necessárias, comandos de inicialização, variáveis de ambiente, entre outros.

### **Docker Compose**
Docker Compose é uma ferramenta que permite definir e executar aplicações multi-container. Com um arquivo de configuração YAML, é possível definir os serviços, redes e volumes necessários para a execução da aplicação.

### **Modo interativo**
O modo interativo permite interagir com o container através do terminal. Para ativar o modo interativo, basta utilizar a opção `-i` no comando `docker container run`.

### **Máquina host**
Máquina host é o computador físico ou virtual que executa o Docker. É a máquina onde os containers são criados e executados.

### ***Registry***
Registry é um serviço que armazena e distribui imagens Docker. O Docker Hub é o registry público padrão, mas é possível configurar registries privados para armazenar imagens internas.

### **Docker hub**
Docker Hub é um serviço de registro de imagens Docker mantido pela Docker, Inc. Ele permite que desenvolvedores compartilhem e distribuam imagens Docker publicamente.

### **Imagens oficiais**
Imagens oficiais são imagens Docker mantidas e suportadas pela comunidade Docker. Elas são verificadas e atualizadas regularmente para garantir a segurança e a qualidade.

### **Imagens pendentes**
Imagens pendentes são imagens Docker que estão sendo baixadas ou construídas. Elas são exibidas no Docker CLI com o status `<pending>`. O tempo de download ou construção depende do tamanho da imagem e da velocidade da conexão.

Este é um exemplo de imagem pendente:
```bash
    REPOSITORY          TAG       IMAGE ID       CREATED         SIZE
    <none>              <none>    1234567890ab   1 minute ago   <pending>
```

Para remover imagens pendentes, basta executar o comando `docker image prune`.

**Atenção:** Este comando irá remover todas as imagens pendentes, incluindo as que estão sendo baixadas no momento.

[**Voltar ao README**](README.md)