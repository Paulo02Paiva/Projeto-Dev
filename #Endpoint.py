#Endpoint

import flask

#Criando endpoint de rota:

app = Flask(__name__)

@app.route('/links', methods=['GET', 'POST'])
def links():
    if request.method == 'POST':
        # Aqui você pode adicionar o código para salvar o link enviado na sua base de dados
        url = request.form['url']
        title = request.form['title']
        return 'Link adicionado: {} ({})'.format(title, url)
    else:
        # Aqui você pode adicionar o código para recuperar todos os links da sua base de dados e retorná-los como uma lista ou objeto JSON
        return 'Lista de links'

if __name__ == '__main__':
    app.run()
