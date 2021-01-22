
def turing_M (state = None, #estados de la maquina de turing
              blank = None, #simbolo blanco de el alfabeto dela cinta
              rules = [],   #reglas de transicion
              tape = [],    #cinta
              final = None,  #estado valido y/o final
              pos = 0):#posicion siguiente de la maquina de turing

   #se verifica que la cinta no este vacía
    st = state
    if not tape: 
        tape = [blank]   
    if pos <0 : pos += len(tape)
    if pos >= len(tape) or pos < 0 : raise Error ("Se inicializa mal la posicion")

     #Declaramos la estructura de las reglas por medio de un dicccionario de datos:
    #s0 = stado inicial, v0 = símbolo inicial, v1 = simbolo escrito, dr = la dirección o movimiento s1 = estado  siguiente, 
    # for -Repetir desde la primera regla, hasta la última en Rules    
    rules = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in rules) 
   
    while True: #leer las reglas y la cinta
        print (st, '\t', end=" ")
        for i, v in enumerate(tape):
             if i==pos: print ("[%s]"%(v,),end=" ")
             else: print (v, end=" ")    
        print()
        
        if st == final: 
            print('Llegó a la aceptacion')#cuando no llega en el estado de aceptacion
            break
        if (st, tape[pos]) not in rules: 
            break
        
        (v1,dr,s1) = rules [(st, tape[pos])]
        tape[pos]=v1 #rescribe el simbolo de la cinta
    
    #movimiento del cabezal
        if dr == 'left':
            if pos > 0: pos -= 1
            else: 
                tape.insert(0, blank)
                
        if dr == 'right':
            pos += 1
            if pos >=len(tape): 
                tape.append('x')
                print('')
                print('No llega a la aceptacion')#cuando llega al estado de aceptacion en el autómata
                print('')
    
        st = s1


#se puede cambiar las reglasde transicion para otra maquina de turing
turing_M (state = 'q0', #estado inicial de la maquina de turing
              blank = 'b', #simbolo blanco de el alfabeto dela cinta
              tape = list("10010"),#inserta los elementos en la cinta
              final = 'q3',  #estado valido y/o final
              rules = map(tuple,#reglas de transicion
                          [
                          "q0 0 E right q2".split(),
                          "q0 1 T right q0".split(),
                          "q2 0 C right q2".split(),
                          "q2 1 N right q1".split(),
                          "q1 0 M left q3".split(),
                          "q1 1 H right q1".split(),

                          ]   
                         )
             )    

#COMENTARIO IMPORTANTE
#CUANDO LOS FALTAN LETRAS PARA LLEGAR A LA ACEPTACION SE MANDA MENSAJE
#CUANDO SOBRAN LETRAS, PERO SE LLEGA A CUMPLIR EL AUTÓMATA NOS LO TOMA COMO BUENA