from time import sleep
from datetime import date

#INTRODUÇÃO DE CABEÇALHO
sleep(1)
print('\n')
print('-=' *31 )
data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')
print('PROTÓTIPO SIMPLIFICADO DE CONSULTA JURÍDICA, RIO, {}.'.format(data_em_texto))
print('-=' *31 )

#INTRODUÇÃO DIDÁTICA
sleep(2)
print('\n')
print('============ TERMINAL INTERATIVO ============')
sleep(1)
print('\n====== CONSTITUIÇÃO FEDERAL - ARTIGO 5º  ======')
sleep(2)
print('\n<<< ATENÇÃO >>> \n\nO CONTEÚDO AQUI DISPOSTO RESUME E \nEXPLICA DIDATICAMENTE O TEXTO ORIGINAL.\n')
sleep(1)
print('-=' * 22)
print('\nAvaliação e revisão retirada de "Direito \nconstitucional descomplicado":')
sleep(1)
print('16 ed. rev., atual. e ampl. Rio de Janeiro: \nForense; São Paulo: Método, 2017.')
sleep(1)
print('\n\npor PAULO, V.; ALEXANDRINO, M.')
sleep(1)
print('-=' * 22)
sleep(2)

#MENU DE CONSULTA
print('\n<<<< Referente a disposição dos artigos e incisos, escolha o conteúdo. >>>>\n')
sleep(3)
print('''Leia sobre:\n
[   0   ] DEFINIÇÃO DO ARTIGO 5º 
[   1   ] INCISO I
[   2   ] INCISO II
[   3   ] INCISO III
[   4   ] INCISO IV
[   5   ] INCISO V
[   6   ] INCISO VI
[   7   ] INCISO VII
[   8   ] INCISO VIII

[   9   ] FAZER UMA AVALIAÇÃO DESTA APLICAÇÃO
''')
sleep(1)
menu = int(input('>>> SUA ESCOLHA: '))
print('-=' * 22)
sleep(1)

#RETORNANDO CONSULTA

if menu == 0:
    print('''    Todos são iguais perante a lei, sem distinção de qualquer natureza, 
      garantindo-se aos brasileiros e aos estrangeiros residentes no País a 
      inviolabilidade do direito à vida, à liberdade, à igualdade, à segurança e à 
      propriedade, nos termos seguintes:
    
      A despeito da literalidade do artigo, que indica serem os direitos fundamentais 
      destinados apenas aos brasileiros e aos estrangeiros residentes no país, Paulo e
      Alexandrino (2017) indicam que o entendimento majoritário é o de que estrangeiros
      não residentes também fazem jus aos direitos em questão.
    
      O caput enumera cinco direitos fundamentais como ponto de partida. A doutrina entende
      que desses direitos decorrem os que seguem, constantes dos incisos do artigo. Sobre o 
      direito à vida e à igualdade vale fazer algumas observações.
    
    VIDA
    
      Antes de mais nada, cabe ressaltar que o direito à vida não é absoluto. Muitas questões de
      concurso levam o candidato a afirmar o contrário a respeito desse direito fundamental. 
      A própria CF prevê, porém, a possibilidade de que o Estado tire a vida de um indivíduo por 
      ter praticado crime militar em caso de guerra declarada em outro inciso do Art. 5º. Veja:
    
      XLVII - não haverá penas:
    
      A de morte, salvo em caso de guerra declarada, nos termos do art. 84, XIX;
    
      A morte, nesse caso, deverá ser levada a cabo por fuzilamento. Pelo princípio da vedação 
      ao retrocesso, impede-se que sejam criadas novas hipóteses de pena de morte no país. Isso 
      se reflete nas obrigações com as quais o Brasil se comprometeu por meio de tratados também. 
      Não se esqueça dessa exceção!
    
      Ainda sobre o direito à vida, alguns detalhes muito cobrados em provas:
    
      O direito à vida compreende a existência intrauterina e extrauterina. As hipóteses de aborto
      são apenas aquelas sobre as quais o legislador expressamente se manifestou. O feto anencéfalo é 
      considerado biologicamente vivo, mas juridicamente morto, segundo o STF, por ser inviável. Dessa 
      forma, é possível interromper a gravidez também nessa hipótese. Para saber mais a respeito, pesquise 
      o teor da decisão prolatada nos autos da ADPF 54;
     
      Há uma dupla acepção do direito à vida que deve ser considerada: o direito de permanecer vivo importa
      tanto quanto o direito de ter uma vida digna. O Estado deve envidar esforços para garantir a todos uma 
      existência pautada na dignidade da pessoa humana, que a maioria da doutrina considera como o valor central 
      do ordenamento jurídico brasileiro e está prevista no Art. 1º, III, CF.
      
    IGUALDADE
      
      É necessário entender a igualdade também sob um viés duplo. A igualdade formal diz respeito à equiparação de 
      todas as pessoas no que diz respeito aos direitos e garantias.
      
      A igualdade material diz respeito a entender que certos grupos de pessoas, por motivos históricos, sociais e 
      econômicos não têm acesso aos direitos da mesma forma que as demais. O legislador não pode ignorar essas 
      disparidades enraizadas na sociedade brasileira, devendo prever, sempre de maneira razoável, condições diferentes
      a fim de nivelar minimamente as condições de vida dessas minorias em relação às gozadas pelas demais pessoas.
      
      O direito à igualdade deve pautar a conduta do legislador, que não pode criar hipóteses que tragam tratamento 
      diverso a quem está em igualdade de condições - a chamada igualdade na lei. Também deve ser objetivo do aplicador
      do direito concretizar o direito em questão, privilegiando a interpretação das normas de forma a não criar 
      situação anti-isonômica no caso concreto. Nesse último caso, estamos diante da obrigação de observar a igualdade
      perante a lei.
      
      Sobre o tema, é importante levar em conta os precedentes do STF que consideram constitucionais as cotas raciais 
      em concursos públicos e vestibulares (ADC 41 e RE 597.285); o programa que concede bolsas para cursos de graduação
      em universidades privadas, visando à diminuição da desigualdade social no país (ADI 3.330) e critérios de 
      diferença de idade para fins de inscrição em concurso público (Súmula 683).
    
    ''')
