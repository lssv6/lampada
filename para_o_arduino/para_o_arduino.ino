// Definimos uma constante para a saída de energia do led
#define PIN_LED 25

// Variável de controle de entrada de dados
int entrada;


// FUNÇÃO SETUP
// É executado uma vez e configura a conexão serial
// para trabalhar com dados a 9600 bauds/s.
// Também configura a porta <PIN_LED> como saída(OUTPUT).
void setup() {
  Serial.begin(9600);
  pinMode(PIN_LED, OUTPUT);
}


// FUNÇÃO LOOP
// Vai fazer a comunicação serial com o arduino.
// Implementa o seguinte pseudo-código
// se(serial.estaDisponivel = 👍):
//   entrada = serial.lerbyte // char entre 0 e 255
//   se(entrada == 76):// 76 é o código ASCII de 'L'
//     ligar led
//   else if(entrada == 68):// 68 é o código ASCII de 'D'
//     desligar led

void loop() {
  if(Serial.available() > 0){
    entrada = Serial.read();
    if(entrada == 76){
      digitalWrite(PIN_LED, HIGH);
    }else if(entrada == 68){
      digitalWrite(PIN_LED, LOW);
    }
    delay(10);//XXX: Segundo a internet é melhor por um sleep.
  }
}
