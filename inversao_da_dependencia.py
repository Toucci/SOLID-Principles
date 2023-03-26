#Solid(D) - Principio da Inversão da Dependência

"""
O princípio SOLID de Inversão da Dependência (DIP) diz que é melhor depender de abstrações
 (ideias gerais) do que de coisas específicas. Isso significa que, ao escrever código, é melhor 
 depender de interfaces ou classes abstratas em vez de depender diretamente de outras classes ou 
 funções. Isso torna o código mais flexível e fácil de manter a longo prazo, porque, se precisar 
 mudar algo no futuro, você pode fazer isso sem afetar outras partes do seu código.


me dê um exemplo de uma classe abstrata
Classe abstrata é uma classe que não pode ser instanciada diretamente, mas é usada
como um modelo para outras classes. Ela é declarada com a palavra-chave "abstract" e pode conter
métodos abstratos (que não têm implementação) e métodos concretos (que têm implementação).

Por exemplo, imagine que estamos criando um sistema de pagamento que suporta diferentes
tipos de cartões de crédito. Podemos ter uma classe abstrata chamada "CartaoDeCredito" que define os 
métodos básicos que todos os cartões de crédito têm em comum, como "validar()" e
"processarPagamento()". Em seguida, podemos criar classes concretas para cada tipo de cartão de 
crédito, como "MasterCard", "Visa" e "American Express", que herdam da classe abstrata 
"CartaoDeCredito" e implementam seus próprios métodos específicos.

Dessa forma, podemos usar a classe abstrata "CartaoDeCredito" como um modelo para criar diferentes 
tipos de cartões de crédito, mantendo a consistência dos métodos em comum. E, se precisarmos 
adicionar ou alterar algum método comum a todos os cartões de crédito, podemos fazê-lo na
 classe abstrata, sem precisar alterar cada classe concreta individualmente.

"""