elif menu == 1:
    print('''  INCISO I - Homens e mulheres são iguais em direitos e obrigações, nos termos desta Constituição;
    
       A igualdade é um dos pilares do ordenamento jurídico brasileiro. Como visto acima, a igualdade deve ser alcançada
       a partir da conjugação das duas acepções - a formal e a material. Dessa forma, a ressalva inscrita no inciso "nos 
       termos desta Constituição" faz referência a direitos e deveres previstos de forma diferente para cada qual dos 
       diversos grupos que compõem a sociedade brasileira. Cite-se como exemplo o tratamento distinto previsto no próprio
       texto constitucional, a respeito da necessidade de incentivar a integração da mulher ao mercado de trabalho, como
       disposto no Art. 7º, XX.
    ''')
elif menu == 2:
    print('''   INCISO II - Ninguém será obrigado a fazer ou deixar de fazer alguma coisa senão em virtude de lei;
    
       Aqui faz-se menção ao princípio da legalidade. Segundo esse princípio, é dado ao particular fazer tudo o que não 
       estiver expressamente proibido pela lei. A doutrina afirma, portanto, que o particular pode agir para além da lei 
       (praeter legem) e segundo a lei (secundum legem). Ao Estado, porém, não é possível agir de maneira diferente da que
       o legislador impõe, devendo pautar sua conduta segundo a lei.
    
       O respeito à lei imposto ao Estado deve ser entendido como o respeito ao ordenamento jurídico como um todo. 
       No âmbito do Direito Administrativo, conclui-se que o alargamento decorrente desse entendimento restringe bastante
       a atuação da Administração.
    
       Decorrem do princípio da legalidade outros dois: o princípio da anterioridade e o princípio da reserva legal.
    
       O primeiro dos referidos corolários define que as condutas sociais devem ser pautadas por leis previamente 
       existentes no ordenamento jurídico. É estudado com mais profundidade no âmbito do Direito Penal. Existem diversas
       exceções a esse princípio, notadamente as que dizem respeito à retroatividade da lei penal mais benéfica para o réu,
       prevista no inciso do Art. 5º, XL, CF. A Lindb, entre outras normas, trata de aspectos relativos à aplicação das 
       leis no tempo.
    
       O princípio da reserva legal impõe que algumas matérias só podem ser regulamentadas por meio de lei formal, 
       excluindo-se qualquer outra espécie de norma. O processo legislativo compreende regras específicas, que devem 
       ser observadas para que a lei que dele resulte produza regularmente seus efeitos. A lei que não segue o rito deve
       ser considerada formalmente inconstitucional, vício também conhecido como inconstitucionalidade nomodinâmica.
    
       Essas regras, que variam de acordo com a espécie de norma editada, foram estabelecidas com o objetivo de garantir 
       que as normas resultantes desse processo de fato reflitam a vontade da população, externada pelos parlamentares 
       eleitos pelo povo. Algumas matérias são consideradas importantes demais para prescindirem desse procedimento, 
       motivo pelo qual se sujeitam à reserva legal.
    
       A doutrina diferencia a reserva legal qualificada da simples. Na primeira hipótese, exige-se que se defina 
       previamente o conteúdo da lei e a finalidade específica do ato. O segundo caso diz respeito à mera obrigatoriedade 
       de que a norma regulamentadora seja lei formal, sem que se estabeleça seu conteúdo ou sua finalidade.
    ''')
elif menu == 3:
    print('''  INCISO III - Ninguém será submetido a tortura nem a tratamento desumano ou degradante; 
    
       A literalidade do inciso já passa a ideia completa do dispositivo. Não seria possível que o Estado Brasileiro 
       deixasse de se comprometer com o combate a tais práticas, o que faz criminalizando tais condutas e atuando para 
       impedir que elas ocorram.
    ''')
