# desafio-python

Considerando um capital para investimento de R$2.400.000 e as seguintes opções de
investimento:
Opção          Descrição                            Custo do investimento (R$)   Retorno esperado (R$)  Risco do i
1       Ampliação da capacidade do armazém ZDP em 5%    470.000                    410.000                Baixo
2       Ampliação da capacidade do armazém MGL em 7%    400.000                    330.000                Baixo
3       Compra de empilhadeira                          170.000                    140.000                Médio
4       Projeto de P&D I                                270.000                    250.000                Médio
5       Projeto de P&D II                               340.000                    320.000                Médio
6       Aquisição de novos equipamentos                 230.000                    320.000                Médio
7       Capacitação de funcionários                      50.000                     90.000                Médio
8       Ampliação da estrutura de carga rodoviária      440.000                    190.000                 Alto
9       Construção de datacenter                        320.000                    120.000                 Alto
10      Aquisição de empresa concorrente                800.000                    450.000                 Alto
11      Compra de serviços em nuvem                     120.000                     80.000                Baixo
12      Criação de aplicativo mobile e desktop          150.000                    120.000                Baixo
13      Terceirizar serviço de otimização da logística  300.000                    380.000                Médio

Desenvolva um algoritmo de otimização para selecionar os projetos que maximizam o retorno
total esperado, considerando que:

Pelo menos 1 (um) investimento de risco alto deve ser selecionado;
Pelo menos 2 (dois) investimentos de risco médio devem ser selecionados;
Pelo menos 2 (dois) investimentos de risco baixo devem ser selecionados;

A soma dos custos dos investimentos selecionados, agrupados por categoria de risco,
não deve ultrapassar o teto estipulado para esse categoria, qual seja:
Baixo: R$ 1.200.000
Médio: R$ 1.500.00
Alto: R$ 900.000
Ao final, teste a sua implementação por meio de testes unitários
