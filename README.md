# WASM - Collection of run-time Decoders

### Matan Dombelski's and Arad Zulti's Graduation project

## Project's Goals

We would like to enable websites to hide their Javasctipt code. \
We send decoder which create the hidden code at run-time. 

## Phases

Each of the following is a standalone decoder:

| Project | Description |
| ------- | ----------- |
| Phase 1 | Poc - running Js code from Wasm |
| Phase 3 | Encryption, using substitution cipher, at preprocessing, decryption at run-time |
| Phase 4 | Encryption, using AES cipher, at preprocessing, decryption at run-time |
| Phase 5 | Read the code from text file |
| Phase 6 | Create a Lookup Tabel of chars |
| Phase 7 | Create a Lookup Tabel of chars, and saving it dynamically |
| Phase 8 | Create a Lookup Tabel of stings |
| Phase 9 | Create the code by a web library |
| Phase 10 | Steganography. Hide the code inside an image |
| Phase 11 | Hide the code inside classes, and build it using virtual functions |
| Phase 12 | Hide the encrypted code inside an image |
| Phase 13 | Combination of P.9, P.11 |
| Phase 14 | Run the code only when the user move his mouse to certain location |
| Phase 15 | Like P.14, with advance to how we run the code |
| Phase 16 | Combination of P.13, P.15 |

## Project structure
 
Every phase has tree folders:

| Folder | Purpose |
| ------ | ------- |
| src    | Source files |
| build  | Bat build script |
| code   | where we saved the code we wanted to hide |

## Build instrsuctions (on Windows)

### Prerequisites

-  Emscripten - we assume it stand next to repository folder
|-- WebAssDecoder
|-- emsdk-master

### How to build and run

#### Using bat file

- Go to `build` folder and run `build_and_run.bat` \
first arg: files to compile root folder, second arg: output location (assume: build/main.js) 
- The script run server. Navigate to: [http://localhost:8080](http://localhost:8080)

#### Using VS code

- Open main file 
- In the toolbar. Terminal -> Run Task... -> Wasm Build
- The script run server. Navigate to: [http://localhost:8080](http://localhost:8080)
