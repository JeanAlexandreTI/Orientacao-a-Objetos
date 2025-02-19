# Projeto: Sistema de Biblioteca Simples

# Enunciado:
# Crie um sistema simples de biblioteca que permita adicionar livros, registrar usuários e fazer empréstimos.
# O sistema deve ser estruturado em classes, com os principais conceitos da Orientação a Objetos (OO) sendo 
# aplicados para permitir uma melhor organização do código e facilitar a compreensão de seus pilares.

# O sistema deve contar com as seguintes funcionalidades básicas:

# Cadastro de livros – Permite que um livro seja adicionado ao acervo.
# Cadastro de usuários – Registra os usuários que poderão pegar livros emprestados.
# Empréstimo de livros – Registra os livros emprestados para um usuário, com verificação de disponibilidade.
# Devolução de livros – Marca o livro como devolvido.
# Durante o desenvolvimento desse sistema, a aplicação de Encapsulamento, Herança, Polimorfismo e Abstração 
# deve ser clara e aplicada corretamente.

# Explicação dos Pilares de Orientação a Objetos
# Encapsulamento

# Definição: O encapsulamento refere-se ao processo de esconder os detalhes internos de implementação de uma classe,
# permitindo que apenas os métodos públicos (interface da classe) sejam acessados. Isso ajuda a proteger o estado do
# objeto de alterações indesejadas e proporciona maior controle sobre a manipulação de seus dados.

# Aplicação prática: Em nosso sistema de biblioteca, podemos aplicar o encapsulamento para garantir que informações
# como o status de um livro (disponível ou emprestado) não sejam modificadas diretamente, mas sim através de métodos
# específicos. Por exemplo, ao invés de permitir que o status de um livro seja alterado diretamente, podemos criar
# métodos como emprestar() e devolver(), que controlam como esse status é alterado.

# Exemplo de cenário: Ao adicionar um livro, a classe Livro pode ter um atributo privado status, que armazena se o
# livro está disponível ou emprestado. Esse atributo não pode ser acessado diretamente fora da classe. Para mudar o
# status do livro, um método público chamado alterar_status() seria utilizado.

# Herança

# Definição: Herança permite que uma classe (subclasse) herde comportamentos (métodos e atributos) de outra classe
# (superclasse). Isso promove reutilização de código e facilita a criação de hierarquias de objetos.

# Aplicação prática: Em nosso sistema de biblioteca, podemos ter uma classe Pessoa que define os atributos e
# comportamentos comuns de um usuário e de um funcionário. A partir da classe Pessoa, podemos criar subclasses como
# Usuario e Funcionario, que herdam os atributos e métodos da classe Pessoa, mas com comportamentos específicos, como
# a possibilidade de um funcionário adicionar novos livros ao sistema.

# Exemplo de cenário: A classe Pessoa poderia ter os atributos nome e email. As classes Usuario e Funcionario herdam
# esses atributos e ainda podem ter seus próprios atributos e métodos, como Usuario ter o método emprestar_livro() e
# Funcionario ter o método adicionar_livro().

# Polimorfismo

# Definição: Polimorfismo é o conceito que permite que diferentes classes respondam de maneira diferente ao mesmo método
# ou operação. Em outras palavras, o polimorfismo permite que objetos de tipos diferentes possam ser manipulados de
# forma uniforme, mesmo que os comportamentos internos desses objetos sejam diferentes.

# Aplicação prática: No sistema de biblioteca, podemos usar polimorfismo para garantir que, apesar de termos diferentes
# tipos de pessoas (usuário e funcionário), ambos possam realizar operações como realizar_emprestimo() ou
# realizar_devolucao(), mas com comportamentos adaptados às suas funções. A classe Usuario pode ter uma forma de
# empréstimo diferente de um Funcionario.

# Exemplo de cenário: A classe Pessoa pode ter um método genérico chamado realizar_emprestimo(). No entanto, a
# implementação desse método pode ser diferente em cada subclasse (como Usuario e Funcionario). O usuário só pode pegar
# um livro emprestado, enquanto o funcionário pode registrar novos livros e também emprestar livros.

# Abstração

# Definição: A abstração é o processo de ocultar os detalhes complexos e mostrar apenas a interface necessária para o
# usuário. Em outras palavras, abstração é a simplificação de um sistema complexo para uma interface simples e
# compreensível, sem revelar sua implementação interna.

# Aplicação prática: Para aplicar abstração em nosso sistema de biblioteca, podemos ter uma classe abstrata Pessoa que
# define os métodos comuns de qualquer pessoa (como cadastrar() ou atualizar_dados()), mas sem fornecer uma implementação
# detalhada desses métodos. As subclasses como Usuario e Funcionario fornecerão a implementação real desses métodos, de
# acordo com as necessidades específicas de cada tipo de pessoa.

# Exemplo de cenário: Criar uma classe Cadastro que forneça uma interface simples para cadastrar um livro ou usuário, mas
# a implementação real de como o cadastro acontece pode ser diferente entre as classes Funcionario e Usuario. A classe
# abstrata garante que ambos sigam um mesmo padrão de cadastro, mas cada um faz isso de uma forma específica.
# %%