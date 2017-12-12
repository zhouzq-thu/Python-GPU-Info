from __future__ import print_function
__author__      = "Zhi-Qiang Zhou"
__copyright__   = "Copyright 2017"

import pyopencl as cl

def openclInfo():
    """Print OpenCL information.
    """
    platforms = cl.get_platforms()
    print('There are {:d} platform(s) detected:\n'.format(len(platforms)))
    print(70 * '-')
    for platform_id, platform in enumerate(platforms):
        print('Platform:             ', platform.name)
        print('Vendor:               ', platform.vendor)
        print('Version:              ', platform.version)
        print('Number of devices:    ', len(platform.get_devices()))
        print('  ' + 68 * '-')
        for device_id, device in enumerate(platform.get_devices()):
            printDeviceInfo(platform_id, device_id, prefix='  ')
            print('  ' + 68 * '-')

def printDeviceInfo(platform_id, device_id, prefix=''):
    """Print OpenCL device information.

    Args:
        platform_id (int): Platform ID
        device_id (int): Device ID
        prefix (str): Prefix string
    """
    platforms = cl.get_platforms()
    devices = platforms[platform_id].get_devices()
    device = devices[device_id]
    print(prefix + 'Device {:d}:'.format(device_id), str(device.name), 
        '[Type: {:s}]'.format(cl.device_type.to_string(device.type)))
    print(prefix + '  Device version:               ', device.version)
    print(prefix + '  Driver version:               ', device.driver_version)
    print(prefix + '  Vendor:                       ', device.vendor)
    print(prefix + '  Available:                    ', bool(device.available))
    print(prefix + '  Address bits:                 ', device.address_bits)
    print(prefix + '  Max compute units:            ', device.max_compute_units)
    print(prefix + '  Max clock frequency:          ', device.max_clock_frequency, 'MHz')
    print(prefix + '  Global memory:                ', int(device.global_mem_size / 1024**2), 'MB')
    print(prefix + '  Global cache memory:          ', int(device.global_mem_cache_size), 'B')
    print(prefix + '  Local memory:                 ', int(device.local_mem_size / 1024), 'KB')
    print(prefix + '  Max allocable memory:         ', int(device.max_mem_alloc_size / 1024**2), 'MB')
    print(prefix + '  Max constant args:            ', device.max_constant_args)
    print(prefix + '  Max work group size           ', device.max_work_group_size)
    print(prefix + '  Max work item dimensions:     ', device.max_work_item_dimensions)
    print(prefix + '  Max work item size:           ', device.max_work_item_sizes)
    print(prefix + '  Image support:                ', bool(device.image_support))
    print(prefix + '  Max Image2D size (H x W):     ', device.image2d_max_height, 'x', 
        device.image2d_max_width)
    print(prefix + '  Max Image3D size (D x H x W): ', device.image3d_max_depth, 'x', 
        device.image3d_max_height, 'x', device.image3d_max_width)

if __name__ == '__main__':

    openclInfo()
