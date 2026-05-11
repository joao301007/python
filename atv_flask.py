from flask import Flask


app = Flask(__name__) 

@app.route('/') 
def funcao_flask():
    return 'Decorators em Python são funções especiais que modificam ou aprimoram o comportamento de outras funções ou métodos, adicionando novas funcionalidades sem alterar seu código-fonte original. Eles "envolvem" a função original (wrapper), permitindo executar ações antes ou depois dela, sendo aplicados com a sintaxe' 


if __name__ == '__main__':
    app.run(debug=True) 
