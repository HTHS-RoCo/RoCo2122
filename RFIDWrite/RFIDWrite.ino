#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9
#define SS_PIN 10

MFRC522 mfrc522(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key key;
MFRC522::StatusCode status;

void setup() {
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();
}

void loop() {
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;
  if (!mfrc522.PICC_IsNewCardPresent()) return;
  if (!mfrc522.PICC_ReadCardSerial()) return;
  Serial.setTimeout(20000L);

  byte block = 4;
  byte buffr[] = "RoCo2022        ";
  writeBytesToBlock(block, buffr);

  Serial.println();
  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();
}

void writeBytesToBlock(byte block, byte buff[]) {
  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("PCD_Authenticate() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  } else Serial.println(F("PCD_Authenticate() success"));

  status = mfrc522.MIFARE_Write(block, buff, 16);
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("MIFARE_Write() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  } else Serial.println(F("MIFARE_Write() success"));
}
