from flask import Flask, request
app = Flask(__name__)


@app.route("/") # Route 1
def hello_world():

    return """
                <form action="/skaicius">
                    <label for="test">skaicius 1</label><br>
                        <input type="text" id="test" name="test" value="0"><br>
                        </br></br>

                    <label for="test2">skaicius 2</label><br>
                        <input type="text" id="test2" name="test2" value="0"><br><br>
                        </br></br>
                    
                     <label for="zenklas" >zenklas </label><br>
                        <input type="text" id="test2" name="test2" value="0"><br><br>
                        </br></br>

                    <input type="submit" value="Submit">
                </form> 
            """

@app.route("/labas")  # Route 2
def sakyk_labas():
    global skaicius ## Naudoju globalu kintamaji
    skaicius = skaicius +1 ## kaskart atidare pridedam 1
    return f"Labas {skaicius}"


    '''
        /skaicius?test=100
        /skaicius?test=0  &  test2=0
    '''

skaicius = 0 #apsiraspme kintamaji (Globalus)

def sudetis (pirmas,antras):
        return pirmas+antras

def atimtis (pirmas,antras):
    return pirmas-antras

def daugyba (pirmas,antras):
    return pirmas * antras

def dalyba (pirmas,antras):
    if antras !=0:
        return pirmas/antras
    else:
        return "Dalyba is nulio negalima"

@app.route("/skaicius") # Route 3
def skaiciavimo():
    #UZKLAUSA. ARGUMENTAI. METODAS()
    if not request.args.get("test") or not request.args.get ("test2"):
        return "nera argumento"
    skaicius = request.args.get("test") ### Pasiimam argumenta is URL pvz.: /skaicius?test=100
    skaicius2 = request.args.get("test2") ### Pasiimam argumenta 2 is URL pvz.: /skaicius?test2=100
    suma = sudetis(int(skaicius2),int(skaicius))
    return f"Tavo ivestas skaicius: {suma}"


''' 1 susidiegiame Flask
        pip3 install Flask
        pip install Flask
'''


# 1. Susidiegiame Flask
    # pip3 install Flask

# 2. Importuojame

kintamasis = 1
kintamasis = 2

def finkcija():
    print(kintamasis)
    print(kintamasis2)
    print(f'test:{kintamasis2}{kintamasis}')
    print('test:{}{}'.format(kintamasis2,kintamsis))



    #Komentaras 1

    """
        Komentaras 2

    """

    '''
        Komentaras 3
    '''


    # Apibrėžiame funkciją skaiciuotuvas
def skaiciuotuvas():
    print("Paprastas skaičiuotuvas")
    print("Pasirinkite operaciją:")
    print("1. Sudėtis")
    print("2. Atimtis")
    print("3. Daugyba")
    print("4. Dalyba")

    # Vykdoma operacija pagal vartotojo pasirinkimą
    pasirinkimas = input("Įveskite operacijos numerį (1/2/3/4): ")

    if pasirinkimas in ('1', '2', '3', '4'):
        num1 = float(input("Įveskite pirmą skaičių: "))
        num2 = float(input("Įveskite antrą skaičių: "))

        if pasirinkimas == '1':
            print(num1, "+", num2, "=", num1 + num2)
        elif pasirinkimas == '2':
            print(num1, "-", num2, "=", num1 - num2)
        elif pasirinkimas == '3':
            print(num1, "*", num2, "=", num1 * num2)
        elif pasirinkimas == '4':
            if num2 != 0:
                print(num1, "/", num2, "=", num1 / num2)
            else:
                print("Dalyba iš nulio negalima!")
    else:
        print("Netinkamas pasirinkimas. Bandykite dar kartą.")



# Iškviečiame funkciją skaiciuotuvas



if __name__ == "__main__":
    app.run()
