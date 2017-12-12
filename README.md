# Python-GPU-Info
Get CUDA and OpenCL information using python

## Get CUDA Information

1. Install [pycuda](https://mathema.tician.de/software/pycuda/) package:

  ```shell
  pip install pycuda
  ```

2. Run the following script:

  ```shell
  python CUDAInfo.py
  ```

Example output:

```
There are 1 CUDA device(s) detected:

--------------------------------------------------------------------------------
Device 0: GeForce GTX 1080
  CUDA Driver Version / Runtime Version:         9.1 / 9.0
  CUDA Capability Major/Minor version number:    6.1
  Total amount of global memory:                 8191 MBytes
  (20) Multiprocessors x (128) CUDA Cores/MP:    2560 CUDA Cores
  GPU Clock rate:                                1733.5 MHz
  Memory Clock rate:                             5005.0 MHz
  Memory Bus Width:                              256-bit
  L2 Cache Size:                                 2048.0 MBytes
  Max Texture Dimension Size (x,y,z):            1D = (131072)
                                                 2D = (131072, 65536)
                                                 3D = (16384, 16384, 16384)
  Max Layered Texture Size (dim) x layers:       1D = (32768) x 2048
                                                 2D = (32768, 32768) x 2048
  Total amount of constant memory:               65536 Bytes
  Total amount of shared memory per block:       49152 Bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Maximum sizes of each dimension of a block:    1024 x 1024 x 64
  Maximum sizes of each dimension of a grid:     2147483647 x 65535 x 65535
  Maximum memory pitch:                          2147483647 Bytes
  Texture alignment:                             512 Bytes
  Concurrent copy and kernel execution:          True with 2 copy engine(s)
  Run time limit on kernels:                     True
  Integrated GPU sharing Host Memory:            False
  Support host page-locked memory mapping:       True
  Alignment requirement for Surfaces:            True
  Device has ECC support:                        False
  Device supports Unified Addressing (UVA):      True
  Device PCI Bus ID / PCI location ID:           196 / 0
  Compute Mode:                                  DEFAULT
--------------------------------------------------------------------------------
```

## Get OpenCL Information

1. Install [pyopencl](https://mathema.tician.de/software/pyopencl/) package:

  ```shell
  pip install pyopencl
  ```

2. Run the following script:

  ```shell
  python CUDAInfo.py
  ```

Example output:

```
There are 1 platform(s) detected:

----------------------------------------------------------------------
Platform:              Apple
Vendor:                Apple
Version:               OpenCL 1.2 (Oct 31 2017 18:19:43)
Number of devices:     4
  --------------------------------------------------------------------
  Device 0: Intel(R) Core(TM) i7-6920HQ CPU @ 2.90GHz [Type: CPU]
    Device version:                OpenCL 1.2 
    Driver version:                1.1
    Vendor:                        Intel
    Available:                     True
    Address bits:                  64
    Max compute units:             8
    Max clock frequency:           2900 MHz
    Global memory:                 16384 MB
    Global cache memory:           64 B
    Local memory:                  32 KB
    Max allocable memory:          4096 MB
    Max constant args:             8
    Max work group size            1024
    Max work item dimensions:      3
    Max work item size:            [1024, 1, 1]
    Image support:                 True
    Max Image2D size (H x W):      8192 x 8192
    Max Image3D size (D x H x W):  2048 x 2048 x 2048
  --------------------------------------------------------------------
  Device 1: Intel(R) HD Graphics 530 [Type: GPU]
    Device version:                OpenCL 1.2 
    Driver version:                1.2(Nov  9 2017 18:56:42)
    Vendor:                        Intel Inc.
    Available:                     True
    Address bits:                  64
    Max compute units:             24
    Max clock frequency:           1050 MHz
    Global memory:                 1536 MB
    Global cache memory:           0 B
    Local memory:                  64 KB
    Max allocable memory:          384 MB
    Max constant args:             8
    Max work group size            256
    Max work item dimensions:      3
    Max work item size:            [256, 256, 256]
    Image support:                 True
    Max Image2D size (H x W):      16384 x 16384
    Max Image3D size (D x H x W):  2048 x 2048 x 2048
  --------------------------------------------------------------------
  Device 2: AMD Radeon Pro 460 Compute Engine [Type: GPU]
    Device version:                OpenCL 1.2 
    Driver version:                1.2 (Nov  9 2017 18:48:40)
    Vendor:                        AMD
    Available:                     True
    Address bits:                  32
    Max compute units:             16
    Max clock frequency:           907 MHz
    Global memory:                 4096 MB
    Global cache memory:           0 B
    Local memory:                  32 KB
    Max allocable memory:          1024 MB
    Max constant args:             8
    Max work group size            256
    Max work item dimensions:      3
    Max work item size:            [256, 256, 256]
    Image support:                 True
    Max Image2D size (H x W):      16384 x 16384
    Max Image3D size (D x H x W):  2048 x 2048 x 2048
  --------------------------------------------------------------------
  Device 3: GeForce GTX 1080 [Type: GPU]
    Device version:                OpenCL 1.2 
    Driver version:                10.29.10 378.10.10.10.25.102
    Vendor:                        NVIDIA
    Available:                     True
    Address bits:                  64
    Max compute units:             20
    Max clock frequency:           1139 MHz
    Global memory:                 8192 MB
    Global cache memory:           0 B
    Local memory:                  48 KB
    Max allocable memory:          2048 MB
    Max constant args:             8
    Max work group size            1024
    Max work item dimensions:      3
    Max work item size:            [1024, 1024, 64]
    Image support:                 True
    Max Image2D size (H x W):      32768 x 32768
    Max Image3D size (D x H x W):  2048 x 16384 x 16384
  --------------------------------------------------------------------
```

## License

MIT