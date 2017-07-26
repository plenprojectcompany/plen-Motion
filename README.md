Motion | PLEN Project Company Inc.
===============================================================================

Motion files (JSON) for PLEN series robots.

## Description of the Files

- `/motion-empty`: Dummy motion files for the all slots
- `/motion-plen1.4`: Default motion files for PLEN1.4 (PLEN.D)
- `/motion-plen1.4-extra`: Additional motion files for PLEN1.4 (PLEN.D)
- `/motion-plen2`: Default motion files for PLEN2
- `sdk`: Development kit for motion files
    - `device_map.json`: The file indicates the relationship between **'device name'** -> **'device address'**.
    - `device_map.rev.json`: The file indicates the relationship between **'device address'** -> **'device name'**.
    - `metadata.py`: Metadata adding python script
    - `motion.schema.json`: The file indicates the motion structure using [JSON schema](http://json-schema.org/).
    - `naming.py`: Renaming python script (Automatically name a file from `motion['slot']` and `motion['name']`.)
    - `prettify.py`: JSON Prettifying python script

## Attention!

There are some types of **PLEN2**, thus motion files should be choosed considering your PLEN2.
Just for reference, you could check the version of your PLEN2 seeing a servo motor.

If you are using the servo motor **A**, recommended version is [plen2-old](https://github.com/plenprojectcompany/plen-Motion/tree/plen2-old).
If not (using **B**), any latest version is OK.

## How to Use the SDK
### metadata.py

`python metadata.py -f <MOTION_FILES>`

- `-t`: Set up target device in `motion['@metadata']['target']`.
- `-v`: Set up required firmware version in `motion['@metadata']['required_firmware']`.

**Attention!**: This script overwrites given files.

### naming.py

`python naming.py -f <MOTION_FILES>`

**Attention!**: This script overwrites given files.

### prettify.py

`python prettify.py -f <MOTION_FILES>`

**Attention!**: This script overwrites given files.

## Copyright (c) 2017,
- [PLEN Project Company Inc.](https://plen.jp)

## Build Environment
### OS
- Windows 8.1 Professional 64 bit

### Programming Tools (SDK)
- Python 3.6.1

## License
These files are released under [the MIT License](https://opensource.org/licenses/mit-license.php).