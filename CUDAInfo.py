from __future__ import print_function
__author__      = "Zhi-Qiang Zhou"
__copyright__   = "Copyright 2017"

import pycuda.autoinit
import pycuda.driver as cuda

def cudaInfo():
    """Print CUDA information.
    """
    deviceCount = cuda.Device.count()
    print('There are {:d} CUDA device(s) detected:\n'.format(deviceCount))
    print(80 * '-')
    for device_id in range(deviceCount):
        printDeviceInfo(device_id)
        print(80 * '-')

def convertSMVer2Cores(major, minor):
    """GPU Architecture definitions.

    Args:
        major (int): major version
        minor (int): minor version

    Returns:
        int: the # of cores per SM

    """
    sm = str(major) + str(minor)
    if   sm == '30': return 192 # Kepler Generation (SM 3.0) GK10x class
    elif sm == '32': return 192 # Kepler Generation (SM 3.2) GK10x class
    elif sm == '35': return 192 # Kepler Generation (SM 3.5) GK11x class
    elif sm == '37': return 192 # Kepler Generation (SM 3.7) GK21x class
    elif sm == '50': return 128 # Maxwell Generation (SM 5.0) GM10x class
    elif sm == '52': return 128 # Maxwell Generation (SM 5.2) GM20x class
    elif sm == '53': return 128 # Maxwell Generation (SM 5.3) GM20x class
    elif sm == '60': return 64  # Pascal Generation (SM 6.0) GP100 class
    elif sm == '61': return 128 # Pascal Generation (SM 6.1) GP10x class
    elif sm == '62': return 128 # Pascal Generation (SM 6.2) GP10x class
    elif sm == '70': return 64  # Volta Generation (SM 7.0) GV100 class

