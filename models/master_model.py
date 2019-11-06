'''Mater dictionary structure guide
NOTE: Additional values may be inserted, this is a guide only
CPU: For each cpu... cpu[index] = value
RAM: In order of the call response array
'''


master = {
    'resources': {
        'cpu': {
            '0' : 0.0,
            '1' : 0.0,
            '2' : 0.0,
            '4' : 0.0
        },
        'ram': {
            'total': 0,
            'available': 0,
            'percent': 0.0,
            'used': 0,
            'free': 0,
            'active': 0,
            'inactive': 0,
            'buffers': 0,
            'cached': 0,
            'shared': 0,
            'slab': 0
        },
        'swap': {
            'total': 0,
            'used': 0,
            'free': 0,
            'percent': 0,
            'sin': 0,
            'sout': 0
        },
        'disk_partitions': []
        },
        'disk_usage': {
            'C:/': {
                'total': 0,
                'used' : 0,
                'free' : 0,
                'percent' : 0
            }
        },
        'disk_io': {
            'PhysicalDrive0': {
                'read_count': 0,
                'read_count_sec': 0,
                'write_count': 0,
                'write_count_sec': 0,
                'read_bytes': 0,
                'read_bytes_sec': 0,
                'write_bytes': 0,
                'write_bytes_sec': 0,
                'read_time': 0,
                'read_time_sec': 0,
                'write_time': 0,
                'write_time_sec': 0
            },
        },
        'network': {

        }

}