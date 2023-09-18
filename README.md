# Projeto de Data Science - Censo da Educação Superior

Este repositório contém código Python para analisar dados do Censo da Educação Superior. Ele é projetado para ajudar na extração e análise de dados relacionados à educação superior no Brasil. O código utiliza as bibliotecas pandas, mysql-connector-python e tkinter.

## Pré-requisitos

Antes de usar este código, certifique-se de ter as seguintes dependências instaladas:

- [Python](https://www.python.org/downloads/) (versão 3.6 ou superior)
- [pip](https://pip.pypa.io/en/stable/installation/)
- Bibliotecas Python: mysql-connector-python, tkinter e pandas.

Você pode instalar as bibliotecas necessárias usando o seguinte comando:

```python
pip install mysql-connector-python tk pandas tqdm
```

## Uso

Siga os passos abaixo para usar este código:

1. Clone este repositório em seu ambiente local:

```bash
git clone [https://github.com/seuusuario/seu-repositorio.git](https://github.com/thanwill/python-datascience.git)
```

2. Navegue para o diretório do projeto


3. Execute o script Python:

```python
python main.py
```


4. O código abrirá uma janela de seleção de arquivo. Selecione o arquivo CSV de dados e o arquivo CSV de IES (Instituições de Ensino Superior) quando solicitado.

5. O código processará os dados e imprimirá as informações relevantes no console.
   


https://github.com/thanwill/python-datascience/assets/62673590/81bbd4c7-64cc-4bbc-91fc-e66017943a31



Lembre-se de que você também precisará configurar as informações de conexão ao banco de dados MySQL no arquivo `main.py` no dicionário `config`:

```bash
config = {
    "user" : "root",
    "password" : "sua-senha",
    "host" : 'localhost',
    "database" : 'seu-banco-de-dados'
}
```
Certifique-se de que o servidor MySQL esteja em execução e acessível.

