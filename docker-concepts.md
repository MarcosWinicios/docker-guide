# Conceitos e extratégias de uso do Docker

## Conceitos
### **Docker**
Docker é uma plataforma de código aberto que facilita a criação, o deploy e a execução de aplicações em ambientes isolados chamados containers. Containers são unidades de software que empacotam código e todas as dependências necessárias para a execução de uma aplicação. Diferentemente das máquinas virtuais, containers não possuem um sistema operacional completo, o que os torna mais leves e rápidos.

### **Imagem**
Uma imagem é um pacote de software que contém tudo o que é necessário para executar uma aplicação, incluindo o código, um ambiente de execução e todas as dependências. Imagens são usadas para criar containers.

### **Container**
Um container é uma instância de uma imagem em execução. Containers são isolados uns dos outros e da máquina hospedeira, o que garante que a aplicação rode de forma consistente em diferentes ambientes.

### **Dockerfile**
Um Dockerfile é um arquivo de configuração que contém instruções para a criação de uma imagem. Ele define o ambiente de execução da aplicação, incluindo as dependências necessárias, comandos de inicialização, variáveis de ambiente, entre outros.

### **Docker Compose**
Docker Compose é uma ferramenta que permite definir e executar aplicações multi-container. Com um arquivo de configuração YAML, é possível definir os serviços, redes e volumes necessários para a execução da aplicação.

### **Modo interativo**
O modo interativo permite interagir com o container através do terminal. Para ativar o modo interativo, basta utilizar a opção `-i` no comando `docker container run`.


### **Máquina host**
Máquina host é o computador físico ou virtual que executa o Docker. É a máquina onde os containers são criados e executados.

## Estratégias de uso

### **Reutilização de containers**
Uma das principais vantagens do Docker é a reutilização de containers. Em vez de criar um novo container para cada execução da aplicação, é possível reutilizar o mesmo container várias vezes. Isso reduz o tempo de inicialização e o consumo de recursos.

Para reutilizar um container, basta utilizar o comando [**start**](docker-commands.md#start) em vez de [**run**](docker-commands.md#run).:

### Integrações entre a máquina host e o container

- **Portas**: É possível mapear portas da máquina host para o container, permitindo que a aplicação seja acessível externamente.

sintaxe: `-p <porta-host>:<porta-container>`

```bash
  docker container run -p 8080:80 nginx
```

- **Volumes**: Volumes permitem compartilhar arquivos entre a máquina host e o container. Isso é útil para persistir dados ou compartilhar arquivos de configuração.