elif menu == 4:
    print('''   INCISO IV - É livre a manifestação do pensamento, sendo vedado o anonimato;
    
       Aqui o constituinte consagrou o direito à liberdade de expressão. Lembre-se bem da parte final do inciso, que 
       demonstra que as opiniões expressas sem identificação do emissor da mensagem não estão compreendidas entre as 
       manifestações protegidas pelo direito em questão. A vedação ao anonimato aparece em muitas questões de Direito 
       Constitucional.
    
       O Supremo, ao julgar o HC 82.424, tornou evidente que a liberdade de expressão não abrange o discurso de ódio, 
       postulando que o direito fundamental à livre manifestação do pensamento não pode ser meio para a prática de crimes 
       previstos no ordenamento.
    
       Sobre o tema, é importante destacar ainda que a liberdade de expressão não exime o emissor da mensagem de indenizar
       quem quer que tenha sido lesado com o que foi dito. A busca pela reparação deverá ser feita de acordo com o que 
       dispõe a lei.
    ''')
elif menu == 5:
    print(''' INCISO V - É assegurado o direito de resposta, proporcional ao agravo, além da indenização por dano 
    material, moral ou à imagem; 
     
        O direito de resposta previsto nesse inciso exige que se verifique no caso concreto que a ofensa foi repelida pelo
        ofendido pelo mesmo meio de comunicação, tamanho ou duração, sendo necessário que seja dado o mesmo destaque que 
        teve a ofensa.
     
        A compensação por dano material, moral ou à imagem foi trazida pelo constituinte de forma independente do direito 
        de resposta. Não há motivo para dúvida: se a questão mencionar uma suposta necessidade de exercer o direito de 
        resposta para buscar indenização por uma ofensa, ou, em sentido diverso, indicar que quem exerce o direito de 
        resposta fica impossibilitado de buscar reparação pelo dano sofrido por outras vias, é sinal de que a banca do 
        seu concurso está subvertendo a disposição do inciso V. Essa dica é para nunca mais errar!
    ''')
elif menu == 6:
    print('''   INCISO VI - É inviolável a liberdade de consciência e de crença, sendo assegurado o livre exercício dos 
    cultos religiosos e garantida, na forma da lei, a proteção aos locais de culto e a suas liturgias.
    ''')
elif menu == 7:
    print('''   INCISO VII - É assegurada, nos termos da lei, a prestação de assistência religiosa nas entidades civis 
    e militares de internação coletiva;
    ''')
elif menu == 8:
    print('''  INCISO VIII - Ninguém será privado de direitos por motivo de crença religiosa ou de convicção filosófica 
    ou política, salvo se as invocar para eximir-se de obrigação legal a todos imposta e recusar-se a cumprir prestação 
    alternativa, fixada em lei; 
    
       Sobre a liberdade de crença, o constituinte considerou muito importante explicitar a forma como deve ser garantido 
       o exercício de tal prerrogativa fundamental. A importância dada à liberdade religiosa é tamanha que é o fundamento 
       para a imunidade tributária concedida aos templos de qualquer culto, presente no Art. 150, VI, "b" da CF.
    
       Art. 150. Sem prejuízo de outras garantias asseguradas ao contribuinte, é vedado à União, aos Estados, ao Distrito 
       Federal e aos Municípios:
    
       Instituir impostos sobre:
       Templos de qualquer culto;
    
       A prestação de assistência religiosa a que faz referência o inciso VII é de caráter privado. Não confunda o 
       compromisso do Estado de garantir o acesso à assistência religiosa com a assunção de uma responsabilidade por parte 
       do Estado de oferecê-la por meio da atuação de seus órgãos e agentes. Considere a disposição constitucional a seguir
       e perceba que uma interpretação nesse sentido não seria compatível com o que a Carta da República estabelece.
    
       Art. 19. É vedado à União, aos Estados, ao Distrito Federal e aos Municípios:
    
       Estabelecer cultos religiosos ou igrejas, subvencioná-los, embaraçar-lhes o funcionamento ou manter com eles ou 
       seus representantes relações de dependência ou aliança, ressalvada, na forma da lei, a colaboração de interesse 
       público;
    
       O inciso VIII trata da escusa de consciência. Assim, ninguém deve ser submetido a cumprir uma obrigação legal que 
       vá de encontro as suas convicções religiosas, morais ou filosóficas. Porém, se a lei previr uma obrigação 
       alternativa a ser exigida nesses casos, deixar de cumpri-la poderá acarretar privação de direitos.
    
       Perceba que se trata de norma de eficácia contida: enquanto o legislador não regular a hipótese, prevendo as 
       mencionadas obrigações alternativas, não poderá restringir qualquer direito de quem se declarar impossibilitado 
       de cumprir com obrigação imposta a todos.
    ''')
elif menu == 9:
    sleep(2)
    av = int(input('Digite uma nota de 0 a 10 para esta aplicação: '))
    sleep(1)
    comment = str(input('Deixe seu comentário ou tecle ENTER para continuar: '))
    sleep(1)
    print('Obrigado por utilizar nosso protótipo, sua avaliação {} foi computada com sucesso.\nMuito obrigado!'.format(av))
else:
    print('Opção inválida')
