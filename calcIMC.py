#Importando as bibliotecas.
import streamlit as st

#Exibindo texto de boas-vindas.
st.header('Bem-vindo ao aplicativo de cálculo do Índice de Massa Corporal (IMC)!')

#Informação sobre o peso em quilogramas (kg)
mass = st.number_input('Qual seu peso em quilogramas (kg)?')

#Informação sobre a altura
high = st.number_input('Qual sua altura?')

#Informe a unidade de medida da sua altura.
unite = st.radio('Qual a unidade de medida de sua altura?',
                  ('m', 'cm', 'ft'))

success = False

if unite == 'm':
    try:
        bmi = mass/(high**2)
        success = True
    except:
        st.text('Use apenas números em peso e altura!')
elif unite == 'cm':
    try:
        bmi = mass/((high/100)**2)
        success = True
    except:
        st.text('Use apenas números em peso e altura!')
else:
    try:
        bmi = mass/((high/3.2808)**2)
        success = True
    except:
        st.text('Use apenas números em peso e altura!')

#Criar botão de cálculo
if st.button('Calcula IMC'):
    if success:
        st.text(f"Seu índice de massa corporal é '{bmi}'.")
        #Classifica sua condição
        if bmi < 16:
            st.error('Você está extremamente abaixo do peso.')
        elif bmi >= 16 and bmi < 18.5:
            st.warning('Vocè está abaixo do peso.')
        elif bmi >= 18.5 and bmi < 25:
            st.success('Você está saudável.')
        elif bmi >= 25 and bmi < 30:
            st.warning('Você tem sobrepso.')
        elif(bmi >= 30):
            st.error('Você está extremamente acima do peso.')
    else:
        st.error('Peso e altura devem ser digitados e corresponder a número diferente de zero.')

conn = st.connection('mysql', type='sql')




