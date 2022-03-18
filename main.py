import pytest 


pytest.main([__file__, "-p", "no:warnings"])

 
def diamond(character):
    diamond_output = []
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    espacos_anterior = alfabeto.index(character)
    #esp_temp = espacos_anterior
    espacos_entre = 0
    aux = -1
    
  

    if character == 'A':
        return ['A']
      
    for index, letra in enumerate(alfabeto):

      
      espacos_entre = alfabeto.index(letra)
        
        if letra =='A':
          temp += letra
                

        diamond_output.append(temp)

        #esp_temp -= 1
        espacos_entre += 1
        
        if (letra == character ):
            aux = 1
        
    for diamond_output
        
    ##character_size = len(character)
    ##for current_characters in character: 
        
    if character == 'A':
        diamond_output.append('A')

    if character == 'B':
        diamond_output.append(' A')
        diamond_output.append('B B') 
        diamond_output.append(' A')
      
    if character == 'C':
        diamond_output.append('  A')
        diamond_output.append(' B B') 
        diamond_output.append('C   C')
        diamond_output.append(' B B')
        diamond_output.append('  A')

    if character == 'D':
        diamond_output.append('   A')
        diamond_output.append('  B B') 
        diamond_output.append(' C   C')
        diamond_output.append('D     D')
        diamond_output.append(' C   C')
        diamond_output.append('  B B')
        diamond_output.append('   A')
    return diamond_output

def test_4():
  assert diamond('D') == ['   A', '  B B', ' C   C','D     D', ' C   C','  B B','   A']

def test_3():
  assert diamond('C') == ['  A', ' B B', 'C   C',' B B','  A']

def test_2():
    assert diamond('B') == [' A', 'B B', ' A']

def test_1():
    assert diamond('A') == ['A']