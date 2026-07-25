# Amlogic S905X3 BootROM
## USB Password Authentication Sequence

Status:
    Reverse engineering in progress

------------------------------------------------------------
1. BootROM enters USB Download Mode
------------------------------------------------------------

PC:
    0xffff8250

Responsible functions:

    FUN_ffff8250()

Initializes:

    USB controller
    USB endpoints
    Endpoint state
    RX/TX descriptors

Calls:

    FUN_ffff80e8()
    FUN_ffff81ec()

------------------------------------------------------------
2. USB packet received
------------------------------------------------------------

Incoming USB packet arrives in

    USB FIFO
        0xff401000

BootROM endpoint structure

    0xfffe3888

contains

    rx_buffer = 0xfffe7000

------------------------------------------------------------
3. Copy FIFO -> SRAM
------------------------------------------------------------

Function

    FUN_ffff7c00()

Operation

    while (remaining)
    {
        *dst = USB_FIFO;
        dst += 4;
    }

Observed:

    x3 = 0xff401000

    ldr w3,[x3]

    str w3,[0xfffe7000]

Example

FIFO

    73736170
    64726f77

becomes

SRAM

    73736170
    64726f77

ASCII

    password

This function performs only the copy.

No parsing.

No hashing.

No validation.

------------------------------------------------------------
4. Update endpoint state
------------------------------------------------------------

Function

    FUN_ffff7c64()

Updates

    endpoint read pointer

Fields

    read_offset
    write_offset
    available bytes

Located around

    0xfffe3888

------------------------------------------------------------
5. USB receive manager
------------------------------------------------------------

Function

    FUN_ffff7d70()

Calls

    FUN_ffff7c00()
    FUN_ffff7c64()

Responsible for

    receiving complete USB packet

Acts as

    USB RX manager

------------------------------------------------------------
6. USB polling loop
------------------------------------------------------------

Function

    FUN_ffff7ef8()

Continuously

    checks endpoints

When packet available

    calls FUN_ffff7c64()

Appears to be

    USB scheduler

------------------------------------------------------------
7. USB initialization
------------------------------------------------------------

Function

    FUN_ffff80e8()

Configures

    USB controller

Registers

    ff400800
    ff400804
    ff400900
    ff400b00...

------------------------------------------------------------
8. USB enable
------------------------------------------------------------

Function

    FUN_ffff81ec()

Enables

    USB download mode

Calls

    FUN_ffff6948()

------------------------------------------------------------
9. Password verification
------------------------------------------------------------

NOT located in

    FUN_ffff7c00()

NOT located in

    FUN_ffff7c64()

NOT located in

    FUN_ffff7d70()

Those functions only move data.

Verification occurs later after

    complete password packet

has been received.

------------------------------------------------------------
Current understanding
------------------------------------------------------------

USB FIFO
    0xff401000

        │

        ▼

FUN_ffff7c00()
    FIFO → SRAM

        │

        ▼

0xfffe7000
    USB receive buffer

        │

        ▼

FUN_ffff7c64()
    update endpoint state

        │

        ▼

FUN_ffff7d70()
    receive manager

        │

        ▼

command dispatcher

        │

        ▼

password verification

        │

        ▼

SHA-256 / salt / efuse comparison
        (not yet located)

------------------------------------------------------------
Interesting observations
------------------------------------------------------------

password.bin contains

    "password"

BootROM copies it verbatim into

    0xfffe7000

using

    ldr w3,[0xff401000]
    str w3,[0xfffe7000]

before any processing occurs.

This proves that

    FUN_ffff7c00()

is only the USB receive routine.

The password authentication logic is located later in the BootROM execution path.
