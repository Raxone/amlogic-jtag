# Amlogic JTAG

## Supported SoCs

Current research primarily focuses on:

* SM1 (S905X3) (X96 Max Plus, Board Q5x3_141 V3.1 19351)
    Most X96 Max boards provide accessible JTAG test points on the PCB.
* GXL (S905W / S905X)
    Depending on the board revision, JTAG is available either through PCB test points or the SD-card connector.
* SC2 (S905x4) (A95 F4)
    JTAG is routed through the SD-card connector
    
## JTAG Pinout

AO JTAG (GXL / G12A / SM1):

|   GPIO   |  JTAG  |
|----------|--------|
| GPIOAO_6 |  TDI   |
| GPIOAO_7 |  TDO   |
| GPIOAO_8 |  TMS   |
| GPIOAO_9 |  TCK   |

## microSD Debug Pinout (Tested)

| Pin | SD_Card| UART/JTAG|
|-----|--------|----------|
|  1  |  DAT2  | UART TX  |
|  2  |  DAT3  | UART RX  |
|  3  |  CMD   | JTAG TMS |
|  4  |  VDD   | 3.3V     |
|  5  |  CLK   | JTAG TCK |
|  6  |  GND   | GND      |
|  7  |  DAT0  | JTAG TDO |
|  8  |  DAT1  | JTAG TDI |


Support for additional Amlogic SoCs will be added as research progresses.

## Project Status

This project is under active development.

Documentation will expand as additional hardware is analyzed and new findings are verified.

## Contributing

Contributions are welcome.

If you discover undocumented registers, memory regions, pin configurations, or debugging techniques, feel free to open an issue or submit a pull request.

## Disclaimer

This repository is intended for educational, research, and interoperability purposes.

Always comply with applicable laws, licenses, and the terms governing the hardware and software you are working with.

## License

This project is licensed under the MIT License.