def printDeviceInfo(device_id, prefix=''):
    """Print CUDA device information.

    Args:
        device_id (int): Device ID
        prefix (str): Prefix string
    """
    device = cuda.Device(device_id)
    attributes = device.get_attributes()
    attrs = {}
    for (key,value) in attributes.items():
        attrs[str(key)] = value

    major = attrs['COMPUTE_CAPABILITY_MAJOR']
    minor = attrs['COMPUTE_CAPABILITY_MINOR']
    cores = convertSMVer2Cores(major, minor)

    runtimeVersion = pycuda.driver.get_version()
    driverVersion = pycuda.driver.get_driver_version()

    print(prefix + 'Device {:d}:'.format(device_id), device.name())
    print(prefix + '  CUDA Driver Version / Runtime Version:        ', 
        '{:d}.{:d} / {:d}.{:d}'.format(
            driverVersion // 1000, (driverVersion % 100) // 10,
            runtimeVersion[0], runtimeVersion[1]))
    print(prefix + '  CUDA Capability Major/Minor version number:   ', 
        str(major) + '.' + str(minor))
    print(prefix + '  Total amount of global memory:                ', 
        device.total_memory()//1024**2, 'MBytes')
    print(prefix + '  ({:2d}) Multiprocessors x ({:3d}) CUDA Cores/MP:   '.format(
        attrs['MULTIPROCESSOR_COUNT'], cores), 
        attrs['MULTIPROCESSOR_COUNT'] * cores, 'CUDA Cores')
    print(prefix + '  GPU Clock rate:                               ', 
        attrs['CLOCK_RATE'] / 1e3, 'MHz')
    print(prefix + '  Memory Clock rate:                            ', 
        attrs['MEMORY_CLOCK_RATE'] / 1e3, 'MHz')
    print(prefix + '  Memory Bus Width:                             ', 
        '{:d}-bit'.format(attrs['GLOBAL_MEMORY_BUS_WIDTH']))
    print(prefix + '  L2 Cache Size:                                ', 
        attrs['L2_CACHE_SIZE']/1024, 'MBytes')
    print(prefix + '  Max Texture Dimension Size (x,y,z):           ', 
        '1D = ({:d})'.format(attrs['MAXIMUM_TEXTURE1D_WIDTH']))
    print(prefix + '                                                ', 
        '2D = ({:d}, {:d})'.format(attrs['MAXIMUM_TEXTURE2D_WIDTH'], 
                                   attrs['MAXIMUM_TEXTURE2D_HEIGHT']))
    print(prefix + '                                                ', 
        '3D = ({:d}, {:d}, {:d})'.format(attrs['MAXIMUM_TEXTURE3D_WIDTH'], 
                                         attrs['MAXIMUM_TEXTURE3D_HEIGHT'], 
                                         attrs['MAXIMUM_TEXTURE3D_DEPTH']))
    print(prefix + '  Max Layered Texture Size (dim) x layers:      ', 
        '1D = ({:d}) x {:d}'.format(
            attrs['MAXIMUM_TEXTURE1D_LAYERED_WIDTH'], 
            attrs['MAXIMUM_TEXTURE1D_LAYERED_LAYERS']))
    print(prefix + '                                                ', 
        '2D = ({:d}, {:d}) x {:d}'.format(
            attrs['MAXIMUM_SURFACE2D_LAYERED_WIDTH'], 
            attrs['MAXIMUM_SURFACE2D_LAYERED_HEIGHT'], 
            attrs['MAXIMUM_SURFACE2D_LAYERED_LAYERS']))
    print(prefix + '  Total amount of constant memory:              ', 
        attrs['TOTAL_CONSTANT_MEMORY'], 'Bytes')
    print(prefix + '  Total amount of shared memory per block:      ', 
        attrs['MAX_SHARED_MEMORY_PER_BLOCK'], 'Bytes')
    print(prefix + '  Total number of registers available per block:', 
        attrs['MAX_REGISTERS_PER_BLOCK'])
    print(prefix + '  Warp size:                                    ', 
        attrs['WARP_SIZE'])
    print(prefix + '  Maximum number of threads per multiprocessor: ', 
        attrs['MAX_THREADS_PER_MULTIPROCESSOR'])
    print(prefix + '  Maximum number of threads per block:          ', 
        attrs['MAX_THREADS_PER_BLOCK'])
    print(prefix + '  Maximum sizes of each dimension of a block:   ', 
        '{:d} x {:d} x {:d}'.format(attrs['MAX_BLOCK_DIM_X'], 
                                    attrs['MAX_BLOCK_DIM_Y'], 
                                    attrs['MAX_BLOCK_DIM_Z']))
    print(prefix + '  Maximum sizes of each dimension of a grid:    ', 
        '{:d} x {:d} x {:d}'.format(attrs['MAX_GRID_DIM_X'], 
                                    attrs['MAX_GRID_DIM_Y'], 
                                    attrs['MAX_GRID_DIM_Z']))
    print(prefix + '  Maximum memory pitch:                         ', 
        attrs['MAX_PITCH'], 'Bytes')
    print(prefix + '  Texture alignment:                            ', 
        attrs['TEXTURE_ALIGNMENT'], 'Bytes')
    print(prefix + '  Concurrent copy and kernel execution:         ', 
        '{} with {:d} copy engine(s)'.format(
            bool(attrs['CONCURRENT_KERNELS']), 
            attrs['ASYNC_ENGINE_COUNT']))
    print(prefix + '  Run time limit on kernels:                    ', 
        bool(attrs['KERNEL_EXEC_TIMEOUT']))
    print(prefix + '  Integrated GPU sharing Host Memory:           ', 
        bool(attrs['INTEGRATED']))
    print(prefix + '  Support host page-locked memory mapping:      ', 
        bool(attrs['CAN_MAP_HOST_MEMORY']))
    print(prefix + '  Alignment requirement for Surfaces:           ', 
        bool(attrs['SURFACE_ALIGNMENT']))
    print(prefix + '  Device has ECC support:                       ', 
        bool(attrs['ECC_ENABLED']))
    print(prefix + '  Device supports Unified Addressing (UVA):     ', 
        bool(attrs['UNIFIED_ADDRESSING']))
    print(prefix + '  Device PCI Bus ID / PCI location ID:          ', 
        attrs['PCI_BUS_ID'], '/', attrs['PCI_DEVICE_ID'])
    print(prefix + '  Compute Mode:                                 ', 
        attrs['COMPUTE_MODE'])

if __name__ == '__main__':

    cudaInfo()
