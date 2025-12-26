# Mini projeto: webcam + Arduino (detector de mao)

Projeto simples que detecta uma mao pela webcam usando MediaPipe e liga/desliga um LED no Arduino via serial (9600 bps). O script envia `1` quando ha mao no quadro e `0` quando nao ha.

## Requisitos

- Python 3.12
- Pacotes: `mediapipe==0.10.20`, `opencv-python==4.10.0.84`, `pyserial`
- Arduino com LED no pino 10 (caso altere teria que obrigatoriamente alterar no código sketch `MAO.ino`), cabo USB e porta COM livre

## Estrutura

- `mao.py` – captura webcam, detecta mao, envia `1/0` pela serial
- `MAO.ino` – recebe `1/0` e liga/desliga LED no pino 10
- `.vscode/settings.json` – aponta o interpretador para `.venv`

## Como rodar (Windows)

```bash
# clonar
# git clone https://github.com/PauloHenriqueJunio/mini-projeto-webcam-arduino.git
# cd mini-projeto-webcam-arduino

# criar venv
python -m venv .venv

# ativar
".venv\\Scripts\\activate"

# instalar deps
python -m pip install mediapipe==0.10.20 opencv-python==4.10.0.84 pyserial

# ajustar a porta, se preciso, dentro de mao.py (variavel porta_arduino)
# rodar
python mao.py
```

Atalhos:

- Tecla `q` fecha a janela de video.
- Se usar VS Code, selecione o interpretador `.venv` no status bar ou use a configuracao de debug incluida.

## Arduino

1. Abra `MAO.ino` no Arduino IDE.
2. Ajuste a porta/board se necessario e faça upload.
3. Feche o Monitor Serial antes de rodar o script Python (para liberar a COM).