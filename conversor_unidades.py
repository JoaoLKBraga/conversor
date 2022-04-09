import locale
import pint
import units

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
ureg = pint.UnitRegistry()

imput = input("Metros ou Dolar  ")
if(imput.lower() == "metros"):
    metros = float( input("Digite quantos metros  ")) * ureg.meter

    print ("SI =  {}".format(metros.to_base_units().format_babel(locale='pt_BR')))
    print ("Centimetros = {}".format(metros.to('cm').format_babel(locale='pt_BR')))

elif(imput.lower() == "dolar"):
    resul = float( input("Digite quantos dolares  ")) * float(units.cotacao_usdbrl)

    print(locale.currency(resul, grouping=True))
else:
    print("Error")