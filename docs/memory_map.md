# Memory Map

This document summarizes the known memory layout of the Amlogic boot chain used by SM1 and related SoCs.

The addresses below are collected from BootROM analysis, bootloader reverse engineering, JTAG debugging, Trusted Firmware (BL31), U-Boot and runtime memory inspection.

> **Note**
>
> Some addresses may vary between SoC families or firmware versions. The addresses below correspond to the platforms investigated in this repository (primarily SM1 / S905X3).

# Cortex-M3 Memory Map

The Cortex-M3 core is responsible for Always-On (AO) firmware and low-power management.

|    Address   | Component | Description |
|--------------|-----------|-------------|
| `0x00000000` | BootROM   | Internal Cortex-M3 BootROM |
| `0x10000000` | BL30      | Main Cortex-M3 firmware |
| `0x1000A000` | BL301     | Suspend / Resume firmware |

---

# Cortex-A53 / Cortex-A55 Memory Map

The application processor executes the secure boot chain.

|    Address   | Component | Description |
|--------------|-----------|-------------|
| `0xFFFF0000` | BootROM   | Internal BootROM |
| `0xFFFA0000` | BL2       | First-stage bootloader loaded into SRAM |
| `0x05100000` | BL31      | ARM Trusted Firmware (EL3 Secure Monitor) |
| DDR | BL33   | U-Boot relocated after DRAM initialization |

Example runtime output:

```
U-Boot 2015.01.SMC_JTAG

DRAM: 3.8 GiB

Relocation Offset:
0xD6E80000

Runtime Address:
0xD7E80000
```

---

# Security Memory

| Address | Component | Description |
|---------:|-----------|-------------|
| `0xFFFE0000` | eFuse | Secure eFuse memory |
| `0xFFFE7C00` | eFuse Shadow | Shadow copy used during boot |

---

# Peripheral Base Addresses

| Base Address | Peripheral |
|-------------:|------------|
| `0xFF630000` | eFuse Controller |
| `0xFF634000` | PERIPHS |
| `0xFF63C000` | HIU (Clock & Reset) |
| `0xFF800000` | AO Bus |
| `0xFF900000` | VCBUS |
| `0xFFD00000` | CBUS |

---

# Secure Boot Chain

# Boot Architecture

```
                  Reset
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
+----------------+      +----------------+
| A55 BootROM    |      | M3 BootROM     |
| 0xFFFF0000     |      | 0x00000000     |
+-------+--------+      +-------+--------+
        │                       │
        │                       │
        ▼                       │
+----------------+              │
| BL2            |              │
| 0xFFFA0000     |              │
+-------+--------+              │
        │                       │
        ├──────────────┐        │
        │              │        │
        ▼              ▼        │
+---------------+  +-------------+
| BL31          |  | BL30        |
| 0x05100000    |  | 0x10000000  |
+-------+-------+  +------+------+
        │                 │
        │                 ▼
        │           +-------------+
        │           | BL301       |
        │           | 0x1000A000  |
        │           +-------------+
        │
        ▼
+----------------+
| BL33 (U-Boot)  |
+----------------+
```

---

# Memory Regions

```
                High Address
+--------------------------------------------------+
| 0xFFFF0000  A55 BootROM                          |
+--------------------------------------------------+
| 0xFFFE7C00  eFuse Shadow                         |
+--------------------------------------------------+
| 0xFFFE0000  eFuse                                |
+--------------------------------------------------+
| 0xFFFD0000  Secure SRAM                          |
+--------------------------------------------------+
| 0xFFFA0000  BL2 SRAM                             |
+--------------------------------------------------+
|                                                  |
|        Peripheral Registers                      |
|                                                  |
| 0xFFD00000  CBUS                                 |
| 0xFF900000  VCBUS                                |
| 0xFF800000  AO BUS                               |
| 0xFF63C000  HIU                                  |
| 0xFF634000  PERIPHS                              |
| 0xFF630000  eFuse Controller                     |
|                                                  |
+--------------------------------------------------+
                Low Address
```

---

# Notes

This document is based on:

- BootROM reverse engineering
- BL2 analysis
- BL30 reverse engineering
- BL31 reverse engineering
- U-Boot runtime inspection
- JTAG debugging
- Live memory dumps

The memory map will be updated as additional Amlogic SoCs and bootloader versions are analyzed.
